vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> map;
        vector<vector<string>> anagrams;
        
        for(string s: strs){
            string key = createKey(s);
            if(map.count(key) > 0){
                map[key].push_back(s);
            }
            vector<string> temp {s};
            
            map.insert(make_pair(key, temp));
        }
        
        for(pair<string, vector<string>> p: map){
            vector<string> temp;
            for(int i = 0; i < p.second.size(); ++i){
                temp.push_back(p.second[i]);
            }
            anagrams.push_back(temp);
        }
        
        return anagrams;
    }
    
    string createKey(string word){
        string the_key = word;
        sort(the_key.begin(), the_key.end());
        return the_key;
    }
