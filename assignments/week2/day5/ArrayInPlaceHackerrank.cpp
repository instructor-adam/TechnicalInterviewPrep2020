/* Hackerrank Destination/SOurce In-place Problem: Improved solution */

void destination(vector<int> destination, vector<int> source, int start){
  int d_index = destination.size() + start; // start index for shifting elements in destination
  d.resize(d.size() + source.size());
  
  int s_index = 0; // source index for iterating through source
  for(int i = 0; i < destination.size(); ++i){
    if(i == start){
      int temp = destination[i]; // save element
      destination[i] = source[s_index];
      s_index++;
      if(s_index < source.size()){
        start++; // shift index to insert next element from source array
      }
      if(d_index < destination.size()){
        destination[d_size] = temp;
        d_index++;
      }
    }
  }
}
