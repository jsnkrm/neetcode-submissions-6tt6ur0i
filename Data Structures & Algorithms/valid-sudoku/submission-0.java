class Solution {
    public boolean isValidSudoku(char[][] board) {
        return isRowValid(board) && isColumnValid(board) 
                && isSubBoxValid(board);
    }
    private boolean isRowValid(char[][] board) {
        int[] count = new int[9];
        for( int i =0; i < 9 ; i++) {
            Arrays.fill(count,0);
            for ( int j =0; j < 9 ; j++) {
                if(board[i][j] != '.') {
                    count[board[i][j] - '0' - 1]++;
                }
            }
            for(int k = 0; k < 9; k++) {
                if(count[k] > 1){ 
                    System.out.println("row");
                    return false;
                }
            }
        }
        return true;
    }
    private boolean isColumnValid(char[][] board) {
        int[] count = new int[9];
        for( int i = 0; i < 9 ; i++) {
            Arrays.fill(count,0);
            for ( int j = 0; j < 9 ; j++) {
                 if(board[j][i] != '.') {
                    count[board[j][i] - '0' - 1]++;
                }
            }
            for(int k = 0; k < 9; k++) {
                if(count[k] > 1){ 
                    System.out.println("col");
                    return false;
                }
            }
        }
        return true;
    }
    private boolean isSubBoxValid(char[][] board) {
        for (int square = 0; square < 9; square++) {
            Set<Character> seen = new HashSet<>();
            for (int i = 0; i < 3; i++) {
                for (int j = 0; j < 3; j++) {
                    int row = (square / 3) * 3 + i;
                    int col = (square % 3) * 3 + j;
                    if (board[row][col] == '.') continue;
                    if(seen.contains(board[row][col])) return false;
                    seen.add(board[row][col]);
                }
            }
        }
        return true;
    }
}

