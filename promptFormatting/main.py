from client import Client
from promptHandler import PromptHandler

def main():
    client = Client("John", "Doe", "john.doe@example.com", "English")
    handler = PromptHandler(client)
    print(handler.get_formatted_prompt("short"))

if __name__ == "__main__":
    main()
