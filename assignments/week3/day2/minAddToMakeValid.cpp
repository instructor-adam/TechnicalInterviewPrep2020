class Solution {
public:
    int minAddToMakeValid(string S) {
        stack<char> min_paren;
        int count_ = 0;
        // iterate through string
        for(int i=0; i<S.length();i++){
            // open brace to match
            if(S[i]=='('){
                min_paren.push(S[i]);
            }
            // try to match
            else if(!min_paren.empty()&&S[i]==')'){
                min_paren.pop();                        
            }
            // count unmatched ')'
            else{
                count_++;
            }
        }
        // empty the stack if there is lingering '('
        while(!min_paren.empty()){
            count_++;
            min_paren.pop();
        }
        return count_;
    }
};