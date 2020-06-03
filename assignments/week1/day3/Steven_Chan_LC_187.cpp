class Solution {
public:
    vector<string> findRepeatedDnaSequences(string s) {
        
        //Brute force method that re-does work as I have not learn how to use hash maps
        
        vector<string> store;
        
        for(int i = 0; i < s.size(); i++) { //at each i we need to store the next 9
            
            string temp = "";
            
            for(int j = i; j < i+2; j++) { //loop every ten letters from ith position
                
                temp += s[j];
                
            }
            
            store.push_back(temp);
        }
        
        //works up to here so far
        
        //now we need to compare each element in vector and take note of any that occur more than once
        //if it occurs more than once we should output it
        
        vector<string> repeated;
        
        for(int i = 0; i < store.size(); i++) {
            
            for(int j = i; j < store.size(); i++) {
                
                if(store[i] == store[j]) {
                    
                    repeated.push_back(store[i]);
                    
                    //think of a way to remove it so we don't repeat
                    store[i] = store[i] + "done"; //this only does it for the first two
                    store[j] = store[j] + "next";
                    
                }
            }
            
        }
        
        return repeated;
        
    }
};