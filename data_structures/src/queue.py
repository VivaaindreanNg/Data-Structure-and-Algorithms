from typing import Any


class Queue:
    def __init__(self) -> None:
        self.input_list = []

    def enqueue(self, element: Any) -> list:
        self.input_list.append(element)
        return self.input_list

    def dequeue(self) -> list:
        self.input_list = self.input_list[1:]
        return self.input_list

    def is_empty(self) -> bool:
        return True if len(self.input_list) == 0 else False
