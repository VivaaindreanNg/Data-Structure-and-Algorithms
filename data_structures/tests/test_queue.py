import unittest

from ..src.queue import Queue


class TestQueue(unittest.TestCase):
    def setUp(self) -> None:
        self.queue = Queue()

    def test_enqueue(self) -> None:
        self.assertTrue(self.queue.is_empty())

        self.queue.enqueue("A")
        self.queue.enqueue("B")
        self.assertFalse(self.queue.is_empty())
        self.assertEqual(2, len(self.queue.input_list))

    def test_dequeue(self) -> None:
        self.queue.enqueue("X")
        self.queue.enqueue("Y")
        self.queue.enqueue("Z")
        self.assertEqual(3, len(self.queue.input_list))

        self.queue.dequeue()
        self.assertEqual(2, len(self.queue.input_list))
        self.assertEqual("Y", self.queue.input_list[0])
        self.assertEqual("Z", self.queue.input_list[1])

        self.queue.dequeue()
        self.assertEqual(1, len(self.queue.input_list))
        self.assertEqual("Z", self.queue.input_list[0])
