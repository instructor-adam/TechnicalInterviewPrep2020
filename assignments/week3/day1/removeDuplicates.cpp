class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
       int nextElement = 1;
       for(int i=1; i<nums.size(); i++){
           if(nums[i] != nums[nextElement-1]){
               nums[nextElement] = nums[i];               
               nextElement++;
           }
       }
       if(nums.size()==0){
           return nums.size();
       }
       nums.resize(nextElement);
       return nums.size();
    }
};