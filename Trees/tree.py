from typing import Any


class Node:
    def __init__(self, data: Any = None, left=None, right=None):
        self.data: Any = data
        self.left: Node = left
        self.right: Node = right

    def add_left_child(self, child) -> None:
        self.left: Node = child

    def add_right_child(self, child) -> None:
        self.right: Node = child

    def del_left_child(self) -> None:
        self.left = None

    def del_right_child(self) -> None:
        self.right = None


class Tree:

    def __init__(self, root: Node = None) -> None:
        self.root: Tree.Node = root



