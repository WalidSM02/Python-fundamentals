import json
from difflib import get_close_matches

def load_knowladge_base(file_path: str) -> dict:
    with open(file_path, 'r') as file:
        data: dict = json.load(file)
    return data

def save_knowladge_base(file_path:str, data:dict):
    with open(file_path,"w") as file:
        json.dump(data, file, indent=2)
        
def find_best_matches(user_question:str, questions:list[str]) -> str| None:
    matches:list = get_close_matches(user_question, questions, n=1, cutoff = 0.6)
    return matches[0] if matches else None

def get_answer_for_question(question:str, knowladge_base: dict) -> str| None:
    for i in knowladge_base["question"]:
        if i["question"]== question:
            return i["answer"]
      
def chatbot():
    
    knowladge_base: dict = load_knowladge_base('knowladge_base.json')
    print(knowladge_base)  
    
    while True:
        user_input: str = input("\nYou : ")
        if user_input.lower() == 'quit':
            print("Thank you for using me 💖")
            break
        best_matches: str = find_best_matches(user_input, [i["question"] for i in knowladge_base['question']])
        print(best_matches)
        
        if best_matches:
            answer: str = get_answer_for_question(best_matches, knowladge_base)
            print(f'Bot : {answer}')
        else:
            print("Bot : I don\'t understand. Can you teach me?")
            new_answer:str = input(" Type answer or type 'skip' to skip \n>>>>>> ")
            if new_answer != "skip":
                knowladge_base['question'].append({'question': user_input, 'answer':new_answer})
                save_knowladge_base('knowladge_base.json', knowladge_base)
                print("Thank you for teaching.")
        
if __name__ == '__main__':
    chatbot()
    