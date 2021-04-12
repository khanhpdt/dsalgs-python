from src.data_structures.binary_search_tree_symbol_table import BinarySearchTreeSymbolTable
from tests.data_structures.ordered_symbol_table_test_common import OrderedSymbolTableTestCommon


class TestBinarySearchTreeSymbolTable(OrderedSymbolTableTestCommon):

    def setup_method(self):
        super().setup_method()
        self.table = BinarySearchTreeSymbolTable()
