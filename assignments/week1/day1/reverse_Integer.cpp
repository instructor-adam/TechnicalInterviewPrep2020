class Solution {
public:
    int reverse(int x) {
        
        if(x < -2147483647)
            return 0;
           
        string revStr;
        if (x < 0) {
            revStr = "-";
            x *= -1;
        }
        
        int bigMax = x%1000000000;
        int max = x%10;
        if((max > 2 || bigMax > 463847412) && x > 999999999)
            return 0;
        
        string str = to_string(x);
        int length = str.length();
        
        int i = length-1;
        for (; i >= 0; i-- ) {
            revStr += str[i];
        }
        x = stoi(revStr);
        
        return x;
    }
};
        //cout << str[i] << " i: " << i << endl;

        //Max 2,147,483,647
        //Min -2,147,483,648
