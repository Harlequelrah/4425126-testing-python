from calculate.view import View

def test_shoud_print_menu(capsys):
    View.print_menu()
    out,err = capsys.readouterr()
    expected_output="\n=========== MENU ===========\n1 - Addition\n2 - Soustraction\n3 - Multiplication\n4 - Division\n5 - Quitter\n============================\n\n"

    assert out == expected_output

def test_should_print_end_message(capsys):
    View.end_message()
    out,err = capsys.readouterr()
    expected_output= "=========== GOOD-BYE ===========\n"
    assert out == expected_output


def test_should_print_result(capsys):
    operation= "2+3"
    result = 6.0
    View.print_result(operation,result)
    out,err = capsys.readouterr()
    expected_output = f"RESULTAT : {operation} = {result}\n"
    assert out == expected_output

def test_should_print_result_with_error(capsys):
    operation = "2*3"
    result = None
    View.print_result(operation,result)
    out,err = capsys.readouterr()
    expected_value = f"Votre operation est incorrect ! : {operation}\n"
    assert out == expected_value
