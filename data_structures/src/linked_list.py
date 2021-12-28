# TODO: Application: Polynomial calculation
# https://www.javatpoint.com/application-of-linked-list


class Node:
    def __init__(self, coefficient: int, variable: str, exponent: int) -> None:
        """
        To initialize a single Node object
        """
        self.coefficient = coefficient
        self.variable = variable
        self.exponent = exponent
        self.next = None


class LinkedList:
    """
    Using LL to perform polynomial calculation. Consider:\n
    P(x) = 6x^3 + 10x^2\n
    Q(x) = 4x^2 + 2x^1

    P(x) + Q(x) = 6x^3 + 14x^2 + 2x^1
    """

    def __init__(self) -> None:
        """
        When initialized LL, the head is initially points to None/null
        """
        self.node = None
        self.head = None

    def insert(
        self, coefficient: int, variable: str, exponent: int, next: Node
    ) -> None:
        """
        TODO: Insert sequentially
        """
        self.node = Node(coefficient, variable, exponent)
        self.next = None

    def __str__(self) -> str:
        coeff = self.node.coefficient
        var = self.node.variable
        exp = self.node.exponent
        return f"{coeff}{var}^{exp}"


if __name__ == "__main__":
    ll = LinkedList()
    ll.insert(6, "x", 3, None)
    print(ll)
