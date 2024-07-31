import json

def check_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        try:
            json.load(file)
            print(f"{file_path} is valid JSON.")
        except json.JSONDecodeError as e:
            print(f"Error in {file_path}: {e}")

check_json('authors.json')
check_json('quotes.json')

