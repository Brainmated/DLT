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
	public int[] nextMove(SuperTicTacToe gs, char maxPlayer) {
		char[][] board = gs.getBoard();
		int[] activeboard = gs.getActiveBoard();
	
		int bestScore = Integer.MIN_VALUE;
		int[] bestMove = null;
	
		for (int x = 0; x < SuperTicTacToe.BOARDSIZE; x++)
			for (int y = 0; y < SuperTicTacToe.BOARDSIZE; y++)
				if (gs.inActiveBoard(new int[] {x,y}) && board[x][y] == SuperTicTacToe.SPACE) {
					board[x][y] = maxPlayer;  // Make the move on the board
					int score = evaluateBoard(gs, maxPlayer);  // Evaluate the board
					board[x][y] = SuperTicTacToe.SPACE;  // Undo the move
	
					if (score > bestScore) {  // If this move is better than the current best, update bestScore and bestMove
						bestScore = score;
						bestMove = new int[]{x,y};
					}
				}
		
		if (bestMove == null) 
			return new int[]{0,0};  // If no move could be found (should not happen), return default move
	
		return bestMove;  // Return the best move found
	}
}
