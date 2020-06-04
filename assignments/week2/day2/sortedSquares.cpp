//Cordell Hurst
//977. Squares of a Sorted Array

class Solution {
public:
    vector<int> sortedSquares(vector<int>& A) {
        
        bool hasNegative = 0;
        if(A[0] < 0)
            hasNegative = 1;
        
        for(int i = 0; i < A.size(); i++)
            A[i] = A[i]*A[i];
        
        if(hasNegative)
            sort(A.begin(), A.end());
        
        return A;
    }
};
