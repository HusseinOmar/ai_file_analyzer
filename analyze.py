import os
from openai import OpenAI
from upload_file import build_store
from get_files import get_files


# Use this option if you configured the API in your OS environment
# for macos use this command export OPENAI_API_KEY="xxx"
# for windows use this command sets OPENAI_API_KEY="xxx"
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
# Use this option to paste your API key directly here
# client = OpenAI(api_key='')


def banner():
    print("============================================================")
    print("==================== Ai File Analyzer ======================")
    print("============================================================")
    print('''
    This script uses OpenAI API to analyze files in a local folder.
    The script uses two methods:
    ==> Method 1: Upload multiple files and analyze data in all files at once with single prompt
    ==> Method 2: Analyze each file separately with the same prompt.
    ========= PLEASE READ THE README FILE BEFORE USING THIS SCRIPT ========
    ''')


def start_prompt():
    print("===================================================")
    prompt = input(" ~~~~ Enter your prompt [type 'exit' to quit]: ")
    return prompt


def send_prompt(client, prompt, vector_store_id_list, previous_response_id=None):
    response = client.responses.create(
        model="gpt-4o",
        previous_response_id=previous_response_id,
        input=prompt,
        tools=[{
            "type": "file_search",
            "vector_store_ids": vector_store_id_list
        }]
    )
    print(response.output[1].content[0].text)
    return response


def choose_method():
    while True:
        print(" - Method 1: Upload multiple files and analyze data in all files at once with single prompt")
        print(" - Method 2: Analyze each file separately with the same prompt.")
        print('Please choose a method:')
        try:
            choice = int(input("==> Enter your choice (1 or 2): "))
            if choice in [1, 2]:
                break
            else:
                print("Invalid choice. Please enter 1 or 2.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    return choice


def method1():
    prompt = start_prompt()
    if prompt == "exit":
        exit()
    response = send_prompt(client, prompt, store_list_ids)
    while True:
        prompt_2 = start_prompt()
        if prompt_2 == "exit":
            exit()
        response = send_prompt(
            client, prompt_2, store_list_ids, response.id)


def method2():
    prompt = start_prompt()
    if prompt == "exit":
        exit()
    for item in buid_store:
        print(f'===> Processing {item["file"].filename}')
        process(prompt, item['store'].id)


def process(prompt, store_id):
    send_prompt(client, prompt, [store_id])


if __name__ == "__main__":
    banner()
    path, file_names = get_files()
    buid_store = build_store(client, path, file_names)
    store_list_ids = [item['store'].id for item in buid_store]
    choice = choose_method()
    while True:
        if choice == 1:
            method1()
        if choice == 2:
            method2()
