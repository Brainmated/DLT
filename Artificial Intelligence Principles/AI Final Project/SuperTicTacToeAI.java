
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
	public int[] nextMove(SuperTicTacToe gs, char maxPlayer)
	{
		char[][] board = gs.getBoard();
		@SuppressWarnings("unused")
		int[] activeboard = gs.getActiveBoard();
		/*
		for (int y=0; y<SuperTicTacToe.BOARDSIZE; y++)
		{
			for (int x=0; x<SuperTicTacToe.BOARDSIZE; x++)
				System.out.print(board[x][y]);
			System.out.println();
		}
		System.out.println(Arrays.toString(activeboard));
		*/
		for (int x=0; x<SuperTicTacToe.BOARDSIZE; x++)
			for (int y=0; y<SuperTicTacToe.BOARDSIZE; y++)
				if (gs.inActiveBoard(new int[] {x,y}) && board[x][y]==SuperTicTacToe.SPACE)
					return new int[]{x,y};
		return new int[]{0,0}; // should not reach here
	}
}
