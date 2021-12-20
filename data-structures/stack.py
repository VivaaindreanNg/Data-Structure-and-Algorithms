from typing import Any


class Stack:
    def __init__(self, input_list: list) -> None:
        self.input_list = input_list

    def __str__(self) -> str:
        return str([i for i in self.input_list])

    def push(self, num: int) -> list:
        pass 

    def pop(self) -> Any:
        pass


if __name__ == '__main__':
    stack = Stack([1, 2, 3, 4])

    print(stack)