//Longest Common Prefix
//lettcode 14

string longestCommonPrefix(vector<string>& strs) {
    if(strs.size() == 0){
        return "";
    }
    string result = "";
    int index = 0, minimumLength  = strs[0].length();
        
    for(int i = 1; i < strs.size(); ++i){
        if(strs[i].length() < minimumLength){
            minimumLength = strs[i].length();
        }
    }
        
    while(index < minimumLength){
        for(int i = 1; i < strs.size(); ++i){
            if(strs[0][index] != strs[i][index]){
                return result;
            }
        }
        result += strs[0][index];
        ++index;
    }
        
    return result;
}