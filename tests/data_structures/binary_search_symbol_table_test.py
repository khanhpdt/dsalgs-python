from src.data_structures.binary_search_symbol_table import BinarySearchSymbolTable
from tests.data_structures.ordered_symbol_table_test_common import OrderedSymbolTableTestCommon


class TestBinarySearchSymbolTable(OrderedSymbolTableTestCommon):

    def setup_method(self):
        super().setup_method()
        self.table = BinarySearchSymbolTable()
