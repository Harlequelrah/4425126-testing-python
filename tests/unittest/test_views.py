from calculate.view import View
import unittest
from io import StringIO
import contextlib


class TestView(unittest.TestCase):

    def setUp(self):
        self.temp_stdout = StringIO()


    def test_shoud_print_menu(self):
        with contextlib.redirect_stdout(self.temp_stdout):
            View.print_menu()
        out = self.temp_stdout.getvalue()
        expected_output="\n=========== MENU ===========\n1 - Addition\n2 - Soustraction\n3 - Multiplication\n4 - Division\n5 - Quitter\n============================\n\n"

        self.assertEqual(out,expected_output)

    def test_should_print_end_message(self):
        with contextlib.redirect_stdout(self.temp_stdout):
            View.end_message()
        out = self.temp_stdout.getvalue()
        expected_output= "=========== GOOD-BYE ===========\n"
        self.assertEqual(out,expected_output)


    def test_should_print_result(self):
        operation= "2+3"
        result = 6.0
        with contextlib.redirect_stdout(self.temp_stdout):
            View.print_result(operation,result)
        out = self.temp_stdout.getvalue()
        expected_output = f"RESULTAT : {operation} = {result}\n"
        self.assertEqual(out,expected_output)

    def test_should_print_result_with_error(self):
        operation = "2*3"
        result = None
        with contextlib.redirect_stdout(self.temp_stdout):
            View.print_result(operation,result)
        out = self.temp_stdout.getvalue()
        expected_output = f"Votre operation est incorrect ! : {operation}\n"
        self.assertEqual(out,expected_output)
