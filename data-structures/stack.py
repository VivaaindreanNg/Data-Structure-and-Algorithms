from typing import Any


class Stack:
    def __init__(self, input_list: list) -> None:
        self.input_list = input_list

    def __str__(self) -> str:
        return str([i for i in self.input_list])

    def push(self, element: Any) -> list:
        """
        Returns the list after pushing in an element.
        """
        pass 

    def pop(self) -> list:
        """
        Returns the list after popping off the top element.
        """
        pass

    def get_top(self) -> Any:
        """
        Returns top of the element within the stack without
        actually popping it off.
        """
        pass

    def is_empty(self) -> bool:
        return True if len(self.input_list) == 0 else False


if __name__ == '__main__':
    stack = Stack([])

    print(stack)

    print(f"Check if stack is empty: {stack.is_empty()}")