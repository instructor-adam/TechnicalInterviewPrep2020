def findAnagrams(s, p):
    result = []
    p = sorted(p)
   #generate all substrings 
    for i in range(len(s)):
        j = i + 1
        for j in range(len(s)+1):
            if len(s[i:j]) is len(p):
                #sort string of same length 
                sub_str = sorted(s[i:j])
                # should be same if anagram 
                if sub_str == p:
                    result.append(i)

    return result

# run time is O(N^2*N log N) space O(1)
# passes 22 of 36 test cases exceeds time limit on 23rd test case 
# see image in folder for  leetcode results 