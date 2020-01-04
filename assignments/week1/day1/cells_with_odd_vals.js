// Cells With Odd Values In A Matrix

/**
 * @param {number} n
 * @param {number} m
 * @param {number[][]} indices
 * @return {number}
 */

var oddCells = function(n, m, indices) {
  var matrix =  [];   // intialize matrix 
  
  var odd_nums = 0;   // initialize odd number counter
  
  for(var i = 0; i < n; i++) {
    matrix[i] = [];
    for(var j = 0; j < m; j++) {
      matrix[i][j] = 0;
    }
  }
  
  // increment rows and columns
  for(var x = 0; x < indices.length; x++) {   // get row col pair from indices 
    var row = indices[x][0];
    var col = indices[x][1];
    
    for(var c = 0; c < m; c++) {  // increment row of initialized matrix 
      matrix[row][c] += 1;        // increment the entire row by incrementing each column 
    }
    
    for(var r = 0; r < n; r++) {    // increment column of initial matrix  
      matrix[r][col] += 1;          // increment entire column by iterating each row
    }
  }
    
  // count odd values in matrix 
  for(var matrix_row = 0; matrix_row < n; matrix_row++) {   
    for(var matrix_col = 0; matrix_col < m; matrix_col++) {
      if(matrix[matrix_row][matrix_col] % 2 == 1) {   // if cell is odd, add 1 to odd number count 
        odd_nums += 1; 
      }
    }
  }
  
  return odd_nums
};