 int firstUniqChar(string s) {
    unordered_map<char, int> map;

    for(int i = 0; i < s.length(); ++i){
        map[s[i]]++; // increment map's value for s[i]
    }

    for(int i = 0; i < s.length(); ++i){
        if(map[s[i]] == 1){
            return i;
        }
    }

    return -1;
}

// ===================================================

vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> n;
        vector<int> indices;
        
        for(int i = 0; i < nums.size(); ++i){
            n.insert(make_pair(nums[i], i));    
        }
        
        for(int i = 0; i < nums.size(); ++i){
            int addend = target-nums[i];
            
            if(n.count(addend) > 0 && i != n[addend]){
                indices.push_back(i);
                indices.push_back(n[addend]);
                
                return indices;
            }
        }
        return {-1, -1};
    }
};

// ===================================================

 bool containsNearbyDuplicate(vector<int>& nums, int k) {
    unordered_map<int, int> map;
    bool isNearDuplicate = false; 

    // store elements and their indices in map
    for(int i = 0; i < nums.size(); ++i){
        if(map.count(nums[i]) > 0){
            if(abs(map[nums[i]] - i) <= k){
                isNearDuplicate = true;
            }
            map[nums[i]] = i; // update element value w/ new index
        }else{
            map.insert(make_pair(nums[i], i));
        }
    }
    return isNearDuplicate;
}

// ===================================================

vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
    unordered_set<int> hash, intersection;
    vector<int> result;

    for(int i: nums1){
        hash.insert(i);
    }

    for(int j: nums2){
        if(hash.count(j) > 0){
            intersection.insert(j);
        }
    }

    for(int k: intersection){
        result.push_back(k);
    }

    return result;
}
