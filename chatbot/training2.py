import json
import re
from nltk.tokenize import word_tokenize
from difflib import get_close_matches
from google.cloud import translate_v2 as translate

def load_knowledge_base(file_path: str) -> dict:
    with open(file_path, "r") as file:
        data: dict = json.load(file)
    return data

#take file_path as a string and data as a dictionary
def save_knowledge_base(file_path: str, data: dict):
    with open(file_path, "w") as file:
        json.dump(data, file, indent=2)

def preprocess_text(text: str) -> str:
    # Convert text to lowercase
    text = text.lower()
    
    # Remove punctuation
    text = re.sub(r'[^\w\s]', '', text)
    
    return text

def tokenize_text(text: str) -> list[str]:
    # Tokenize the text into individual words
    tokens = word_tokenize(text)
    
    return tokens

def find_best_match(user_question: str, questions: list[str]) -> str | None:
    # Preprocess user question
    user_question = preprocess_text(user_question)
    
    # Tokenize user question
    user_tokens = tokenize_text(user_question)
    
    # Preprocess and tokenize knowledge base questions
    kb_tokens = [tokenize_text(preprocess_text(q)) for q in questions]
    
    # Find best match using tokenized questions
    best_match = get_close_matches(user_tokens, kb_tokens, n=1, cutoff=0.6)
    
    # Return matches if found
    return questions[kb_tokens.index(best_match[0])] if best_match else None

def find_best_match(user_question: str, questions: list[str]) -> str | None:
    #from the function imported get_close_matches
    #n returns the best possible match depending on request
    #cutoff is accuracy
    matches: list = get_close_matches(user_question, questions, n=1, cutoff=0.6)
    
    #return matches if it finds any
    return matches[0] if matches else None

#this method will return a string or None based on the availability found in the dictionary
def get_answer_for_question(question: str, knowledge_base: dict) -> str | None:
    for q in knowledge_base["questions"]:
        if q["question"] == question:
            return q["answer"]
        
#NOTE THIS ISNT WORKING YET
def translate_text(text: str, target_language: str) -> str:
    # Initialize the translation client
    client = translate.Client()

    #line 178, in __init__  
    #credentials, _ = google.auth.default(scopes=scopes)
    
    # Translate the text to the target language
    translation = client.translate(text, target_language=target_language)
    
    # Return the translated text
    return translation["translatedText"]
        
def chat_bot():
    knowledge_base: dict = load_knowledge_base("data/knowledge_base.json")
    translated_input="" #-----------------------------------------------------------WORK ON THIS----------------------------------------------------------------------------
    while True:
        user_input: str = input("You: ")

        if user_input.lower() == "quit":
            break
        #get best match by getting the user input and find a list compression
        #it looks in the list of "question" at the q of knowledge_base at the index of "questions"
        best_match: str | None = find_best_match(user_input, [q["question"] for q in knowledge_base["questions"]])
        # Translate the user input to a target language
        translated_input = translate_text(user_input, target_language="en")
        
        if best_match:
            answer: str = get_answer_for_question(best_match, knowledge_base)
            print(f"Bot: {answer}")
        else:
            print("Bot: I don't know the answer. Can you teach me by typing down the proper answer?")
            new_answer: str = input('Type the answer or "skip" to skip: ')

            if new_answer.lower() != "skip":
                #the knowledge_base at the index of 'questions' is going to append the new answer
                knowledge_base["questions"].append({"question": user_input, "answer": new_answer})
                #this way, knowledge_base.json has been updated
                #now accessed again
                save_knowledge_base("data/knowledge_base.json", knowledge_base)

                print("Bot: Thank you, I learned a new response!")
    
if __name__ == "__main__":
    chat_bot()
