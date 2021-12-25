from typing import Any


class Stack:
    def __init__(self) -> None:
        self.input_list = []

    def push(self, element: Any) -> list:
        """
        Returns the list after pushing in an element.
        """
        self.input_list.append(element)
        return str(self.input_list)

    def pop(self) -> list:
        """
        Returns the list after popping off the top element.
        """
        tmp = self.input_list[:-1]
        self.input_list = tmp
        return str(self.input_list)

    def get_top(self) -> Any:
        """
        Returns top of the element within the stack without
        actually popping it off.
        """
        return self.input_list[-1]

    def is_empty(self) -> bool:
        return True if len(self.input_list) == 0 else False
