from utils.helper_functions import get_menu_choice
from utils.sentence_parser import SentenceParser
from flask import Flask, render_template, request

app = Flask(__name__)

# Define the menu items
menu_items = ["Item 1", "Item 2", "Item 3", "Item 4"]

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get the selected item from the form
        selected_item = request.form['menu']
        return render_template('index.html', menu_items=menu_items, selected_item=selected_item)
    else:
        return render_template('index.html', menu_items=menu_items, selected_item=None)

# create a SentenceParser object
parser = SentenceParser()

# sample sentence
sentence = "The quick, brown fox jumps over the lazy dog."

# parse the sentence and print the results
result = parser.parse_sentence(sentence)
print(result)

choices = ["Option 1", "Option 2", "Option 3"]

if __name__ == '__main__':
    app.run(debug=True)

    # No need to cause our test program to hang
    #
    if False:
        choice = get_menu_choice(choices)
        print(f"You chose option {choice}")
