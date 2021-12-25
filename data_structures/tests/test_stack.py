import unittest

from ..src.stack import Stack


class TestStack(unittest.TestCase):
    def test_push(self) -> None:
        stack = Stack()
        self.assertEqual(len(stack.input_list), 0)

        stack.push(1)
        stack.push(2)

        self.assertEqual(len(stack.input_list), 2)

    def test_pop(self) -> None:
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)

        self.assertEqual(len(stack.input_list), 3)

        stack.pop()
        stack.pop()

        self.assertEqual(len(stack.input_list), 1)

    def test_get_top(self) -> None:
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)

        self.assertEqual(stack.get_top(), 3)

    def test_is_empty(self) -> None:
        stack = Stack()
        stack.push(1)
        stack.push(2)

        self.assertFalse(stack.is_empty())

        stack.pop()
        stack.pop()

        self.assertTrue(stack.is_empty())


if __name__ == "___main__":
    unittest.main()
