class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # if len(s) != len(t):
        #     return False
        # else:
        #     map_dic = {}
        #     cntr = 0
        #     while cntr <= len(s)-1:
        #         if s[cntr] not in map_dic and t[cntr] not in map_dic.values():
        #             map_dic[s[cntr]] = t[cntr]
        #         else:
        #             if s[cntr] in map_dic and map_dic[s[cntr]] != t[cntr]:
        #                 return False
        #             if t[cntr] in map_dic.values() and s[cntr] not in map_dic:
        #                 return False
        #         cntr += 1
        #     return True

        if len(s) != len(t):
            return False
        else:
            map_s_to_t = {}
            map_t_to_s = {}
            cntr = 0
            while cntr <= len(s)-1:
                if s[cntr] not in map_s_to_t and t[cntr] in map_t_to_s:
                    return False
                if  s[cntr] in map_s_to_t and t[cntr] not in map_t_to_s:
                    return False
                map_s_to_t[s[cntr]] = t[cntr]
                map_t_to_s[t[cntr]] = s[cntr]
                cntr += 1
            return True




        