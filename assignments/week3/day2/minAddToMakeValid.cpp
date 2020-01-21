class Solution {
public:
    int minAddToMakeValid(string S) {
        stack<char> min_paren;
        int count_ = 0;
        for(int i=0; i<S.length();i++){
            if(S[i]=='('){
                min_paren.push(S[i]);
            }
            else if(!min_paren.empty()&&S[i]==')'){
                min_paren.pop();                        
            }
            else{
                count_++;
            }
        }
            
        while(!min_paren.empty()){
            count_++;
            min_paren.pop();
        }
        return count_;
    }
};