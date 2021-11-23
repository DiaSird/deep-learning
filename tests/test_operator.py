from src import __version__
import unittest
from src.utils.operator import add


class TestAdd(unittest.TestCase):

    def test_evalate(self):
        self.assertEqual("2", f"{add(1, 1)}")


def test_version():
    assert __version__ == '0.1.0'
