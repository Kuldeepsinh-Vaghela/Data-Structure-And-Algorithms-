class Solution:
    def isHappy(self, n: int) -> bool:

        str_int = str(n)
        
        new_n = 0
        ref_set = ()
        while new_n != 1:
            sum_sq = 0
            for dgt in str_int:
                intv = int(dgt)
                sum_sq += intv**2
            str_int = str(sum_sq)
            new_n = sum_sq
            if new_n in ref_set:
                return False
            else:
                ref_set.add(new_n)
        return True
            