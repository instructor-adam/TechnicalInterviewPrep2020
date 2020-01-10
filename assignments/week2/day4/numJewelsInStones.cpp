class Solution {
public:
    int numJewelsInStones(string J, string S) {
/*        //stupid fast (0 ms, 100%) and low memory (8.3 MB, 91.25%)
        int count = 0;
        for(char possible : S)
            if(J.find(possible) != string::npos)
                count++;
        
        return count;
    }
};*/

     
     //Fast (0 ms, 100%) but high memory usage (8.6 MB, 31.25%)
        unordered_map<int, int> map1;
        int count = 0;
        for(int i = 0; i < J.length(); i++) {
            map1.emplace(J[i], i);
        }
        for(int i = 0; i < S.length(); i++) {
            count += map1.count(S[i]);
        }
        return count;
    }
};

//J == Jewels
//S == Misc_Stones
