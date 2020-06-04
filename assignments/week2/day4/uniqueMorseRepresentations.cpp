using namespace std;

class Solution { 
    
    
public:
    
    int uniqueMorseRepresentations(vector<string>& words) {
        map<char, string> morseMap= { {'a',".-"},{'b',"-..."},{'c', "-.-."},{'d',"-.."},{'e',"."},{'f',"..-."},{'g',"--."},{'h',"...."},{'i',".."},{'j',".---"},{'k',"-.-"},{'l',".-.."},{'m',"--"},{'n',"-."},{'o',"---"},{'p',".--."},{'q',"--.-"},{'r',".-."},{'s',"..."},{'t',"-"},{'u',"..-"},{'v',"...-"},{'w',".--"},{'x',"-..-"},{'y',"-.--"},{'z',"--.."} };
        vector<string> codeSet;
        string code;
        for(int i = 0; i < words.size(); i++)
        {
            code.clear();
            for(int j = 0; j < words[i].length(); j++)
                code += morseMap.find(words[i][j])->second;
            
            if(count(codeSet.begin(), codeSet.end(), code) == 0)
                codeSet.push_back(code);
        }
        return codeSet.size();
    }
};
