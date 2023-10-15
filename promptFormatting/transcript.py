# Transcript class to handle different scripts
class Transcript:
    transcripts = {
        "short": {
            "English": """
                Coach: 'How do you feel about the situation?' 
                Client: 'I'm a bit overwhelmed.'
                ...< 100+ lines >...
            """
        },
        # Can add other formats and languages as required
    }

    @classmethod
    def get_transcript(cls, format_type, language):
        return cls.transcripts.get(format_type, {}).get(language, "Transcript not available")