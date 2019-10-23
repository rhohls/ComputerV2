import sys
import pytest
from V2.TheCompute.mycomputer import Computer


@pytest.fixture(scope='function')
def computer():
    computer = Computer()
    return computer


def test_basic(capsys, computer):
    computer.handle_input("varA = 2")
    assert capsys.readouterr().out == "2\n"
    computer.handle_input("varB = 2.546")
    assert capsys.readouterr().out == "2.546\n"
    computer.handle_input("varC = -3.1")
    assert capsys.readouterr().out == "-3.1\n"

    computer.handle_input("varA")
    assert capsys.readouterr().out == "2\n"
    computer.handle_input("varB")
    assert capsys.readouterr().out == "2.546\n"
    computer.handle_input("varC")
    assert capsys.readouterr().out == "-3.1\n"


def test_using_variables(capsys, computer):
    computer.handle_input("x = 2")
    assert capsys.readouterr().out == "2\n"
    computer.handle_input("y = x")
    assert capsys.readouterr().out == "2\n"
    computer.handle_input("y = 7")
    assert capsys.readouterr().out == "7\n"

    computer.handle_input("varA = 2")
    assert capsys.readouterr().out == "2\n"
    computer.handle_input("varB= 2 * (4 + varA + 3)") #varB= 2 * (4 + 2 + 3)
    assert capsys.readouterr().out == "18\n"
    computer.handle_input("varC =2 * varB")
    assert capsys.readouterr().out == "36\n"
    computer.handle_input("varD = 2 *(2 + 4 *varC -4 /3)")
    assert capsys.readouterr().out == "289.33333\n"


def test_imaginary(capsys, computer):
    computer.handle_input("varA = 2*i + 3")
    assert capsys.readouterr().out == "3 + 2i\n"
    computer.handle_input("-4i - 4")
    assert capsys.readouterr().out == "-4 - 4i\n"
    computer.handle_input("y = 2 * i - 4")
    assert capsys.readouterr().out == "-4 + 2i\n"


def test_matrix(capsys, computer):
    computer.handle_input("varA = [[2,3];[4,3]]")
    assert capsys.readouterr().out == "[ 2 , 3 ]\n[ 4 , 3 ]\n"
    computer.handle_input("varB=[[3,4]]")
    assert capsys.readouterr().out == "[ 3 , 4 ]\n"
    computer.handle_input("matA = [[1,2];[3,2];[3,4]]")
    assert capsys.readouterr().out == "[ 1 , 2 ]\n[ 3 , 2 ]\n[ 3 , 4 ]\n"
    computer.handle_input("matB= [[1,2]]")
    assert capsys.readouterr().out == "[ 1 , 2 ]\n"


def test_functions(capsys, computer):
    computer.handle_input("funA(x) = 2*x^5 + 4x^2 - 5*x + 4")
    assert capsys.readouterr().out == "2 * x^5 + 4 * x^2 - 5*x + 4\n"
    computer.handle_input("funB(y) = 43 * y / (4 % 2 * y)")
    assert capsys.readouterr().out == "43 * y / (4 % 2 * y)\n"
    computer.handle_input("funC(z) = -2 * z - 5")
    assert capsys.readouterr().out == "-2 * z - 5\n"

    computer.handle_input("funA(b) = 2*b+b")
    assert capsys.readouterr().out == "2 * b + b\n"
    computer.handle_input("funB(a) =2 * a")
    assert capsys.readouterr().out == "2 * a\n"
    computer.handle_input("funC(y) =2* y + 4 -2 * 4+9/3")
    assert capsys.readouterr().out == "2 * y + 4 - 8 + 0.333333...\n"
    computer.handle_input("funD(x) = 2 *x")
    assert capsys.readouterr().out == "2 * x\n"


def test_using_functions(capsys, computer):
    computer.handle_input("varA = 2 + 4 *2 - 5 %4 + 2 * (4 + 5)")
    assert capsys.readouterr().out == "27\n"
    computer.handle_input("varB = 2 * varA - 5 %4")
    assert capsys.readouterr().out == "53\n"
    computer.handle_input("funA(x) = varA + varB * 4 - 1 / 2 + x")
    assert capsys.readouterr().out == "238.5 + x\n"
    computer.handle_input("varC = 2 * varA - varB")
    assert capsys.readouterr().out == "1\n"
    computer.handle_input("varD = funA(varC)")
    assert capsys.readouterr().out == "239.5\n"


def test_basic_evaluation(capsys, computer):
    computer.handle_input("a = 2 * 4 + 4")
    assert capsys.readouterr().out == "12\n"
    computer.handle_input("a + 2 = ?")
    assert capsys.readouterr().out == "14\n"


def test_function_evaluation(capsys, computer):
    computer.handle_input("funA(x) = 2 * 4 + x")
    assert capsys.readouterr().out == "8 + x\n"
    computer.handle_input("funB(x) = 4 - 5 + (x + 2)^2 - 4")
    assert capsys.readouterr().out == "(x + 2)^2 - 5\n"
    computer.handle_input("funC(x) = 4x + 5 - 2")
    assert capsys.readouterr().out == "4 * x + 3\n"

    computer.handle_input("funA(2) + funB(4) = ?")
    assert capsys.readouterr().out == "41\n"
    computer.handle_input("funC(3) = ?")
    assert capsys.readouterr().out == "15\n"


def test_ploynomial(capsys, computer):
    computer.handle_input("funA(x) = x^2 + 2x + 1")
    assert capsys.readouterr().out == "x^2 + 2x + 1\n"
    computer.handle_input("y = 0")
    assert capsys.readouterr().out == "0\n"
    computer.handle_input("funA(x) = y ?")
    assert capsys.readouterr().out == "x^2 + 2x + 1 = 0\nA solution on R :\n-1\n"

#
def test_custom(capsys, computer):
    computer.handle_input("y=2")
    assert capsys.readouterr().out == "2\n"
    computer.handle_input("a = 2* y + 4 -2 * 4+9/3 + 2y")
    assert capsys.readouterr().out == "7\n"