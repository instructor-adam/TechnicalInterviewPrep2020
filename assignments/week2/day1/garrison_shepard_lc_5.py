s = "babad"

def isPalindrome(s):
    return s == s[::-1] 
    
def longestPalindromeSubstring(s):
    length = 0
    longest = ""
    for i in range(len(s)): 
        for j in range(i+1,len(s)+1): 
            if isPalindrome(s[i:j]):
                if length < len(s[i:j]):
                    length = len(s[i:j])
                    longest = s[i:j]

    return longest
