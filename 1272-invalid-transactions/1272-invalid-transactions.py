class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:

        invalid = []
        processed = []
        for transaction in transactions:
            if self.isinvalid(transaction, transactions):
                invalid.append(transaction)
        return invalid


    def isinvalid(self, transaction, transactions):

        name1, time1, amnt1, city1 = transaction.split(",")

        if int(amnt1) > 1000: return True

        for cur_trans in transactions:
            name2, time2, amnt2, city2 = cur_trans.split(",")

            if abs(int(time2) - int(time1)) <= 60 and name1 == name2 and city1 != city2:
                return True

        return False

            






"""
50 - 20 > 60
"""
        