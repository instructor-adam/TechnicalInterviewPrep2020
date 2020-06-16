
#  i really struggled with this question (even the brute force)
#  this is a brute force solution i found online from geeks to geeks
#  i understand this solution. i explain each line below 
#  in general i really struggle with any dynamic programming 
#  question 
# 
def perfectSquares(n): 
    if n <= 3: 
        return n; 
  
    res = n
    # we loop through number swho are a square that is smaller than n
    # at each iteration we make a recursive call
    # we make use of the fact that our number n minus 
    # some perfect square ... minus some perfect sqaure 
    # will eventually each zero and that number 
    # can be found by adding up all those numbers 
    #  each time we find a result we take the min with the previous result
    # the result is a count of the minum perfect saqaure needed to sum
    # to the number 
    for x in range(1, n + 1): 
        temp = x * x; 
        if temp > n: 
            break
        else: 
            res = min(res, 1 + perfectSquares(n  
                                  - temp)) 
      
    return res; 