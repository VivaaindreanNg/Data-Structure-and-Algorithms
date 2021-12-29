# TODO: Application: Polynomial calculation
# https://www.javatpoint.com/application-of-linked-list


class Node:
    def __init__(self, node_data: dict) -> None:
        """
        To initialize a single Node object.

        Each Node object consists of 2 parts:
            1) Data.
            2) Link to the next node.
        """
        self.data = {}
        self.data["coefficient"] = node_data["coefficient"]
        self.data["variable"] = node_data["variable"]
        self.data["exponent"] = node_data["exponent"]
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

    def insert_first(self, node_data: dict) -> None:
        """
        TODO: Insert a node at the beginning of the list.

        Time Complexity: O(1)
        """
        self.node = Node(node_data)
        self.next = None

        # Links the head pointer to the newly-created first Node
        self.head = self.node

    def insert_after(self, node: Node, new_node_data: dict) -> None:
        """
        TODO: Insert a node right after given node.

        ```
        Pseudocode:
        function insertAfter(Node node, Node newNode)
            newNode.next := node.next
            node.next    := newNode
        ```

        Time Complexity: O(n)
        """
        pass

    def delete_first(self) -> None:
        """
        TODO: Delete a node at the beginning of the list.

        ```
        Pseudocode:
        function removeBeginning(List list)
            obsoleteNode := list.firstNode
            list.firstNode := list.firstNode.next // point past deleted node
            destroy obsoleteNode
        ```

        Time Complexity: O(1)
        """
        pass

    def delete(self) -> None:
        """
        TODO: Delete a given node.

        ```
        Pseudocode:
        function remove(Node node)
            while currNode not null:
                if currNode == node:
                    obsoleteNode := currNode.next
                    currNode.next := currNode.next.next
                    destroy obsoleteNode
                else:
                    currNode := currNode.next
        ```

        Time Complexity: O(n)
        """
        pass

    def get_by(self) -> Node:
        """
        TODO: Get a node based on a given key.

        Time Complexity: O(n)
        """
        pass

    def __str__(self) -> str:
        """
        TODO: Display all the nodes in Linked List.

        Traversal of a singly linked list is simple,
        beginning at the first node and following each next
        link until we come to the end.

        ```
        Pseudocode:
        while node not null
            (do something with node.data)
            node := node.next
        ```

        Time Complexity: O(n)
        """

        output = ""
        while self.node is not None:
            coeff = self.node.data["coefficient"]
            var = self.node.data["variable"]
            exp = self.node.data["exponent"]
            output += f"{coeff}{var}^{exp} "

            if self.node.next is not None:
                output += "+ "

            # If there's next (Node), move on to it.
            self.node = self.node.next

        return output


if __name__ == "__main__":
    ll = LinkedList()

    node1_data = {"coefficient": 6, "variable": "x", "exponent": 3}
    ll.insert_first(node1_data)
    print(ll)
