"""
LeetCode 242. Valid Anagram (Easy)

Problem Statement:
Given two strings `s` and `t`, return `true` if `t` is an anagram of `s`, 
and `false` otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a 
different word or phrase, typically using all the original letters exactly once.

Example 1:
    Input: s = "anagram", t = "nagaram"
    Output: true

Example 2:
    Input: s = "rat", t = "car"
    Output: false

Constraints:
    * 1 <= s.length, t.length <= 5 * 10^4
    * s and t consist of lowercase English letters.

Follow-up: What if the inputs contain Unicode characters? How would you adapt 
your solution to such a case?


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # TODO: Implement an efficient frequency counting strategy
        pass

# --- Test Cases ---
if __name__ == "__main__":
    sol = Solution()
    
    # Test Case 1
    assert sol.isAnagram("anagram", "nagaram") is True, "Failed Test Case 1"
    
    # Test Case 2
    assert sol.isAnagram("rat", "car") is False, "Failed Test Case 2"
    
    print("All basic test cases parsed successfully!")
"""


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if sorted(s) == sorted(t):
            return True
        return False
            
                


        
