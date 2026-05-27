import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from app import add

def test_add():
    assert add(2, 3) == 5