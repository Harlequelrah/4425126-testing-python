from calculate.operators import Operators
import unittest


class testAdditionOperator(unittest.TestCase):

    def test_should_make_addition(self):
        sut = Operators()
        operation = "2+3"
        expected_value = 5.0
        self.assertEqual(sut.addition(operation),expected_value)

    def test_should_make_multiple_addition(self):
        sut = Operators()
        operation = "5.5 + 10 + 30 + 13.7"
        expected_value = 59.2
        self.assertEqual(sut.addition(operation),expected_value)

    def test_addition_should_return_none_with_wrong_operator(self):
        sut = Operators()
        operation = "2#5"
        expected_value = None
        self.assertEqual(sut.addition(operation),expected_value)


    def test_addition_should_return_none_with_wrong_operation(self):
        sut  = Operators()
        operation = "2+8*2"
        expected_value = None
        self.assertEqual(sut.addition(operation),expected_value)


    def test_addition_should_return_none_with_one_operand(self):
        sut = Operators()
        operation = "1+"
        expected_value = None
        self.assertEqual(sut.addition(operation),expected_value)

    def test_addition_should_return_none_with_no_operand(self):
        sut = Operators()
        operation = "+"
        expected_value = None
        self.assertEqual(sut.addition(operation),expected_value)


class MultiplicationOperator(unittest.TestCase):
    def test_should_make_multiplication(self):
        sut = Operators()
        operation = "2*3"
        expected_value = 6.0
        self.assertEqual(sut.multiplication(operation), expected_value)


    def test_should_make_multiple_multiplication(self):
        sut= Operators()
        operation="10*5*2"
        expected_value = 100.0
        assert sut.multiplication(operation)==expected_value

    def test_multiplication_should_return_none_with_wrong_operator(self):
        sut = Operators()
        operation = "2&3"
        expected_value = None
        self.assertEqual(sut.multiplication(operation), expected_value)

    def test_multiplication_should_return_none_with_wrong_operation(self):
        sut = Operators()
        operation = "2*4-1"
        expected_value = None
        self.assertEqual(sut.multiplication(operation), expected_value)


    def test_multiplication_should_return_none_with_one_operand(self):
        sut = Operators()
        operation = "2*"
        expected_value = None
        self.assertEqual(sut.multiplication(operation), expected_value)

    def test_multiplication_should_return_none_with_no_operand(self):
        sut = Operators()
        operation = "*"
        expected_value = None
        self.assertEqual(sut.multiplication(operation), expected_value)

class TestSubstractionOperator(unittest.TestCase):

    def test_should_make_multiple_substraction(self):
        sut = Operators()
        operation = "8-2-3"
        expected_value = 3.0
        self.assertEqual(sut.substraction(operation), expected_value)

    def test_should_make_substraction(self):
        sut = Operators()
        operation = "10-5"
        expected_value = 5.0
        self.assertEqual(sut.substraction(operation), expected_value)


    def test_substration_should_return_none_with_wrong_operator(self):
        sut = Operators()
        operation = "2%3"
        expected_value = None
        self.assertEqual(sut.substraction(operation), expected_value)


    def test_substraction_should_return_none_with_wrong_operation(self):
        sut = Operators()
        operation = "2-4+1"
        expected_value = None
        self.assertEqual(sut.substraction(operation), expected_value)


    def test_substraction_should_return_none_with_one_operand(self):
        sut = Operators()
        operation = "2-"
        expected_value = None
        self.assertEqual(sut.substraction(operation), expected_value)

    def test_substraction_should_return_none_with_no_operand(self):
        sut = Operators()
        operation = "-"
        expected_value = None
        self.assertEqual(sut.substraction(operation), expected_value)


class TestDivisionOperator(unittest.TestCase):
    def test_should_make_division(self):
        sut = Operators()
        operation = "10/2"
        expected_value = 5.0
        self.assertEqual(sut.division(operation), expected_value)

    def test_should_make_multiple_division(self):
        sut = Operators()
        operation = "100/2/5"
        expected_value = 10.0
        self.assertEqual(sut.division(operation), expected_value)

    def test_division_should_return_none_with_wrong_operator(self):
        sut = Operators()
        operation = "2%3"
        expected_value = None
        self.assertEqual(sut.division(operation), expected_value)


    def test_division_should_return_none_with_wrong_operation(self):
        sut = Operators()
        operation = "2/4+1"
        expected_value = None
        self.assertEqual(sut.division(operation), expected_value)


    def test_division_should_return_none_with_one_operand(self):
        sut = Operators()
        operation = "2/"
        expected_value = None
        self.assertEqual(sut.division(operation), expected_value)


    def test_division_should_return_none_with_no_operand(self):
        sut = Operators()
        operation = "/"
        expected_value = None
        self.assertEqual(sut.division(operation), expected_value)

    def test_division_should_return_none_with_zero_division(self):
        sut = Operators()
        operation = "2/0"
        expected_value = None
        self.assertEqual(sut.division(operation), expected_value)

