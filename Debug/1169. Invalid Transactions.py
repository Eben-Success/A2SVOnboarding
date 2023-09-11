"""
A transaction is possibly invalid if:

the amount exceeds $1000, or;
if it occurs within (and including) 60 minutes of another transaction with the same name in a different city.
You are given an array of strings transaction where transactions[i] consists of comma-separated values representing the name, time (in minutes), amount, and city of the transaction.

Return a list of transactions that are possibly invalid. You may return the answer in any order.

 

Example 1:

Input: transactions = ["alice,20,800,mtv","alice,50,100,beijing"]
Output: ["alice,20,800,mtv","alice,50,100,beijing"]
Explanation: The first transaction is invalid because the second transaction occurs within a difference of 60 minutes, have the same name and is in a different city. Similarly the second one is invalid too.
Example 2:

Input: transactions = ["alice,20,800,mtv","alice,50,1200,mtv"]
Output: ["alice,50,1200,mtv"]
Example 3:

Input: transactions = ["alice,20,800,mtv","bob,50,1200,mtv"]
Output: ["bob,50,1200,mtv"]
 

Constraints:

transactions.length <= 1000
Each transactions[i] takes the form "{name},{time},{amount},{city}"
Each {name} and {city} consist of lowercase English letters, and have lengths between 1 and 10.
Each {time} consist of digits, and represent an integer between 0 and 1000.
Each {amount} consist of digits, and represent an integer between 0 and 2000.
"""

"""
time of two transaction <= 60mins
same name
different city
"""

from typing import List

class Transaction:
    def validTransaction(self, transactions: List[str]) -> List[str]:
        """
        input: accepts transactions
        output: process transactions based on specific conditions.
        """
        invalid_transactions = []
        valid_transactions = []
        
        for transaction in transactions:
            if self.is_valid(transactions, transaction):
                valid_transactions.append(transaction)
            else:
                invalid_transactions.append(transaction)
            
        return invalid_transactions
    
    def is_valid(self, transactions: List[str], prev_transaction: List[str]) -> bool:
        """
        input: accept prev transaction and current transactions.
        output: return a boolean based on specified conditions
        """
        
        # unpack the List[str]
        prev_name, prev_time, prev_amount, prev_city = prev_transaction.split()
        
        #condition 1: if cur_amount > 1000
        
        if int(prev_amount) > 1000:
            return False
        
        # Iterate over the current transactions
        for transaction in transactions:
            cur_name, cur_time, cur_amount, cur_city = transaction.split()
            
            #condition 2
            if abs(int(prev_time) - int(cur_time)) <= 60 and prev_name == cur_name and cur_city != prev_city:
                return False
        
        