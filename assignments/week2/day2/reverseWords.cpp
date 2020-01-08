//Cordell Hurst
//557. Reverse Words in a String III

class Solution {
public:
    string reverseWords(string s) {
        
        int start = 0;
        int size = s.size();
        string results;
        
        results.reserve(size);
        for(int i = 0; i < size; i++)
        {
            if(s[i] != ' ')
                results.insert(start, 1, s[i]);
            else
            {
                results += ' ';
                start = i+1;
            }
                
        }
        return results;
    }
};
