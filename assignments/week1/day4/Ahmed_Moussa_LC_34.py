class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        int l=0, r=nums.size()-1;
        int start = -1, ed = -1;
        while(l <= r) {
            int mid = (l+r)/2;
            if(nums[mid] < target) l = mid + 1;
            else {
                if(nums[mid] == target) start = mid;
                r = mid - 1;
            }
        }
        if(start != -1) l = start, r = nums.size()-1;
        while(l <= r) {
            int mid = (l+r)/2;
            if(nums[mid] > target) r = mid - 1;
            else {
                if(nums[mid] == target) ed = mid;
                l = mid + 1;
            }
        }
        return {start, ed};
    }

};
