/* https://leetcode.com/problems/daily-temperatures/ */

class Solution {
public:

    vector<int> dailyTemperatures(vector<int>& T) {
        vector<int> untilWarmer(T.size(), 0);
        stack<int> s;
        
        s.push(T.size()-1);
        
        for(int i  = T.size()-1; i > -1; --i){
            
            // if(s.empty()){s.push(T(7));}
            if(!s.empty() || T[i] > T[s.top()]){ // curr temp is greater than top of stack
                s.pop();
                s.push(i);
            }else if(T[i] < T[s.top()]){
                untilWarmer[i] = abs(i-s.top());
                cout << "Hello :" << abs(i-s.top()) << endl;
                s.push(i);
            }
        }
               
        return untilWarmer;
    }
    
    /* Approach #1:
        vector<int> untilWarmer;

        for(int i = 0; i < T.size(); ++i){
            for(int j = i; j < T.size(); ++j){
                if(T[j] > T[i]){
                    untilWarmer.push_back(abs(j-i));
                    break;
                }else if(j == T.size() -1){
                    untilWarmer.push_back(0);
                }
            }
        }

        return untilWarmer;
        
        */
};
