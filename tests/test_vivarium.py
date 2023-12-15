import unittest
from unittest.mock import patch
from io import StringIO
from liala.utils.vivarium import Vivarium

class TestVivarium(unittest.TestCase):
    def setUp(self):
        """ At the start of each test, create a new Vivarium object
            and kick off its threads
        """
        self.vivarium = Vivarium()
        # self.vivarium.start_threads()

    def tearDown(self):
        """ At the end of each test, stop the Vivarium object's
            threads
        """
        pass
        #self.vivarium.stop_threads()

    def test_write_to_egress_list(self):
        self.vivarium.write_to_egress_list("Test Data")
        self.assertEqual(len(self.vivarium.egress_list), 1)
        self.assertEqual(self.vivarium.egress_list[0], "Test Data")

    def test_read_ingress_list(self):
        self.vivarium.ingress_list = ["Data 1", "Data 2", "Data 3"]
        ingress_copy = self.vivarium.read_ingress_list()
        self.assertEqual(ingress_copy, ["Data 1", "Data 2", "Data 3"])

    @patch('builtins.input', side_effect=["Input 1", "Input 2"])
    def test_async_input(self, mock_input):
        result = self.vivarium.loop.run_until_complete(self.vivarium.async_input("Prompt: "))
        self.assertEqual(result, "Input 1")
        result = self.vivarium.loop.run_until_complete(self.vivarium.async_input("Prompt: "))
        self.assertEqual(result, "Input 2")

    @patch('sys.stdout', new_callable=StringIO)
    def test_async_print(self, mock_stdout):
        self.vivarium.loop.run_until_complete(self.vivarium.async_print("Test Output"))
        self.assertEqual(mock_stdout.getvalue().strip(), "Test Output")

if __name__ == '__main__':
    unittest.main()
