from calculate.operators import Operators


def test_should_make_addition():
    sut = Operators()
    operation = "2+3"
    expected_value = 5.0
    assert sut.addition(operation)==expected_value

def test_should_make_multiple_addition():
    sut = Operators()
    operation = "5.5 + 10 + 30 + 13.7"
    expected_value = 59.2
    assert sut.addition(operation) == expected_value

def test_addition_should_return_none_with_wrong_operator():
    sut = Operators()
    operation = "2#5"
    expected_value = None
    assert sut.addition(operation) == expected_value


def test_addition_should_return_none_with_wrong_operation():
    sut  = Operators()
    operation = "2+8*2"
    expected_value = None
    assert sut.addition(operation) == expected_value


def test_addition_should_return_none_with_one_operand():
    sut = Operators()
    operation = "1+"
    expected_value = None
    assert sut.addition(operation) == expected_value

def test_addition_should_return_none_with_no_operand():
    sut = Operators()
    operation = "+"
    expected_value = None
    assert sut.addition(operation) == expected_value

def test_should_make_multiplication():
    sut = Operators()
    operation = "2*3"
    expected_value = 6.0
    assert sut.multiplication(operation) == expected_value


def test_should_make_multiple_multiplication():
    sut= Operators()
    operation="10*5*2"
    expected_value = 100.0
    assert sut.multiplication(operation)==expected_value

def test_multiplication_should_return_none_with_wrong_operator():
    sut = Operators()
    operation = "2&3"
    expected_value = None
    assert sut.multiplication(operation) == expected_value

def test_multiplication_should_return_none_with_wrong_operation():
    sut = Operators()
    operation = "2*4-1"
    expected_value = None
    assert sut.multiplication(operation) == expected_value


def test_multiplication_should_return_none_with_one_operand():
    sut = Operators()
    operation = "2*"
    expected_value = None
    assert sut.multiplication(operation) == expected_value

def test_multiplication_should_return_none_with_no_operand():
    sut = Operators()
    operation = "*"
    expected_value = None
    assert sut.multiplication(operation) == expected_value


def test_should_make_multiple_substraction():
    sut = Operators()
    operation = "8-2-3"
    expected_value = 3.0
    assert sut.substraction(operation) == expected_value

def test_should_make_substraction():
    sut = Operators()
    operation = "10-5"
    expected_value = 5.0
    assert sut.substraction(operation) == expected_value


def test_substration_should_return_none_with_wrong_operator():
    sut = Operators()
    operation = "2%3"
    expected_value = None
    assert sut.substraction(operation) == expected_value


def test_substraction_should_return_none_with_wrong_operation():
    sut = Operators()
    operation = "2-4+1"
    expected_value = None
    assert sut.substraction(operation) == expected_value


def test_substraction_should_return_none_with_one_operand():
    sut = Operators()
    operation = "2-"
    expected_value = None
    assert sut.substraction(operation) == expected_value

def test_substraction_should_return_none_with_no_operand():
    sut = Operators()
    operation = "-"
    expected_value = None
    assert sut.substraction(operation) == expected_value


def test_should_make_division():
    sut = Operators()
    operation = "10/2"
    expected_value = 5.0
    assert sut.division(operation) == expected_value

def test_should_make_multiple_division():
    sut = Operators()
    operation = "100/2/5"
    expected_value = 10.0
    assert sut.division(operation) == expected_value

def test_division_should_return_none_with_wrong_operator():
    sut = Operators()
    operation = "2%3"
    expected_value = None
    assert sut.division(operation) == expected_value


def test_division_should_return_none_with_wrong_operation():
    sut = Operators()
    operation = "2/4+1"
    expected_value = None
    assert sut.division(operation) == expected_value


def test_division_should_return_none_with_one_operand():
    sut = Operators()
    operation = "2/"
    expected_value = None
    assert sut.division(operation) == expected_value


def test_division_should_return_none_with_no_operand():
    sut = Operators()
    operation = "/"
    expected_value = None
    assert sut.division(operation) == expected_value

def test_division_should_return_none_with_zero_division():
    sut = Operators()
    operation = "2/0"
    expected_value = None
    assert sut.division(operation) == expected_value

