public class SuperTicTacToeAI extends SuperTicTacToe {
    private static final int WIN_SCORE = 100; // Score assigned to a winning move
    private static final int BLOCK_SCORE = 50; // Score assigned to a move that blocks the opponent's winning move
    private static final int OPEN_SPACE_SCORE = 1; // Score assigned to an open space
    
    @Override
    public int[] nextMove(SuperTicTacToe gs, char maxPlayer) {
        char[][] board = gs.getBoard();
        int[] activeBoard = gs.getActiveBoard();
        
        int bestScore = Integer.MIN_VALUE;
        int[] bestMove = null;
        
        for (int x = 0; x < BOARDSIZE; x++) {
            for (int y = 0; y < BOARDSIZE; y++) {
                int[] move = new int[]{x, y};
                
                if (inActiveBoard(move) && board[x][y] == SPACE) {
                    // Make a copy of the current board
                    char[][] tempBoard = copyBoard(board);
                    
                    // Apply the move to the temporary board
                    implementMove(move, maxPlayer, tempBoard);
                    
                    // Evaluate the board position using the heuristic function
                    int score = evaluateBoardPosition(tempBoard, maxPlayer);
                    
                    // Update the best move if the current move has a higher score
                    if (score > bestScore) {
                        bestScore = score;
                        bestMove = move;
                    }
                }
            }
        }
        
        return bestMove;
    }
    
    private int evaluateBoardPosition(char[][] board, char maxPlayer) {
        int score = 0;
        
        // Evaluate rows
        for (int row = 0; row < BOARDSIZE; row++) {
            score += evaluateLine(board[row][0], board[row][1], board[row][2], maxPlayer);
        }
        
        // Evaluate columns
        for (int col = 0; col < BOARDSIZE; col++) {
            score += evaluateLine(board[0][col], board[1][col], board[2][col], maxPlayer);
        }
        
        // Evaluate diagonals
        score += evaluateLine(board[0][0], board[1][1], board[2][2], maxPlayer);
        score += evaluateLine(board[0][2], board[1][1], board[2][0], maxPlayer);
        
        return score;
    }
    
    private int evaluateLine(char cell1, char cell2, char cell3, char maxPlayer) {
        int score = 0;
        
        // Count the number of maxPlayer's symbols in the line
        int maxPlayerCount = 0;
        if (cell1 == maxPlayer) {
            maxPlayerCount++;
        }
        if (cell2 == maxPlayer) {
            maxPlayerCount++;
        }
        if (cell3 == maxPlayer) {
            maxPlayerCount++;
        }
        
        // Evaluate the line based on the count of maxPlayer's symbols
        if (maxPlayerCount == 3) {
            score = WIN_SCORE; // Max player wins
        } else if (maxPlayerCount == 2) {
            score = BLOCK_SCORE; // Block the opponent's winning move
        } else if (maxPlayerCount == 1) {
            score = OPEN_SPACE_SCORE; // Open space for future moves
        }
        
        return score;
    }
}