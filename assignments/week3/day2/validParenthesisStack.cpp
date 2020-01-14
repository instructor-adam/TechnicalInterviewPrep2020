stack<char> s;
        int ctr = 0;
        
        
        for(char c : S){
            if(c == '('){
                s.push(c);
            }else if(!s.empty() && s.top() == '('){
                s.pop();
            }else{
                ctr++;
            }
        }
        
        
        
        while(!s.empty()){
            ctr++;
            s.pop();
            
        }
        
        return ctr;
    }
