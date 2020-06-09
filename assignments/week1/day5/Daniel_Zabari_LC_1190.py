class Solution:
    def reverseParentheses(self, s: str) -> str:
        tup = self.reverse_helper(s)
        return tup[0]
        

    def reverse_helper(self, s):
        final = ""
        i = 0
        count = 1
        while (i < len(s)):
            if (s[i] == "("):
                reverse_string, sub_count = self.reverse_helper(s[i+1:])
                reverse_string = reverse_string[::-1]
                count += sub_count + 1
                i += len(reverse_string) + sub_count
                final += reverse_string
            elif (s[i] == ")"):
                return (final, count)
            else:
                final += s[i]
            i += 1
        return (final, count)
