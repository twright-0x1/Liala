import io
import unittest
from unittest.mock import patch
from liala.utils.helper_functions import get_menu_choice

class TestHelperFunctions(unittest.TestCase):
    # Use the patch decorator to simulate user input
    # The patched stdin object will return '2' when input() is called
    #
    @patch('sys.stdin', io.StringIO('2\n'))
    def test_get_menu_choice(self):
        # Define a list of menu options
        #
        choices = ["Option 1", "Option 2", "Option 3"]

        # Define the expected output from get_menu_choice() given the above user input
        #
        expected_output = 2

        # Use the patch function as a context manager to redirect print() output to a fake stdout object
        #
        with patch('sys.stdout', new=io.StringIO()) as fake_output:
            # Call the get_menu_choice() function with the list of menu options
            #
            choice = get_menu_choice(choices)

            # Verify that the output of get_menu_choice() matches the expected output
            #
            self.assertEqual(choice, expected_output)

            # Verify that the menu options were printed correctly
            #
            self.assertEqual(fake_output.getvalue(), "1. Option 1\n2. Option 2\n3. Option 3\nEnter your choice: ")

if __name__ == '__main__':
    unittest.main()
