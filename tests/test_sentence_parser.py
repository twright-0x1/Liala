import unittest
from liala.utils.sentence_parser import SentenceParser

class SentenceParserTest(unittest.TestCase):
    """
    Unit test class for testing the SentenceParser class.
    """

    def setUp(self):
        """
        Set up any necessary objects or configurations before each test case.
        """
        self.parser = SentenceParser()

    def test_parse_sentence(self):
        """
        Test the parse_sentence method of SentenceParser.
        """
        sentence = "The quick brown fox jumps over the lazy dog."
        expected_output = {
            "The": "DET",
            "quick": "ADJ",
            "brown": "ADJ",
            "fox": "NOUN",
            "jumps": "VERB",
            "over": "ADP",
            "the": "DET",
            "lazy": "ADJ",
            "dog": "NOUN",
            ".": "PUNCT"
        }
        result = self.parser.parse_sentence(sentence)
        self.assertEqual(result, expected_output)

if __name__ == "__main__":
    unittest.main()
