import unittest

from ..src.stack import Stack


class TestStack(unittest.TestCase):
    def setUp(self) -> None:
        self.stack = Stack()

    def test_push(self) -> None:
        self.assertEqual(len(self.stack.input_list), 0)

        self.stack.push(1)
        self.stack.push(2)
        self.assertEqual(len(self.stack.input_list), 2)

    def test_pop(self) -> None:
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)
        self.assertEqual(len(self.stack.input_list), 3)

        self.stack.pop()
        self.stack.pop()
        self.assertEqual(len(self.stack.input_list), 1)

    def test_get_top(self) -> None:
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)
        self.assertEqual(self.stack.get_top(), 3)

    def test_is_empty(self) -> None:
        self.stack.push(1)
        self.stack.push(2)
        self.assertFalse(self.stack.is_empty())

        self.stack.pop()
        self.stack.pop()
        self.assertTrue(self.stack.is_empty())
