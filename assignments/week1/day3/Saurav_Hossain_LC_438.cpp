class Solution 
{
public:
    
    //gotta have a isAnagram helper fucntion 

    //will check if string x appears inside y as an anagram 
    //in this case it has the precondition that both strings are the same length 
    bool isAnagram(string x, string y)
    {
      for(int i = 0; i < x.length(); i++)
      { 
        if(x.find(y[i]) == string::npos) //not found
          return false;
      }
      return true;
    }    
    
    vector<int> findAnagrams(string s, string p) 
    {
        //split the big string into all possible lengths of small string and run isAnagram
        vector <string> holdsEachPossibleCombo;
        int it = 0;
        for(int i = 0; i < s.length()-p.length(); i++)
        {
            holdsEachPossibleCombo[it] = s.substr(s[i], p.length());
            it++;
        }
    }
    
    //gotta go to 340...
};
