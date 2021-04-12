from src.data_structures.sequential_search_symbol_table import SequentialSearchSymbolTable
from tests.data_structures.ordered_symbol_table_test_common import OrderedSymbolTableTestCommon


class TestSequentialSearchSymbolTable(OrderedSymbolTableTestCommon):

    def setup_method(self):
        super().setup_method()
        self.table = SequentialSearchSymbolTable()
