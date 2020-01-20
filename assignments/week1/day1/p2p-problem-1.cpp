#include <string>
#include <iostream>
using namespace std;

class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
    	//longestCommonPrefix accepts a Vector of String type passed by reference
        // iterate through the array
        //for each string in the array, get the first two letters
        for (int i = 0; i <= strs.size(); i++){
        	string first_two = strs.substr(0,2);
        	//if the first two letters in each element are the same, return the the first two letters
        	//if the first two letters are not the same, return an empty string: ""
        	if(first_two.compare(first_two) == 0){
        		return first_two;
        	} else {
        		return << " ";
        	}

        }
        
    }
};