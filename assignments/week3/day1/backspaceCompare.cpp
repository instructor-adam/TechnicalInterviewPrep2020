class Solution {
public:
    bool backspaceCompare(string S, string T) {
        stack<char> wS, wT;
        string wordS, wordT;
        
        for(char c: S){
            if(c != '#'){
                wS.push(c);
            }else if(!wS.empty()){
                wS.pop();
            }
        }
        
        for(char c: T){
            if(c != '#'){
                wT.push(c);
            }else if(!wT.empty()){
                wT.pop();
            }
        }
        
                
        while(!wS.empty()){
            wordS += wS.top();
            wS.pop();
        }
        
        while(!wT.empty()){
            wordT += wT.top();
            wT.pop();
        }
        
        return wordS == wordT;
    }
};
