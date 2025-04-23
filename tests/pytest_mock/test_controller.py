from calculate.controller import Controller
from calculate import view
from calculate.operators import Operators
from calculate import operators
def test_quit_without_infinite_loop(mocker):
    sut = Controller()
    mocker.patch('calculate.view.View.get_user_input', return_value="5")
    assert sut._is_quit(view.View.get_user_input("Entrez votre choix")) == False


def test_addition(mocker):
    sut = Controller()
    expected_value= 10.0
    mock=mocker.patch('calculate.view.View.get_user_input')
    mock.side_effect=["1","5+5","5"]
    mocker.patch('calculate.operators.Operators.addition',return_value=expected_value)
    mocker.patch('calculate.view.View.continue_message')
    sut.run()
    assert sut.result==expected_value

def test_substraction(mocker):
    sut = Controller()
    expected_value = 2.0
    mock = mocker.patch('calculate.view.View.get_user_input')
    mock.side_effect = ["2","5-3","5"]
    mock.patch('calculate.operators.Operators.substraction',return_value=expected_value)
    mocker.patch('calculate.view.View.continue_message')
    sut.run()
    assert sut.result == expected_value


def test_multiplication(mocker):
    sut = Controller()
    expected_value = 36.0
    mock = mocker.patch('calculate.view.View.get_user_input')
    mock.side_effect= ["3","6*6","5"]
    mocker.patch('calculate.operators.Operators.multiplication',return_value=expected_value)
    mocker.patch('calculate.view.View.continue_message')
    sut.run()
    assert sut.result == expected_value

def test_division(mocker):
    sut = Controller()
    expected_value = 7.0
    mock = mocker.patch('calculate.view.View.get_user_input')
    mock.side_effect= ["4","56/8","5"]
    mocker.patch('calculate.operators.Operators.division',return_value=expected_value)
    mocker.patch('calculate.view.View.continue_message')
    sut.run()
    assert sut.result == expected_value
