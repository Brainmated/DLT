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

	private SuperTicTacToe game;
    private char maxPlayer;

    public SuperTicTacToeAI(SuperTicTacToe game, char maxPlayer) {
        this.game = game;
        this.maxPlayer = maxPlayer;
    }
    private int[][] calculateHeuristic(SuperTicTacToe gs, char maxPlayer) {
        int[][] heuristic = new int[SuperTicTacToe.BOARDSIZE][SuperTicTacToe.BOARDSIZE];
        char[][] board = gs.getBoard();
        int[] activeboard = gs.getActiveBoard();

        // calculate heuristic
        for (int x=0; x<SuperTicTacToe.BOARDSIZE; x++) {
            for (int y=0; y<SuperTicTacToe.BOARDSIZE; y++) {
                if (gs.inActiveBoard(new int[] {x,y}) && board[x][y]==SuperTicTacToe.SPACE) {
                    if (x == SuperTicTacToe.BOARDSIZE/2 && y == SuperTicTacToe.BOARDSIZE/2) {
                        heuristic[x][y] += 10; // Favor the center
                    }
                }
            }
        }
        return heuristic;
    }
    
    public int[] nextMove(SuperTicTacToe gs, char maxPlayer) {
        char[][] board = gs.getBoard();
        int[][] heuristic = calculateHeuristic(gs, maxPlayer);

        int[] bestMove = new int[]{0,0};
        int bestScore = -1;

        for (int x=0; x<SuperTicTacToe.BOARDSIZE; x++) {
            for (int y=0; y<SuperTicTacToe.BOARDSIZE; y++) {
                if (gs.inActiveBoard(new int[] {x,y}) && board[x][y]==SuperTicTacToe.SPACE) {
                    if (heuristic[x][y] > bestScore) {
                        bestScore = heuristic[x][y];
                        bestMove = new int[]{x,y};
                    }
                }
            }
        }

        return bestMove;
    }
}
