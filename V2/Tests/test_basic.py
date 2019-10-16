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

