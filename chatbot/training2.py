import json
from difflib import get_close_matches

def load_knowledge_base(file_path: str) -> dict:
    with open(file_path, "r") as file:
        data: dict = json.load(file)
    return data

#take file_path as a string and data as a dictionary
def save_knowledge_base(file_path: str, data: dict):
    with open(file_path, "w") as file:
        json.dump(data, file, indent=2)

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
        
def chat_bot():
    knowledge_base: dict = load_knowledge_base("knowledge_base.json")

    while True:
        user_input: str = input("You: ")

        if user_input.lower() = "quit":
            break
        #get best match by getting the user input and find a list compression
        #it looks in the list of "question" at the q of knowledge_base at the index of "questions"
        best_match: str | None = find_best_match(user_input, [q["question"] for q in knowledge_base["questions"]])

        if best_match:
            answer: str = get_answer_for_question(best_match, knowledge_base)
            print(f"Bot: {answer}")
        else:
            print("Bot: I don't know the answer. Can you teach me by typing down the proper answer?")
            new_answer: str = input('Type the answer or "skip" to skip: ')

            if new_answer.lower() != "skip":
                #the knowledge_base at the index of 'questions' is going to append the new answer
                knowledge_base = []
