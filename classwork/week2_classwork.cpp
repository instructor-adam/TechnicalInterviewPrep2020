//design hashmap

class MyHashMap {
private:
    vector<long int> hash_map ;
public:
    /** Initialize your data structure here. */
    MyHashMap() {
        hash_map.resize(1000000, -1);
    }
    
    /** value will always be non-negative. */
    void put(int key, int value) {
        hash_map[key] = value;
    }
    
    /** Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key */
    int get(int key) {
        return hash_map[key];
    }
    
    /** Removes the mapping of the specified value key if this map contains a mapping for the key */
    void remove(int key) {
        hash_map[key] = -1;
    }
};

//contains duplicate

bool containsDuplicate(vector<int>& nums) {
        unordered_set<int> mySet;
        
        for(int i : nums){
            if(mySet.count(i) > 0){
                return true;
            }
            mySet.insert(i);
        }
        return false;
    }
	
// single number

int singleNumber(vector<int>& nums) {
        unordered_map<int, int> storeNums;
        
        for(int n : nums){
            // cout << n << endl;
            if(storeNums.find(n) != storeNums.end()){
                // cout << "remo"
                storeNums.erase(n);
            }else{
                storeNums[n]++;
            }
        }
        
        for(auto& x: storeNums){
            return x.first;
        }
        
        return 1;
    }
	
//intersection of two numbers

vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
        unordered_set<int> mySet;
        vector<int> result;
        
        for(int i : nums1){
            mySet.insert(i);
        }
        
        for(int j : nums2){
            if(mySet.count(j) > 0){
                result.push_back(j);
                mySet.erase(j);
            }
        }
        
        return result;
    }
	
//happy number

bool isHappy(int n) {
        
        unordered_set<int> mySet;
        
        while(n != 1){
            int num = n;
            int result = 0;
            while(num > 0 ){
                result += pow(num%10,2);
                num = num/10;
            }
            n = result;
            
            if(mySet.count(n) > 0){
                return false;
            }else{
                mySet.insert(n);
            }
            
        }
        
        
        return true;
    }
	
//first unique character

int firstUniqChar(string s) {
        unordered_map<char, int> myMap;
        
        for(int i = 0; i < s.length(); i++){
            myMap[s[i]]++;
        }
        
        for(int i = 0; i < s.length(); i++ ){
            if(myMap[s[i]] == 1){
                return i;
            }
        }
        
        return -1;
    }
	
//sort colors

    void sortColors(vector<int>& nums) {        
        int zeroP = 1, oneP = 0, twoP = 0;
        
        while(zeroP < size()){
            if(nums[oneP] != 1 ){
                oneP++;
            }
            if(nums[twoP] != 2){
                twoP++;
            }
            if(nums[zeroP] != ){
                zeroP ++
            }else{
                if (twoP < oneP && twoP < zeroP){
                    nums[twoP] = 0;
                    nums[zeroP] = 2;
                    
                    twoP++;
                    zeroP++;
                }
            }
        }
        
        // return nums;
    }
		
//remove linked list element

ListNode* removeElements(ListNode* head, int val) {
        ListNode* curr = head;
        ListNode* dummyHead = head;
        
        if(head == nullptr){
            return head;
        }else{
            ListNode* prev = curr;
            while(curr != nullptr){
                if(curr->val == val){
                    if(curr == prev){
                        ListNode* temp = curr;
                        curr = curr->next;
                        prev = curr;
                        dummyHead = curr;
                        delete temp;
                    }else{
                        ListNode* temp = curr;
                        prev->next = curr->next;
                        curr = curr->next;
                        delete temp;
                    }
                }else{
                    if(prev == curr){
                        curr = curr->next;
                    }else{
                        prev = curr;
                        curr = curr->next;
                    }
                }
            }
        }

//reverse linked list 

ListNode* reverseList(ListNode* head) {
        if(head != nullptr){
            ListNode* temp = head;
            ListNode* curr = head->next;
            while(curr != nullptr){
                temp->next = curr->next;
                curr->next = head;
                head = curr;
                curr = temp->next;
            }
        }
        
        return head;
    }


