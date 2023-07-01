#LeetCode 242: Valid Anagram
#Given two strings s and t, return true if t is an anagram of s, and false otherwise.
#An Anagram is a word or phrase formed by rearranging the letters of a different word 
#or phrase, typically using all the original letters exactly once.
def isAnagram(s, t):
        s_sorted = sorted(s)
        t_sorted = sorted(t)
        if s_sorted == t_sorted:
            return True
        else:
            return False