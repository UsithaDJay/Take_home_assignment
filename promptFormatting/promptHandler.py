from transcript import Transcript

# PromptHandler class to combine and generate the final formatted prompt
class PromptHandler:
    def __init__(self, client):
        self.client = client

    def set_client_details(self, first_name, last_name, email, language):
        self.client.first_name = first_name
        self.client.last_name = last_name
        self.client.email = email
        self.client.language = language

    def get_formatted_prompt(self, format_type):
        prompt_template = f"""
        You're an ICF MCC certified coach, responsible for training individuals to meet international coaching standards.

        Following are your client details:
        First Name: {self.client.first_name}
        Last Name: {self.client.last_name}
        Email: {self.client.email}
        Preferred Language: {self.client.language}

        Following is a sample script that explains how coaching should be carried out.
        Format: {format_type}
        Script:
        {Transcript.get_transcript(format_type, self.client.language)}

        Please follow the instructions carefully and ensure each session is fruitful.
        """
        return prompt_template