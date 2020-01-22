# https://leetcode.com/problems/flipping-an-image/
class Solution {
public:
  vector<vector<int>> flipAndInvertImage(vector<vector<int>>& A) {
    for (auto & i : A){
      reverse(i.begin(), i.end());
      transform(i.begin(), i.end(), i.begin(),
                [](bool bit) -> bool {return !bit;} );
    }
    return A;
  }
};
