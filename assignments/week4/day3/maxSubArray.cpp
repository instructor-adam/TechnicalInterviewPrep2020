class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        // initial value of max_sum
        int max_sum = INT_MIN;
        // moving sum
        int curr_sum = 0;
        for(int i=0;i<nums.size();i++){
        	// check curr sum + next val against nex val
            curr_sum = max(curr_sum + nums[i],nums[i]);
            // check moving sum against max sum
            max_sum = max(max_sum,curr_sum);
            if(curr_sum<0){
                curr_sum = 0;
            }
        }
        return max_sum;
    }
};