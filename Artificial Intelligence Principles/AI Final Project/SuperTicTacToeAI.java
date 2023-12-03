
/**
 * You should extend (inherit from) this class and implement your AI
 * @author Ioannis A. Vetsikas
 *
 */
public class SuperTicTacToeAI {
	
	/**
	 * This method should return the coordinate of the next move (where to place next piece)
	 * NOTE: It just places in the next possible spot, using no strategy.
	 * --- STUDENTS SHOULD INHERIT FROM THIS CLASS AND BUILD THEIR OWN AIS ---
	 * @param gs The gamestate (i.e. the board, active small board etc)
	 * @param maxPlayer the char of the current (max) player - for whom you return the move
	 * @return coordinates as a int[2] array
	 */
	public int[] nextMove(SuperTicTacToe gs, char maxPlayer)
	{
		char[][] board = gs.getBoard();
		@SuppressWarnings("unused")
		int[] activeboard = gs.getActiveBoard();

		for (int x=0; x<SuperTicTacToe.BOARDSIZE; x++)
			for (int y=0; y<SuperTicTacToe.BOARDSIZE; y++)
				if (gs.inActiveBoard(new int[] {x,y}) && board[x][y]==SuperTicTacToe.SPACE)
					return new int[]{x,y};
		return new int[]{0,0}; // should not reach here
	}
	
	/**
	 * Creates a deep copy of the game board.
	 * @param original The original board to copy.
	 * @return A new copy of the board.
	 */
	public char[][] copyBoard(char[][] original) {
	    char[][] copy = new char[original.length][];
	    for (int i = 0; i < original.length; i++) {
	        copy[i] = original[i].clone();
	    }
	    return copy;
	}
}