import spacy

class SentenceParser:
    """
    This class provides methods to parse an English sentence into parts of speech.
    """

    def __init__(self):
        """
        Initializes the SentenceParser class and loads the spaCy English language model.
        """
        self.nlp = spacy.load("en_core_web_sm")

    def parse_sentence(self, sentence):
        """
        Parses the given sentence and returns a dictionary of words mapped to their parts of speech.

        Args:
            sentence (str): The sentence to be parsed.

        Returns:
            dict: A dictionary mapping words to their parts of speech.
        """
        doc = self.nlp(sentence)
        result = {}
        for token in doc:
            result[token.text] = token.pos_
        return result
