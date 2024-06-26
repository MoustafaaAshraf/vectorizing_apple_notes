import re


class TextPreprocessor:
    @staticmethod
    def preprocess(note):
        title, content = note
        # Remove HTML tags
        content = re.sub("<[^<]+?>", "", content)
        # Combine title and content
        full_text = f"{title}\n\n{content}"
        # Additional preprocessing steps can be added here
        return full_text
