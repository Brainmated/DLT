
/**
 * You should extend (inherit from) this class and implement your AI
 */
public class SuperTicTacToeAI {
	
	/**
	 * This method should return the coordinate of the next move (where to place next piece)
	 * NOTE: It just places in the next possible spot, using no strategy.
	 * @param gs The gamestate (i.e. the board, active small board etc)
	 * @param maxPlayer the char of the current (max) player - for whom you return the move
	 * @return coordinates as a int[2] array
	 */
	private SuperTicTacToe game;
    private char maxPlayer;

	public SuperTicTacToeAI(SuperTicTacToe game, char maxPlayer) {
        this.game = game;
        this.maxPlayer = maxPlayer;
    }
	
	public int[] nextMove(SuperTicTacToe gs, char maxPlayer)
{
    char[][] board = gs.getBoard();
    int[] activeboard = gs.getActiveBoard();

    // Greedy heuristic: Try to win, block opponent's win, or create an "open two".
    for (int x=0; x<SuperTicTacToe.BOARDSIZE; x++) {
        for (int y=0; y<SuperTicTacToe.BOARDSIZE; y++) {
            if (gs.inActiveBoard(new int[] {x,y}) && board[x][y]==SuperTicTacToe.SPACE) {
                // Check if this move would win the game for the AI.
                board[x][y] = maxPlayer;
                if (gs.isGameFinished()) {
                    board[x][y] = SuperTicTacToe.SPACE;  // undo move
                    return new int[]{x,y};
                }
                // Check if this move would block the human from winning.
                board[x][y] = (maxPlayer == SuperTicTacToe.P1) ? SuperTicTacToe.P2 : SuperTicTacToe.P1;
                if (gs.isGameFinished()) {
                    board[x][y] = SuperTicTacToe.SPACE;  // undo move
                    return new int[]{x,y};
                }
                // Check for "open two" opportunities.
                // If an "open two" opportunity is found, return new int[]{x,y}.
				for (int dx=-1; dx<=1; dx++) {
					for (int dy=-1; dy<=1; dy++) {
						if (x+dx>=0 && x+dx<SuperTicTacToe.BOARDSIZE && y+dy>=0 && y+dy<SuperTicTacToe.BOARDSIZE &&
							x+2*dx>=0 && x+2*dx<SuperTicTacToe.BOARDSIZE && y+2*dy>=0 && y+2*dy<SuperTicTacToe.BOARDSIZE) {
							if (board[x+dx][y+dy] == maxPlayer && board[x+2*dx][y+2*dy] == maxPlayer) {
								board[x][y] = SuperTicTacToe.SPACE;  // undo move
								return new int[]{x,y};
							}
						}
					}
				}

                board[x][y] = SuperTicTacToe.SPACE;  // undo move
            }
        }
    }

    // If no strategic move is found, just return the first available move.
    for (int x=0; x<SuperTicTacToe.BOARDSIZE; x++) {
        for (int y=0; y<SuperTicTacToe.BOARDSIZE; y++) {
            if (gs.inActiveBoard(new int[] {x,y}) && board[x][y]==SuperTicTacToe.SPACE) {
                return new int[]{x,y};
            }
        }
    }

    return new int[]{0,0}; // should not reach here
}
