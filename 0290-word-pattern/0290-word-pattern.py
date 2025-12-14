class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s_list = s.split(' ')
        if len(pattern) != len(s_list):
            return False
        else:
            map_pat_to_s = {}
            map_s_to_pat = {}
            for i, word in enumerate(s_list):
                if word not in map_s_to_pat and pattern[i] not in map_pat_to_s:
                    map_s_to_pat[word] = pattern[i]
                    map_pat_to_s[pattern[i]] = word
                else:
                    if word in map_s_to_pat and map_s_to_pat[word] != pattern[i]:
                        return False
                    if pattern[i] in map_pat_to_s and map_pat_to_s[pattern[i]] != word:
                        return False
            return True



        