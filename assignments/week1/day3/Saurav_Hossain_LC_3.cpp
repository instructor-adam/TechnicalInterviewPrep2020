class Solution 
{
public:
    int lengthOfLongestSubstring(string s) 
    {
        //go thru whole string
        //as we go we set a temp string and add to it characters until we see a repeating character 
          //check for repeatig with .find 
          //we need to find the longest one, so by that logic we need to put away first longest one found incase that is the longest, if it isnt then we use a new one (vector of string or just reset the string after we see that our old one is longer or not)
    
        string tempLong = ""; //current string being added to 
        string lastLong = ""; //last longest found string, should be overridden when we find a longer one 

        //traverse string
        for(int i = 0; i < s.length(); i++)
        {
            //if we find the current char then we put away current longest and start temp over 
            if (tempLong.find(s[i]) != string::npos)
            {
                //if the last stored longest was shorter we dont care for it 
                if(lastLong.length() < tempLong.length())
                {
                    lastLong = tempLong;
                } 
                tempLong = s[i];
            }
            else
            {
                tempLong = tempLong + s[i];  //just add to current              
            }
        }
        
        
        if(tempLong.length() > lastLong.length())
            return tempLong.length();
        else
            return lastLong.length();
    }
};
