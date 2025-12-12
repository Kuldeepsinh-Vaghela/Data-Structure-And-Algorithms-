class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
            map_dic = {}
            cntr = 0
            while cntr <= len(s)-1:
                if s[cntr] not in map_dic and t[cntr] not in map_dic.values():
                    map_dic[s[cntr]] = t[cntr]
                else:
                    if s[cntr] in map_dic and map_dic[s[cntr]] != t[cntr]:
                        return False
                    if t[cntr] in map_dic.values() and s[cntr] not in map_dic:
                        return False
                cntr += 1
            return True



        