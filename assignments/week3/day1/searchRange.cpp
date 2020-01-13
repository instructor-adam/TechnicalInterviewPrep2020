class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        vector<int> res_ = {-1,-1};

        if(nums.empty()){
            return res_;
        }
        else if(nums[0]==target && nums.size()==1){
            return res_={0,0};
        }
        for(int i=0;i<nums.size();i++){
            if(nums[i]==target){
                res_[0]=i;
                res_[1]=i;
                break;
            }
        }
        for(int j=0;j<nums.size();j++){
            if(nums[j]==target){
                res_[1]=j;
            }
        }

        return res_;
    }
};