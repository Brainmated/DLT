import tkinter as tk
from tkinter import filedialog, messagebox, Text
from pdf2image import convert_from_path
import pytesseract
from PIL import Image
import tempfile

# Configure pytesseract path to the location where Tesseract-OCR is installed
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Update the path if necessary

# Function to perform OCR on an image
def ocr_image(image_path, lang='ell'):
    try:
        image = Image.open(image_path)
        text = pytesseract.image_to_string(image, lang=lang)
        return text
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while processing the image: {e}")
        return ""

# Function called when the "Browse" button is clicked
def browse_files():
    file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    if file_path:
        entry.delete(0, tk.END)
        entry.insert(0, file_path)

# Function called when the "Start OCR" button is clicked
def start_ocr():
    pdf_path = entry.get()
    if pdf_path:
        with tempfile.TemporaryDirectory() as path:
            images_from_path = convert_from_path(pdf_path, output_folder=path)
            text_output.delete('1.0', tk.END)  # Clear the text area before inserting new text
            for page_number, image in enumerate(images_from_path):
                text = ocr_image(image.filename, 'ell')
                text_output.insert(tk.END, f"Text from page {page_number + 1}:\n{text}\n")
                text_output.insert(tk.END, "-"*80 + "\n")  # Separator between pages
    else:
        messagebox.showwarning("Warning", "Please select a PDF file.")

# Create the main window
root = tk.Tk()
root.title("PDF OCR Tool")

# Create the entry widget for selecting files
entry = tk.Entry(root, width=50)
entry.pack(pady=10)

# Create "Browse" button
browse_button = tk.Button(root, text="Browse", command=browse_files)
browse_button.pack(pady=5)

# Create "Start OCR" button
start_button = tk.Button(root, text="Start OCR", command=start_ocr)
start_button.pack(pady=5)

# Create text widget to display results
text_output = Text(root, wrap='word', height=20)
text_output.pack(pady=10)

# Run the application
root.mainloop()
