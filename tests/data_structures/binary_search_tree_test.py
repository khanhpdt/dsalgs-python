import random

from src.data_structures.binary_search_tree import BinarySearchTree, Node


class TestBinaryTreeNode:

    def test_compare(self):
        assert Node(1, 1).compare_to(Node(2, 2)) < 0
        assert Node(1, 1).compare_to(Node(1, 2)) == 0
        assert Node(1, 1).compare_to(Node(0, 2)) > 0

    def test_equals(self):
        assert Node(1, 1).equals(Node(1, 2))
        assert not Node(1, 1).equals(Node(2, 2))


class TestBinarySearchTree:

    def setup_method(self):
        self.tree = BinarySearchTree()
        self.default_keys = []

    def test_put_keep_binary_search_tree_property(self):
        keys = list(range(10))
        random.shuffle(keys)
        for key in keys:
            self.tree.put(key, key * 100)

        assert self.tree.size() == len(keys)
        assert self.tree.satisfy_binary_search_tree_property()

    def test_put_set_correct_node_counts(self):
        self.build_default_tree()

        node_counts = [8, 6, 1, 2, 3, 1, 2, 1]
        for i in range(len(self.default_keys)):
            assert self.tree.get(self.default_keys[i]).node_count == node_counts[i]

    def test_put_replace_existing_value(self):
        self.build_default_tree()

        size_before = self.tree.size()

        keys = self.default_keys.copy()
        random.shuffle(keys)
        for key in keys:
            new_value = 10000 + key
            self.tree.put(key, new_value)

            assert self.tree.get(key).value == new_value
            assert self.tree.size() == size_before

    def build_default_tree(self):
        self.default_keys = [157, 120, 168, 100, 140, 110, 130, 135]
        for key in self.default_keys:
            self.tree.put(key)
        assert self.tree.size() == 8

    def test_put_get_intermixed(self):
        self.tree.put(1, 100)
        assert self.tree.get(1).value == 100

        self.tree.put(2, 200)
        assert self.tree.get(2).value == 200

    def test_get_from_empty_tree(self):
        assert self.tree.is_empty()
        assert self.tree.get(1) is None

    def test_get_not_existing_key(self):
        self.tree.put(1, 100)
        self.tree.put(2, 200)
        assert self.tree.get(3) is None

    def test_in_order_traversal(self):
        self.build_default_tree()
        nodes = self.tree.in_order_traversal()

        assert len(nodes) == self.tree.size()

        expected_keys = [100, 110, 120, 130, 135, 140, 157, 168]
        for i in range(len(nodes)):
            assert nodes[i].key == expected_keys[i]

    def test_pre_order_traversal(self):
        self.build_default_tree()
        nodes = self.tree.pre_order_traversal()

        assert len(nodes) == self.tree.size()

        expected_keys = [157, 120, 100, 110, 140, 130, 135, 168]
        for i in range(len(nodes)):
            assert nodes[i].key == expected_keys[i]

    def test_post_order_traversal(self):
        self.build_default_tree()
        nodes = self.tree.post_order_traversal()

        assert len(nodes) == self.tree.size()

        expected_keys = [110, 100, 135, 130, 140, 120, 168, 157]
        for i in range(len(nodes)):
            assert nodes[i].key == expected_keys[i]

    def test_delete_non_existing_node(self):
        self.build_default_tree()
        size_before = self.tree.size()

        self.tree.delete(11111)

        assert self.tree.size() == size_before

    def test_delete_node_without_child(self):
        self.build_default_tree()

        deleted_key = 135
        parent_key = 130

        assert self.tree.get(parent_key).right.key == deleted_key

        self.tree.delete(deleted_key)

        assert self.tree.get(parent_key).right is None

    def test_delete_node_with_only_one_left_child(self):
        self.build_default_tree()

        deleted_key = 140
        parent_key = 120
        left_child_key = 130

        assert self.tree.get(parent_key).right.key == deleted_key

        self.tree.delete(deleted_key)

        assert self.tree.get(parent_key).right.key == left_child_key

    def test_delete_node_with_only_one_right_child(self):
        self.build_default_tree()

        deleted_key = 130
        parent_key = 140
        right_child_key = 135

        assert self.tree.get(parent_key).left.key == deleted_key

        self.tree.delete(deleted_key)

        assert self.tree.get(parent_key).left.key == right_child_key

    def test_delete_node_with_two_children_and_successor_has_no_child(self):
        self.build_default_tree()
        self.tree.put(90)
        self.tree.put(105)

        deleted_key = 100
        parent_key = 120
        right_child_of_deleted_key = 110
        left_child_of_deleted_key = 90
        successor_key = 105
        parent_of_successor_key = 110

        assert self.tree.get(parent_key).left.key == deleted_key
        assert self.tree.get(parent_of_successor_key).left.key == successor_key

        self.tree.delete(deleted_key)

        assert self.tree.get(parent_key).left.key == successor_key
        assert self.tree.get(successor_key).left.key == left_child_of_deleted_key
        assert self.tree.get(successor_key).right.key == right_child_of_deleted_key

        assert self.tree.get(parent_of_successor_key).left is None

    def test_delete_node_with_two_children_and_successor_has_right_child(self):
        self.build_default_tree()

        deleted_key = 120
        parent_key = 157
        right_child_of_deleted_key = 140
        left_child_of_deleted_key = 100
        successor_key = 130
        right_child_of_successor = 135
        parent_of_successor_key = 140

        assert self.tree.get(parent_key).left.key == deleted_key
        assert self.tree.get(parent_of_successor_key).left.key == successor_key

        self.tree.delete(deleted_key)

        assert self.tree.get(parent_key).left.key == successor_key
        assert self.tree.get(successor_key).left.key == left_child_of_deleted_key
        assert self.tree.get(successor_key).right.key == right_child_of_deleted_key

        assert self.tree.get(parent_of_successor_key).left.key == right_child_of_successor

    def test_delete_maintain_node_count(self):
        self.build_default_tree()

        self.tree.delete(120)

        keys = [157, 130, 168, 100, 140, 110, 135]
        node_counts = [7, 5, 1, 2, 2, 1, 1]
        for i in range(len(keys)):
            assert self.tree.get(keys[i]).node_count == node_counts[i]

    def test_delete_root(self):
        self.build_default_tree()

        self.tree.delete(157)

        nodes = self.tree.pre_order_traversal()
        assert nodes[0].key == 168

    def test_delete_many(self):
        # 10 test cases
        for i in range(10):
            keys = list(range(100))
            random.shuffle(keys)
            self.tree = BinarySearchTree()
            for key in keys:
                self.tree.put(key)

            # delete random 20 keys from the inserted 100 keys
            deleted_keys = random.sample(keys, 20)
            for deleted_key in deleted_keys:
                self.tree.delete(deleted_key)

            assert self.tree.size() == 80
            assert self.tree.satisfy_binary_search_tree_property()

    def test_delete_the_only_node(self):
        self.tree.put(1)
        self.tree.delete(1)
        assert self.tree.is_empty()
