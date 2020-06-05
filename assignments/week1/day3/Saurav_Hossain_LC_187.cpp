class Solution 
{
public:
    vector<string> findRepeatedDnaSequences(string s) 
    {
        //chop up entire string into 10 length increments vec of str
        //do find of increments on original string except where it was found, so omit that part and everything before it 
        //if we cant find kick it out of vector, if we can keep it
            //^ should take care of dupe problem if 2 instances are found the second instance doesnt kick in to find 4 
        
        vector<string> choped;
        
        for(int i = 0 ; i < s.length() - 10; i++)
        {
            string c = s.substr(i, 10);
            choped.push_back(c);
        }
        
        //vector contains all 10 incremented chop values, now we need to edit and search 
        for(int i = 0; i < choped.size(); i++)
        {
            //edit string s in a way to look for dupes
            string es = s.substr(i+1);
            if(es.find(choped[i]) == string::npos) // if dont find it we drop it
            {
                  choped.erase(choped.begin());
            }
        }
        
        return choped;
    }
};
