public class greedy extends SuperTicTacToeAI{
    private SuperTicTacToe game;
    final char aiPlayer = 'X';
    public greedy(SuperTicTacToe game) {
        this.game = game;
    }
    
    public int[] getBestMove(char[][] board) {
        int bestScore = Integer.MIN_VALUE;
        int[] bestMove = new int[2]; //store the best move

        //iterate through all cells on the board
        for (int i = 0; i < board.length; i++) {
            for (int j = 0; j < board[i].length; j++) {
                //check if the move is valid
                if (game.checkMoveValidity(new int[] {i, j}, aiPlayer, board)) {
                    //make a copy of the board
                    char[][] copy = copyBoard(board);
                    //simulate a move on the copied board
                    copy[i][j] = aiPlayer; 
                    //evaluate the board state after the move
                    int score = evaluateBoard(copy);
                    System.out.printf("Move [%d,%d] has score %d\n", i, j, score);
                    //if this score is better than the current best score, update best score and best move
                    if (score > bestScore) {
                        bestScore = score;
                        bestMove[0] = i;
                        bestMove[1] = j;
                        System.out.printf("Best move so far is [%d,%d] with score %d\n", i, j, bestScore);
                    }
                }
            }
        }

        return bestMove;
    }
    
    public int evaluateBoard(char[][] board) {
        int score = 0;

        //prefer boards where 'X' has more marks
        for (int i = 0; i < board.length; i++) {
            for (int j = 0; j < board[i].length; j++) {
                if (board[i][j] == 'X') {
                    score++;
                }
            }
        }

        return score;
    }
    
    @Override
    public int[] nextMove(SuperTicTacToe gs, char maxPlayer) {
        return getBestMove(gs.getBoard());
    }
    
}