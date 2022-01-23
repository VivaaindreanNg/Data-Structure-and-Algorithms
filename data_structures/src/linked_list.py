# Application: Polynomial calculation
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
    P(x) = 6x^3 + 10x^2 + 78\n
    Q(x) = 4x^2 + 2x^1

    P(x) + Q(x) = 6x^3 + 14x^2 + 2x^1 + 78
    """

    def __init__(self) -> None:
        """
        When initialized LL, the first node is initially points to None/null.
        """
        self.first_node = None

    def insert_first(self, node_data: dict) -> None:
        """
        Insert a node at the beginning of the list.

        Pseudocode:
        function insertFirst(Node node)
            if ll.firstNode is null:
                ll.firstNode := node
            else:
                temp := ll.firstNode
                ll.firstNode := node
                ll.firstNode.next := temp

        Time Complexity: O(1)
        """
        if ll.first_node is None:
            ll.first_node = Node(node_data)
        else:
            temp = ll.first_node
            ll.first_node = Node(node_data)
            ll.first_node.next = temp

    def insert(self, new_node_data: dict) -> None:
        """
        Insert a node one after the other within the list (while traversing).

        ```
        Pseudocode:
        function insert(Node newNode)
            if ll.firstNode is null:
                ll.firstNode := newNode
            else:
                currNode := ll.firstNode
                while currNode.next not null:
                    currNode := currNode.next

                if currNode.next is null:
                    currNode.next := newNode
        ```

        Time Complexity: O(n)
        """
        if ll.first_node is None:
            ll.first_node = Node(new_node_data)
        else:
            curr_node = self.first_node
            while curr_node.next is not None:
                curr_node = curr_node.next

            if curr_node.next is None:
                curr_node.next = Node(new_node_data)

    def delete_first(self) -> None:
        """
        Delete a node at the beginning of the list.

        ```
        Pseudocode:
        function removeBeginning(List list)
            if list.firstNode not null:
                list.firstNode := list.firstNode.next
        ```

        Time Complexity: O(1)
        """
        if self.first_node is not None:
            self.first_node = self.first_node.next

    def delete_by_node(self, deleted_node_data: dict) -> None:
        """
        TODO: Delete a given node based on given Node's data.

        ```
        Pseudocode:
        function remove(Node node)
            currNode := ll.firstNode
            while currNode not null:
                if currNode.data == node.data:
                    currNode := currNode.next
                    currNode.next := currNode.next.next
                    break
                else:
                    currNode := currNode.next
        ```

        Time Complexity: O(n)
        """
        pass

    def get_by(self, pos: int) -> Node:
        """
        Get a node based on position of node in the list.

        ```
        Pseudocode:
        counter := 0
        currNode := ll.firstNode
        while currNode != null:
            if counter != position:
                counter := counter + 1
                currNode := currNode.next
            else:
                return currNode
        ```

        Time Complexity: O(n)
        """
        counter = 0
        curr_node = self.first_node
        while curr_node is not None:
            if counter != pos:
                counter += 1
                curr_node = curr_node.next
            else:
                return curr_node

    def __str__(self) -> str:
        """
        Display all the nodes in Linked List.

        Traversal of a singly linked list is simple,
        beginning at the first node and following each next
        link until we come to the end.

        ```
        Pseudocode:
        currNode := ll.firstNode
        while currNode not null
            (do something with currNode.data)
            currNode := currNode.next
        ```

        Time Complexity: O(n)
        """

        output = ""
        curr_node = self.first_node

        while curr_node is not None:
            coeff = curr_node.data["coefficient"]
            var = curr_node.data["variable"]
            exp = curr_node.data["exponent"]
            output += f"{coeff}{var}^{exp} "

            if curr_node.next is not None:
                output += "+ "

            # If there's next (Node), move on to it.
            curr_node = curr_node.next

        return output


if __name__ == "__main__":
    node1_data = {"coefficient": 6, "variable": "x", "exponent": 3}
    node2_data = {"coefficient": 10, "variable": "x", "exponent": 2}
    node3_data = {"coefficient": 78, "variable": "", "exponent": 0}

    ll = LinkedList()
    ll.insert(node2_data)
    ll.insert(node3_data)
    ll.insert_first(node1_data)

    print(f"\nP(x): {ll}")

    print(f"Get by post {0}: {ll.get_by(0).data}")
    print(f"Get by post {2}: {ll.get_by(2).data}")

    ll.insert_first({"coefficient": 999, "variable": "xyz", "exponent": 999})
    print(f"\nAdded first node at P(x): {ll}")

    ll.delete_first()
    print(f"Deleted first node P(x): {ll}")

    data_to_delete = {"coefficient": 123, "variable": "xyz", "exponent": 123}
    ll.insert(data_to_delete)
    print(f"\nAdded new node at P(x): {ll}")

    ll.delete_by_node(data_to_delete)
    print(f"Deleted target node P(x): {ll}")
