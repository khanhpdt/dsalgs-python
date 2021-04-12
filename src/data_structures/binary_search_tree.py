from typing import Optional, List

from src.common.comparable import Comparable
from src.common.utils import gt_or_eq, lt_or_eq, compare, eq, lt, gt


class Node(Comparable):

    def __init__(self, key, value) -> None:
        self.key = key
        self.value = value
        # the total number of nodes (including this node) in the tree rooted at this node
        self.node_count = 1
        self.left: Node = None
        self.right: Node = None

    def compare_to(self, other):
        return compare(self.key, other.key)

    def equals(self, other):
        return eq(self.key, other.key)


class BinarySearchTree:

    def __init__(self):
        self._root: Node = None

    @property
    def root(self):
        return self._root

    def put(self, key, value=None) -> None:
        self._root = self._put(Node(key, value), self._root)

    def _put(self, new_node: Node, position: Node):
        if position is None:
            return new_node

        if eq(new_node.key, position.key):
            position.value = new_node.value
            return position

        if lt(new_node.key, position.key):
            position.left = self._put(new_node, position.left)
        else:
            position.right = self._put(new_node, position.right)

        position.node_count = (position.left.node_count if position.left is not None else 0) \
            + (position.right.node_count if position.right is not None else 0) \
            + 1

        return position

    def size(self):
        return self._root.node_count if self._root is not None else 0

    def is_empty(self):
        return self._root is None

    def get(self, key) -> Optional[Node]:
        if self.is_empty():
            return None

        current = self._root
        while current is not None:
            if eq(current.key, key):
                return current
            current = current.left if lt(key, current.key) else current.right
        return None

    def delete(self, key):
        # no node with the given key exists in the tree
        if self.get(key) is None:
            return

        parent = None
        is_node_left_child = False
        node = self._root
        while node is not None:
            if eq(key, node.key):
                break

            parent = node
            # this is why we want to make sure that the key must exist in the tree.
            parent.node_count = parent.node_count - 1

            if lt(key, node.key):
                node = node.left
                is_node_left_child = True
            else:
                node = node.right
                is_node_left_child = False

        successor, parent_of_successor = self._find_successor_and_parent(node)

        if successor is None:  # the deleted node has no right subtree
            if parent is None:  # the deleted node is the current root
                self._root = node.left
            elif is_node_left_child:
                parent.left = node.left
            else:
                parent.right = node.left
        else:
            # replace successor by its right child
            # Note: Because the successor is the left-most node, it can either have no child or only one right child,
            # and it must be its parent's left child.
            if parent_of_successor is not None:
                parent_of_successor.left = successor.right

            # replace the deleted node by its successor
            if parent is None:  # the deleted node is the current root
                self._root = successor
            elif is_node_left_child:
                parent.left = successor
            else:
                parent.right = successor

            successor.left = node.left
            # the successor is the node's right child if it is the only node in the node's right subtree,
            # and we want to avoid cycle here.
            if not eq(successor, node.right):
                successor.right = node.right

        if successor is not None:
            successor.node_count = node.node_count - 1
        if parent_of_successor is not None:
            parent_of_successor.node_count = parent_of_successor.node_count - 1

    @staticmethod
    def _find_successor_and_parent(node):
        if node.right is None:
            return None, None

        parent = None
        current = node.right
        while current is not None:
            if current.left is None:
                return current, parent
            parent = current
            current = current.left

    def in_order_traversal(self) -> List[Node]:
        return self._in_order_traversal(self._root)

    def _in_order_traversal(self, node: Node) -> List[Node]:
        if node is None:
            return []
        return self._in_order_traversal(node.left) + [node] + self._in_order_traversal(node.right)

    def pre_order_traversal(self):
        return self._pre_order_traversal(self._root)

    def _pre_order_traversal(self, node: Node) -> List[Node]:
        if node is None:
            return []
        return [node] + self._pre_order_traversal(node.left) + self._pre_order_traversal(node.right)

    def post_order_traversal(self):
        return self._post_order_traversal(self._root)

    def _post_order_traversal(self, node: Node) -> List[Node]:
        if node is None:
            return []
        return self._post_order_traversal(node.left) + self._post_order_traversal(node.right) + [node]

    def satisfy_binary_search_tree_property(self):
        return self._satisfy_binary_search_tree_property(self._root)

    def _satisfy_binary_search_tree_property(self, node: Node):
        if node is None:
            return True

        node_satisfy = (node.left is None or gt_or_eq(node, node.left)) \
            and (node.right is None or lt_or_eq(node, node.right))

        return node_satisfy \
            and self._satisfy_binary_search_tree_property(node.left) \
            and self._satisfy_binary_search_tree_property(node.right)

    def min(self) -> Optional[Node]:
        if self.is_empty():
            return None

        current = self._root
        while current.left is not None:
            current = current.left
        return current

    def max(self) -> Optional[Node]:
        if self.is_empty():
            return None

        current = self._root
        while current.right is not None:
            current = current.right
        return current

    def floor(self, key):
        return self._floor(key, self._root)

    def _floor(self, key, node):
        if node is None:
            return None

        if eq(key, node.key):
            return node

        if lt(key, node.key):
            return self._floor(key, node.left)

        right_subtree_floor = self._floor(key, node.right)
        return right_subtree_floor if right_subtree_floor is not None else node

    def ceiling(self, key):
        return self._ceiling(key, self._root)

    def _ceiling(self, key, node):
        if node is None:
            return None

        if eq(key, node.key):
            return node

        if gt(key, node.key):
            return self._ceiling(key, node.right)

        left_subtree_ceiling = self._ceiling(key, node.left)
        return left_subtree_ceiling if left_subtree_ceiling is not None else node

    def rank(self, key):
        return self._rank(key, self._root)

    def _rank(self, key, node):
        if node is None:
            return 0
        left_child_count = node.left.node_count if node.left is not None else 0
        if eq(key, node.key):
            return left_child_count
        if gt(key, node.key):
            return 1 + left_child_count + self._rank(key, node.right)
        return self._rank(key, node.left)

    def select(self, rank):
        return self._select(rank, self._root)

    def _select(self, rank, node):
        if node is None:
            return None

        rank_of_node = node.left.node_count if node.left is not None else 0
        if rank_of_node == rank:
            return node
        if rank_of_node < rank:
            return self._select(rank - (rank_of_node + 1), node.right)
        return self._select(rank, node.left)

    def range(self, low, high):
        return self._range(self._root, low, high)

    def _range(self, node, low, high):
        if node is None:
            return []

        node_satisfy = (low is None or gt_or_eq(node.key, low)) \
            and (high is None or lt_or_eq(node.key, high))
        result = [node] if node_satisfy else []

        if low is not None and lt(node.key, low):
            return result + self._range(node.right, low, high)
        if high is not None and gt(node.key, high):
            return result + self._range(node.left, low, high)
        return result + self._range(node.left, low, high) + self._range(node.right, low, high)
