class Solution {
public:
void sortColors(vector<int>& nums) {
    vector<int> count(3);
    vector<int> res;
    for(int i=0; i<nums.size();i++){
        count[nums[i]]++;
    }
    for(int j=0; j<count.size();j++){
        for(int k=0; k<count[j];k++){
            res.push_back(j);
        }
    }
        nums = res;
    }
};

//https://leetcode.com/problems/sort-colors/