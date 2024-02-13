class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        fives = 0
        tens = 0

        for bill in bills:
            if bill == 5:
                fives += 5
            elif bill == 10:
                if not fives:
                    return False
                fives -= 5
                tens += 10
            elif bill == 20:
                if not fives:
                    return False
                fives -= 5
                if tens:
                    tens -= 10
                else:
                    if fives - 10 < 0:
                        return False
                    else:
                        fives -= 10

        return True
        
