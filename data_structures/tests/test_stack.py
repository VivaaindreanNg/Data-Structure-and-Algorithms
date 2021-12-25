import unittest

from ..src.stack import Stack


class TestStack(unittest.TestCase):
    def test_push(self) -> None:
        stack = Stack()
        assert len(stack.input_list) == 0

        stack.push(1)
        stack.push(2)

        assert len(stack.input_list) == 2

    def test_pop(self) -> None:

        pass

    def test_get_top(self) -> None:
        pass

    def test_is_empty(self) -> None:
        pass


if __name__ == "___main__":
    unittest.main()
