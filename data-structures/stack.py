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


if __name__ == "__main__":
    stack = Stack([])

    print(f"Stack: {stack}")
    print(f"Check if stack is empty: {stack.is_empty()}\n")

    print(f"Push 1: {stack.push(1)}")
    print(f"Push 2: {stack.push(2)}")
    print(f"Push 3: {stack.push(3)}\n")

    print(f"Check if stack is empty: {stack.is_empty()}")

    print(f"Get top of stack: {stack.get_top()}")
    print(f"Pop: {stack.pop()}")
    print(f"Pop: {stack.pop()}")
    print(f"Pop: {stack.pop()}")
    print(f"Check if stack is empty: {stack.is_empty()}")
