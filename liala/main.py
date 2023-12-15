from utils.helper_functions import *
from utils.sentence_parser import SentenceParser

# create a SentenceParser object
parser = SentenceParser()

# sample sentence
sentence = "The quick, brown fox jumps over the lazy dog."

# parse the sentence and print the results
result = parser.parse_sentence(sentence)
print(result)

choices = ["Option 1", "Option 2", "Option 3"]
choice = get_menu_choice(choices)
print(f"You chose option {choice}")
