//34. Find First and Last Position of Element in Sorted Array

int findLowestIndex(vector<int> arr, int target, int index){
        while(arr[index] == target){
            --index;
            if(index == -1){
                break;
            }
        }
        return index+1;
    }
    int findHighestIndex(vector<int> arr, int target, int index){
        //index++;
        while(arr[index] == target){
            ++index;
            
            if(index == arr.size()){
                break;
            }
        } 

        return index-1;
    }
    vector<int> findIndices(vector<int> arr, int target, int low, int high){
        int mid = low+(high-low)/2;
        vector<int> indicies;
        if(low <=high){
            if(arr[mid] == target){
                indicies.push_back(findLowestIndex(arr, target, mid));
                indicies.push_back(findHighestIndex(arr, target, mid));
                return indicies;
            }else if(arr[mid] < target){
                return findIndices(arr, target, mid+1, high); 
            }else if(arr[mid] > target){
                return findIndices(arr, target, low, mid-1);
            }
        }

        return {-1,-1};
    }
    vector<int> searchRange(vector<int>& nums, int target) {
        return findIndices(nums, target, 0, nums.size()-1);
    }
	
//remove duplicates from sorted array

int removeDuplicates(vector<int>& nums) {
        if(nums.size() == 0){
            return nums.size();
        }
        int prevValue = nums[0];
        
        int i = 1;
        
        while(i < nums.size()){
            if(nums[i] == prevValue){
                nums.erase(nums.begin()+i);
            }else{
                prevValue = nums[i];
                i++;
            }
        }
        
        return nums.size();
    }
	
//daily temperature
vector<int> dailyTemperatures(vector<int>& T) {
        
        int count = 0;
        int i, j;
        vector<int> result;
        
        for(i = 0; i < T.size(); ++i ){
            count = 0;
            bool dayFound = false;
            for( j = i+1; j < T.size(); ++j ){
                if(T[j] <= T[i]){
                    count++;
                }else{
                    count++;
                    result.push_back(count);
                    // count = 0;
                    dayFound = true;
                    break;
                }
            }
            
            if(!dayFound){
                result.push_back(0);
            }
            
        }
        
        return result;
    }
	
//minimum add to make parentheses valid

int minAddToMakeValid(string S) {        
        stack<char> myStack;
        int result = 0;
        
        for(char c: S){
            if(c == '('){
                myStack.push(c);
            }else{
                if(myStack.empty()){
                    ++result;
                }else{
                    myStack.pop();
                }
            } 
        }
        
        return myStack.size()+result;
    }
	
//