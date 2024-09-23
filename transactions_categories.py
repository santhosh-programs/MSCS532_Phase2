from typing import List
from collections import defaultdict
from transaction import *
from category import *


class TransactionsAndCategories:
    def __init__(self, transactions: List[Transaction], categories: List[Category]):
        self.transactions: dict[int, Transaction] = {}
        self.categories: dict[int, Category] = {}
        self.init(transactions, categories)

    def init(self, transactions: List[Transaction], categories: List[Category]):
        for tran in transactions:
            if tran.id in self.transactions:
                raise Exception(
                    'Transaction provided with same id, make sure all ids are unique')
            else:
                self.transactions[tran.id] = tran

        for cat in categories:
            if cat.id in self.categories:
                raise Exception(
                    'Category provided with same id, make sure all ids are unique')
            else:
                self.categories[cat.id] = cat
