/**
 * Greedy AI for Super Tic Tac Toe game.
 * This AI evaluates all possible moves and chooses the one that maximizes its own presence on the board.
 * It does not consider the opponent's potential moves.
 * 
 * @author Alexandros Synetos Konstantinidis
 */
public class Greedy extends SuperTicTacToeAI {

    private SuperTicTacToe game;  // The instance of the game this AI is playing
    final char aiPlayer = 'X';  // The character representing the AI player on the game board

    /**
     * Constructor that initializes the game instance this AI is playing.
     *
     * @param game the SuperTicTacToe game instance.
     */
    public Greedy(SuperTicTacToe game) {
        this.game = game;
    }

    /**
     * Evaluates all possible moves and returns the best one according to the evaluateBoard method.
     *
     * @param board the game board to evaluate.
     * @return the coordinates of the best move.
     */
    public int[] getBestMove(char[][] board) {
        int bestScore = Integer.MIN_VALUE;  // Initialize the best score to the lowest possible integer
        int[] bestMove = new int[2];  // Array to store the best move

        // Iterate over all cells of the board
        for (int i = 0; i < board.length; i++) {
            for (int j = 0; j < board[i].length; j++) {
                // If the move is valid
                if (game.checkMoveValidity(new int[] {i, j}, aiPlayer, board)) {
                    // Make a copy of the board
                    char[][] copy = copyBoard(board);
                    // Simulate a move on the copied board
                    copy[i][j] = aiPlayer; 
                    // Evaluate the board state after the move
                    int score = evaluateBoard(copy);

                    // If this score is better than the current best score, update best score and best move
                    if (score > bestScore) {
                        bestScore = score;
                        bestMove[0] = i;
                        bestMove[1] = j;
                    }
                }
            }
        }

        return bestMove;  // Return the best move found
    }

    /**
     * Evaluates a board state by counting the number of cells occupied by 'X'.
     *
     * @param board the game board to evaluate.
     * @return the score of the board.
     */
    public int evaluateBoard(char[][] board) {
        int score = 0;  // Initialize score

        // Iterate over all cells of the board
        for (int i = 0; i < board.length; i++) {
            for (int j = 0; j < board[i].length; j++) {
                // Increment score if cell is occupied by 'X'
                if (board[i][j] == 'X') {
                    score++;
                }
            }
        }

        return score;  // Return the final score
    }

    /**
     * Returns the next move this AI will make. 
     * Implements the required method from the SuperTicTacToeAI abstract class.
     *
     * @param gs the current game state.
     * @param maxPlayer the character representing the AI player on the board.
     * @return the coordinates of the next move.
     */
    @Override
    public int[] nextMove(SuperTicTacToe gs, char maxPlayer) {
        return getBestMove(gs.getBoard());
    }
}
