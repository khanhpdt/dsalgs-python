from src.common.comparable import Comparable
from src.common.utils import compare, eq


class KeyValue(Comparable):

    def __init__(self, key, value=None):
        self.key = key
        self.value = value

    def __repr__(self):
        return f"Key: ${self.key}, Value: ${str(self.value)}"

    def compare_to(self, other):
        return compare(self.key, other.key)

    def equals(self, other):
        return eq(self.key, other.key)


class Key(Comparable):

    def __init__(self, value):
        self.value = value

    def __repr__(self) -> str:
        return str(self.value)

    def compare_to(self, other):
        return compare(self.value, other.value)

    def equals(self, other):
        return eq(self.value, other.value)
