class Solution {
public:
    int climbStairs(int n) {
        // if 0 or 1 stair
        if(n == 0 || n == 1){
            return 1;
        }
        int i = 1;
        int curr = 1;
        int prev = 1;
        while(i<n){
            int next = curr + prev;
            prev = curr;
            curr = next;
            i++;
        }
        return curr;
    }
};