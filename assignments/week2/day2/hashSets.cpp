bool containsDuplicate(vector<int>& nums) {
    unordered_set<int> find_dup;
    for(int n: nums){
        if(find_dup.count(n) > 0){
            return true;
        }
        find_dup.insert(n);
    }
    return false;
}

// ===============================================================

int singleNumber(vector<int>& nums) {
    unordered_set<int> hash;

    for(int i: nums){
        if(hash.count(i) > 0) {
            hash.erase(i);
        }else {
            hash.insert(i);
        }
    }

    for(int i: hash){
       return i;
    }
    
    return -1;
}

// ================================================================

bool isHappy(int n) {
    unordered_set<int> hash; // the sum of the square of its digits

    if(n == 1){
        return true;
    }

    int sum = sumOfSquares(n);
    while(sum != 1){
        if(hash.count(sum) > 0){
            return false; // loop
        }
        hash.insert(sum);
        sum = sumOfSquares(sum);
    }
    return true;
}

int sumOfSquares(int n){
    int sum = 0, digit = 0;

    while(n > 0){
        digit = n % 10;
        sum += digit*digit;
        n = n/10;
    }

    return sum;
}

// ===================================================================
