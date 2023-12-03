public class minMax extends SuperTicTacToeAI {

    private SuperTicTacToe game;
    final char aiPlayer = 'O';
    final char humanPlayer = 'X';

    //constructor to initialize the game
    public minMax(SuperTicTacToe game) {
        this.game = game;
    }

    //function to get the best possible move for the AI player
    public int[] getBestMove(char[][] board) {
        int bestScore = Integer.MIN_VALUE;
        int[] bestMove = new int[2];

        //iterate over all squares on the board
        for (int i = 0; i < board.length; i++) {
            for (int j = 0; j < board[i].length; j++) {
                //check if the current move is valid
                if (game.checkMoveValidity(new int[] {i, j}, aiPlayer, board)) {
                    //make a copy of the board and apply the move
                    char[][] copy = copyBoard(board);
                    copy[i][j] = aiPlayer;
                    
                    //use the Minimax algorithm to find the score of the current move
                    int score = minimax(copy, 0, false, Integer.MIN_VALUE, Integer.MAX_VALUE);

                    //if the current score is better than the best score, update the best score and best move
                    if (score > bestScore) {
                        bestScore = score;
                        bestMove[0] = i;
                        bestMove[1] = j;
                    }
                }
            }
        }

        //return the best move
        return bestMove;
    }

    //the Minimax function, which also implements alpha-beta pruning
    public int minimax(char[][] board, int depth, boolean isMaximizing, int alpha, int beta) {
        //check if the game has ended
        if (game.isGameFinished()) {
            float sum = 0f;
            //calculate the total score
            for (int x = 0; x < game.NOSQUARESXY; x++) {
                for (int y = 0; y < game.NOSQUARESXY; y++) {
                    sum += game.pointsWon(new int[] {x, y}, board);
                }
            }

            //check who won and return the corresponding score
            if (sum > 0.4f) {
                return 1; //aI player won
            } else if (sum < -0.4f) {
                return -1; //minmax won
            } else {
                return 0; //tie
            }
        }

        //if it's the AI player's turn (Maximizing player)
        if (isMaximizing) {
            int bestScore = Integer.MIN_VALUE;
            
            //iterate over all squares on the board 
            for (int i = 0; i < board.length; i++) {
                for (int j = 0; j < board[i].length; j++) {
                    //check if the square is empty
                    if (board[i][j] == '\0') {
                        //try this move for the AI player
                        board[i][j] = aiPlayer;
                        
                        //call the Minimax function recursively and choose the maximum score
                        int score = minimax(board, depth + 1, false, alpha, beta);
                        board[i][j] = '\0';
                        bestScore = Math.max(score, bestScore);
                        alpha = Math.max(alpha, score);

                        //alpha Beta Pruning
                        if (beta <= alpha) {
                            return bestScore;
                        }
                    }
                }
            }
            return bestScore;

        //if it's the other player's turn (Minimizing player)
        } else {
            int bestScore = Integer.MAX_VALUE;
            
            //iterate over all squares on the board 
            for (int i = 0; i < board.length; i++) {
                for (int j = 0; j < board[i].length; j++) {
                    //check if the square is empty
                    if (board[i][j] == '\0') {
                        //try this move for the human player
                        board[i][j] = humanPlayer;
                        
                        //call the Minimax function recursively and choose the minimum score
                        int score = minimax(board, depth + 1, true, alpha, beta);
                        board[i][j] = '\0';
                        bestScore = Math.min(score, bestScore);
                        beta = Math.min(beta, score);

                        //alpha Beta Pruning
                        if (beta <= alpha) {
                            return bestScore;
                        }
                    }
                }
            }
            return bestScore;
        }
    }

    //override the nextMove function to use Minimax AI
    @Override
    public int[] nextMove(SuperTicTacToe gs, char maxPlayer) {
        return getBestMove(gs.getBoard());
    }
}