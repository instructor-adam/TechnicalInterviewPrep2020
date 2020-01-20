class Solution {
public:
    string toGoatLatin(string S) {
    	//split the sentence into words
    	let words = S.split(' ');
    	string goat_latin_ending = 'ma';
    	//traverse through each word
    	//check if first char is a vowel or consonant
    	//if vowel, append "ma" to end of each word
    	//if consonant, move first char to end of word, append "ma"

    	for (int i = 0; i < S.size; i++){
    	}
        if (begin(S) == 'a' || begin(S) == 'e' || begin(S) == 'i' || begin(S) == 'o' || begin(S) == 'u')
        	return << S + goat_latin_ending;
        else if {
        	string first_letter = begin(S);
        	string remove_first_letter = S.erase(begin(S))
        	return remove_first_letter + " " + first_letter + " " + goat_latin_ending;
        }
        //return new S
    }
};