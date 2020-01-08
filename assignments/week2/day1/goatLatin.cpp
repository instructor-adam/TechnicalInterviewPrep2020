//goat latin
//824

class Solution {
public:
    bool isVowel(char firstLetter){
        return firstLetter == 'a' || firstLetter == 'e' || firstLetter == 'i' || firstLetter == 'o' || firstLetter == 'u' || firstLetter == 'A' || firstLetter == 'E' || firstLetter == 'I' || firstLetter == 'O' || firstLetter == 'U' ;
    }
    
    string toGoatLatin(string S) {
        vector<string> sentence;
        string result = "";
        istringstream ss(S);
        
        do{
            string word;
            ss >> word;
            sentence.push_back(word);
        }while(ss);
        
        for(int i = 0; i < sentence.size()-1; i++ ){
            if(isVowel(sentence[i][0])){
                // int lastIndex = sentence[i].length()-1;
                sentence[i] += "ma";
                // sentence[i].erase(0, 1);
                for(int j = 0; j < i+1; j++){
                    sentence[i] += 'a';
                }
                
            }else{
                char firstChar = sentence[i][0];
                sentence[i] += firstChar;
                sentence[i] += "ma";
                sentence[i].erase(0, 1);
                for(int j = 0; j < i+1; j++){
                    sentence[i] += 'a';
                }
            }
            if(i != sentence.size()-2){
                result += sentence[i]+" ";
            }else{
                result += sentence[i];
            }
            
        }
        
        return result;
    }
};