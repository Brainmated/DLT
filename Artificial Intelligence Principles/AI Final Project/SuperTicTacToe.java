import java.io.File;
import java.io.FileNotFoundException;
import java.io.PrintWriter;
import java.util.Arrays;
import java.util.InputMismatchException;
import java.util.Scanner;

import javax.swing.JFrame;
import javax.swing.WindowConstants;

/**
 * This class has the main and also provided all the functionality to play the game
 * @author Ioannis A. Vetsikass
 *
 */

public class SuperTicTacToe {
	public static final int BOARDSIZE = 9;  // don't change this - whole board size
	public static final int SQUARESIZE = 3; // don't change this - small board size (should be sqroot of BOARDSIZE for code to work correctly!)
	public static final int NOSQUARESXY= BOARDSIZE/SQUARESIZE; // how many squares there are in each direction
	
	public static final char P1 = 'X'; // symbol of first player
	public static final char P2 = 'O'; // symbol of second player
	public static final char SPACE = '.'; // empty space
	public static final char ELIGIBLE = '*'; // use this to print all eligible spots where can play
		
	public static final float EPS = 0.000001f; // to check for whether something is zero
	
	private boolean againstHuman;
	private boolean computerFirstPlayer;
	private SuperTicTacToeAI myAI;
	
	private char boardState[][];
	private int lastActiveBoardX, lastActiveBoardY; // boards are numbered x,y in [0,NOSQUARESXY-1] // -1,-1 if all are active
	private BoardComponent boardcomp;
	
	/**
	 * Constructor
	 * @param againstHuman true if the opponent is human
	 * @param computerFirst is computer the first player
	 */
	public SuperTicTacToe(boolean againstHuman, boolean computerFirst)
	{
		this.againstHuman = againstHuman;
		System.out.println("Playing against a human:"+againstHuman);
		this.computerFirstPlayer = computerFirst;
		System.out.println("Computer is: "+(computerFirst?P1:P2));
		this.myAI = new SuperTicTacToeAI(); //new MMAB();
		// init
		boardState = new char[BOARDSIZE][BOARDSIZE];
		lastActiveBoardX = lastActiveBoardY = (NOSQUARESXY-1)/2; // active board in the middle initially
		initializeBoard(boardState);
	}
	
	private void initBoardFromStrings(String[] boardConfig)
	{
		for (int y=0; y<BOARDSIZE; y++)
			for (int x=0; x<BOARDSIZE; x++)
				boardState[x][y] = boardConfig[y].charAt(x);
	}
	
	/**
	 * Initializes the board to have black / white at the four corners
	 * @param board 2D array of the board
	 */
	private void initializeBoard(char board[][])
	{
		for (int x=0; x<BOARDSIZE; x++)
			for (int y=0; y<BOARDSIZE; y++)
				board[x][y] = SPACE;
		lastActiveBoardX = lastActiveBoardY = 1;
		// this code is for testing purposes - you can ignore it
		/*
		String[] initStateForTesting = new String[] {
				"OXXOXOXXO",
				"XO.O..XOO",
				"..OXO.X.X",
				"XOOXXX...",
				"O.X.....X",
				"......OXO",
				"OOO..O.OX",
				".....O.O.",
				"X...XOXXX"
		};
		initBoardFromStrings(initStateForTesting);
		*/
		
		//board[3][3]=P2;  lastActiveBoardX = lastActiveBoardY = 0;
		/*
		// test code for squares
		board[0][0]=P2;		board[1][0]=P1;		board[2][0]=P2;
		board[0][1]=P1;		board[1][1]=P1;		board[2][1]=P2;
		board[0][2]=P2;		board[1][2]=P2;		board[2][2]=P1;
		board[0][3]=P2;		board[0][6]=P2;
		board[0][4]=P2;		board[0][7]=P2;
		board[0][5]=P2;
		//System.out.println(pointsWon(new int[] {0,0}, board));
		*/
		//lastActiveBoardX = lastActiveBoardY = 1;
		//System.out.println(inActiveBoard(new int[] {3,5}));
	}
	
	/**
	 * Create a deep copy of the board and return it
	 * @return copy of game board
	 */
	public char[][] getBoard()
	{
		char[][] boardCopy = new char[BOARDSIZE][BOARDSIZE];
		for (int i=0; i<BOARDSIZE; i++)
		{
			boardCopy[i] = Arrays.copyOf(boardState[i], BOARDSIZE);
		}
		return boardCopy;
	}
	
	/**
	 * Returns the active board (or -1,-1 if all are active)
	 * NOTE: these are (0,0) for the top left board, (1,0) for the next one on the right etc.
	 * @return coordinates of active board
	 */
	public int[] getActiveBoard()
	{
		//System.out.printf(":::%d,%d:::\n",lastActiveBoardX, lastActiveBoardY);
		return new int[] {lastActiveBoardX,lastActiveBoardY};
	}
	
	/**
	 * Prints the board
	 * @param board 2D array of the board
	 */
	public void printBoard(char board[][])
	{
		boolean gameDone = isGameFinished();
		System.out.print("Active Board: ");
		if (lastActiveBoardX<0 && lastActiveBoardY<0) System.out.println("ALL OPEN");
		else
			System.out.printf("%d,%d\n", lastActiveBoardX, lastActiveBoardY);
		System.out.print("\n  ");
		String s = "abcdefghijklmnopqrstuvwxyz".substring(0, BOARDSIZE);
		for (int x=0; x<BOARDSIZE; x++)
		{
			if (x%SQUARESIZE==0) System.out.print("|");
			System.out.print(s.charAt(x));
		}
		System.out.println("|");
		for (int y=0; y<BOARDSIZE; y++)
		{
			if (y%SQUARESIZE==0) System.out.println("  ---------------------------------------------".substring(0, 3+BOARDSIZE+BOARDSIZE/SQUARESIZE));
			System.out.printf("%2d",y+1);
			for (int x=0; x<BOARDSIZE; x++)
			{
				if (x%SQUARESIZE==0) System.out.print("|");
				if (board[x][y]==SPACE && !gameDone && inActiveBoard(new int[] {x,y}))
					System.out.printf("%c", ELIGIBLE);
				else
					System.out.printf("%c", board[x][y]);
			}
			System.out.println("|");
		}
		System.out.println("  ---------------------------------------------".substring(0, 3+BOARDSIZE+BOARDSIZE/SQUARESIZE));			
	}
	
	/**
	 * 
	 * @param move : the move as [a-i][1-9] (for BOARDSIZE=9)
	 * @return array of 2 ints (x,y coordinates on array) or null if error in parse (x,y in [0, BOARDSIZE-1])
	 */
	private int[] parseMove(String move)
	{
		if (move.length()<2 || move.length()>3)
			return null;
		int moves[] = new int[2];
		moves[0] = move.charAt(0)-'a';
		if (moves[0]<0 || moves[0]>BOARDSIZE-1) return null;
		try
		{
			moves[1] = Integer.parseInt(move.substring(1))-1;
		}
		catch (NumberFormatException e)
		{
			return null;
		}
		if (moves[1]<0 || moves[1]>BOARDSIZE-1) return null;
		return moves;
	}
	
	/**
	 * 
	 * @param move : array of 2 ints (x,y coordinates on array)
	 * @return the move as a string [a-g][1-8] (for BOARDSIZE=8)
	 */
	private String moveToString(int[] move)
	{
		char tempc = (char) (((byte)move[0])+'a');
		int tempi = move[1]+1;
		return tempc+""+tempi;
	}
	
	/**
	 * Saves the move to a file
	 * @param currMove : number of current move (used to generate the file name)
	 * @param moves : the current move as an array of 2 ints
	 */
	private void saveToFile(int currMove, int[] moves)
	{
		String name = currMove+".txt";
		PrintWriter out;
		try {
			out = new PrintWriter(name);
			out.println(moveToString(moves));
			out.close();
		} catch (FileNotFoundException e) {
			e.printStackTrace();
			System.exit(-1);
		}
	}

	/**
	 * Reads the opponent move from a file
	 * @param currMove : number of current move (used to generate the file name)
	 * @return the current move as an array of 2 ints
	 */
	private int[] readFromFile(int currMove)
	{
		String name = currMove+".txt";
		int move[] = null;
		while (move==null)
		{
			File inputFile = new File(name);
			while (!inputFile.exists())
			{
				try {
					Thread.sleep(100);
				} catch (InterruptedException e1) {
					e1.printStackTrace();
				}				
			}
			try {
				Scanner in2 = new Scanner(inputFile);
				move = parseMove(in2.nextLine());
				in2.close();
			} catch (FileNotFoundException e) {
				try {
					Thread.sleep(100);
				} catch (InterruptedException e1) {
					e1.printStackTrace();
				}				
			}
		}
		System.out.println("Read move from file: " + moveToString(move));
		return move;
	}
	
	/**
	 * This method is called to play a game against an AI or a human
	 */
	private void playGame()
	{
		Scanner in = new Scanner(System.in);
		int times[] = {0, 0};
		JFrame gui = new JFrame();
		boardcomp = new BoardComponent(this);
		gui.add(boardcomp);
		gui.setDefaultCloseOperation(WindowConstants.DISPOSE_ON_CLOSE);
		gui.setSize(1200, 910);
		gui.setTitle("SuperTicTacToe GUI Viewer");
		gui.setVisible(true);

		boardcomp.updateBoard(this,times, times);
		
		int currentMove = 1;
		char currentPiece = P1;
		
		boolean computerNextMove = computerFirstPlayer;
		
		while (!isGameFinished())
		{
			printBoard(boardState);
			
			if (computerNextMove)
			{
				//computer selects a move
				long time0 = System.currentTimeMillis();
				int move[] = myAI.nextMove(this, currentPiece);
				times[(currentMove+1)%2] = (int)(System.currentTimeMillis()-time0+500)/1000;
				implementMove(move, currentPiece, boardState);
				boardcomp.updateBoard(this,times,move);
				System.out.println("my next move is: "+moveToString(move));
				if (!againstHuman)
				{
					// save to file
					saveToFile(currentMove, move);
				}
			}
			else
			{
				if (againstHuman)
				{
					boolean moveIsValid = false;
					int move[]={0,0};
					while (!moveIsValid)
					{
						System.out.print("Enter a move:");
						if (in.hasNext())
						{
							move = parseMove(in.next());
						}
						if (move!=null)
						{
							moveIsValid = checkMoveValidity(move, currentPiece, boardState);
						}
					}
					implementMove(move, currentPiece, boardState);
					boardcomp.updateBoard(this,times,move);
				}
				else
				{
					// read opponent move from file
					int move[] = readFromFile(currentMove);
					implementMove(move, currentPiece, boardState);
					boardcomp.updateBoard(this,times,move);
				}
			}
			
			computerNextMove = !computerNextMove;
			if (currentPiece==P1)
				currentPiece=P2;
			else
				currentPiece=P1;
			currentMove++;
		}
				
		System.out.println("\n-----------\nFINAL BOARD\n-----------");
		printBoard(boardState);
		in.close();
	}

	/**
	 * Used to just view the game from files! 
	 */
	private void viewGame()
	{
		char boardState[][] = new char[BOARDSIZE][BOARDSIZE];
		initializeBoard(boardState);
		int times[] = {0, 0};
		JFrame gui = new JFrame();
		boardcomp = new BoardComponent(this);
		gui.add(boardcomp);
		gui.setDefaultCloseOperation(WindowConstants.DISPOSE_ON_CLOSE);
		gui.setSize(1200, 910);
		gui.setTitle("SuperTicTacToe GUI Viewer");
		gui.setVisible(true);
		boardcomp.updateBoard(this,times,times);
		int currentMove = 1;
		char currentPiece = P1;

		long timePrev = System.currentTimeMillis();
		while (true)
		{
			int move[] = readFromFile(currentMove);
			if (checkMoveValidity(move, currentPiece, boardState))
				System.err.println("MOVE "+currentMove+"("+currentPiece+") is not valid!");
			implementMove(move, currentPiece, boardState);
			if (currentMove>2)
			{
				times[(currentMove+1)%2] += (System.currentTimeMillis()-timePrev)/1000+1;
			}
			timePrev = System.currentTimeMillis();
			boardcomp.updateBoard(this,times,move);
	
			if (currentPiece==P1)
				currentPiece=P2;
			else
				currentPiece=P1;
			currentMove++;
		}
	}
	
	/**
	 * Returns the points won (from perspective of P1, so negative if P2 has won it)
	 * @param squareCoords coordinates of small board (square)
	 * @param board the board of all the pieces
	 * @return -1, -0.5 (P2 wins full/half victory), 1, 0.5 (same for P1), 0 (board still open) - special case (for even size - split board returns -0.01f)
	 */
	public float pointsWon(int[] squareCoords, char[][] board)
	{
		// compute coordinates
		int x1, x2, y1, y2;
		x1=squareCoords[0]*SQUARESIZE;
		x2=x1+SQUARESIZE-1;
		y1=squareCoords[1]*SQUARESIZE;
		y2=y1+SQUARESIZE-1;
		
		// compute if board has a whole row
		for (int y=y1; y<=y2; y++)
		{
			char c = board[x1][y];
			for (int x=x1; x<=x2; x++)
				if (board[x][y]!=c)
				{
					c = SPACE; // not same
					break;
				}
			if (c==P1) return 1f;
			else if (c==P2) return -1f;
		}
		// compute if board has a whole column
		for (int x=x1; x<=x2; x++)
		{
			char c = board[x][y1];
			for (int y=y1; y<=y2; y++)
				if (board[x][y]!=c)
				{
					c = SPACE; // not same
					break;
				}
			if (c==P1) return 1f;
			else if (c==P2) return -1f;
		}
		// compute main diagonal
		char c = board[x1][y1];
		for (int i=0; i<=SQUARESIZE-1; i++)
			if (board[x1+i][y1+i]!=c)
			{
				c = SPACE; // not same
				break;
			}
		if (c==P1) return 1f;
		else if (c==P2) return -1f;
		// compute other diagonal
		c = board[x1][y2];
		for (int i=0; i<=SQUARESIZE-1; i++)
			if (board[x1+i][y2-i]!=c)
			{
				c = SPACE; // not same
				break;
			}
		if (c==P1) return 1f;
		else if (c==P2) return -1f;
		
		// check for half victory conditions (half+eps if full, or 2/3 if not full)
		int piecesNeededFull = SQUARESIZE*SQUARESIZE;
		int piecesNeededGen = piecesNeededFull*2/3;
		piecesNeededFull = (piecesNeededFull+1)/2;
		int count1=0, count2=0, count0=0;
		for (int y=y1; y<=y2; y++)
			for (int x=x1; x<=x2; x++)
				if (board[x][y]==P1) count1++;
				else if (board[x][y]==P2) count2++;
				else count0++;
		if (count0>0)
		{	// not full
			if (count1>=piecesNeededGen) return 0.5f;
			else if (count2>=piecesNeededGen) return -0.5f;
		}
		else
		{	// full
			if (count1>=piecesNeededFull) return 0.5f;
			else if (count2>=piecesNeededFull) return -0.5f;
			else return -0.01f; // this is in case of tie to indicate that the board does not belong to anyone (should not happen in a 9x9 game!)
		}
		// still open
		return 0f;
	}
	
	/**
	 * Checks if x is zero (within EPS), 
	 * @param x float to check
	 * @param epsilon tolerance
	 * @return |x| < epsilon
	 */
	public static boolean isZeroEps(float x, float epsilon)
	{
		return (x>-epsilon && x<epsilon);
	}
	
	/**
	 * Checks if a board is still open (if it's points ==0)
	 * @param coords coordinates of small board
	 * @return true if open (can still play there), false otherwise
	 */
	public boolean isBoardOpen(int[] coords)
	{
		float points = pointsWon(new int[] {coords[0],coords[1]}, boardState);
		if (!isZeroEps(points,EPS)) // points != 0 essentially (remember special case -0.01f closed but tied for even sizes)
			return false; // board is won
		else return true;
	}
	
	/**
	 * Is the point with coordinates given in the active board?
	 * Checks if board is closed (then board is not active)
	 * Then if all boards are active (then it's active for sure)
	 * Else checks if the coordinates are within unique active board
	 * EXTERNALITY: Uses lastActiveBoardX && lastActiveBoardY global variables
	 * @param coords coordinates of specific point on board
	 * @return true if points is active (so you can play on it) false otherwise
	 */
	public boolean inActiveBoard(int[] coords)
	{
		// check if board is closed (i.e. won)
		if (!isBoardOpen(new int[] {coords[0]/SQUARESIZE, coords[1]/SQUARESIZE})) // points != 0 essentially
			return false; // board is won
		// else
		if (lastActiveBoardX<0 && lastActiveBoardY<0) return true; // all boards active
		// only one board is active
		int x1, x2, y1, y2;
		x1=lastActiveBoardX*SQUARESIZE;
		x2=x1+SQUARESIZE-1;
		y1=lastActiveBoardY*SQUARESIZE;
		y2=y1+SQUARESIZE-1;
		if (coords[0]>=x1 && coords[0]<=x2 && coords[1]>=y1 && coords[1]<=y2) return true;
		return false;
	}
	
	/**
	 * Checks if the move is valid
	 * @param move array of 2 ints (x,y coordinates of move on table)
	 * @param c who's turn it is to play
	 * @param board the board of all the pieces
	 * @return true if move is valid, false otherwise
	 */
	public boolean checkMoveValidity(int[] move, char c, char[][] board) {
		int x = move[0];
		int y = move[1];
		if (board[x][y]!=SPACE) return false; // space is not empty
		if (!inActiveBoard(move)) return false; // not in active board 
		return true;
	}
	
	/**
	 * Plays the move - assumes it is valid (so you should have checked before hand!)
	 * It only checks that the position is empty (SPACE)
	 * Also updates the active board
	 * @param move array of 2 ints (x,y coordinates of move on table)
	 * @param c who's turn it is to play
	 * @param board the board of all the pieces 
	 */
	private void implementMove(int[] move, char c, char[][] board) {
		int x = move[0];
		int y = move[1];
		if (board[x][y]!=SPACE)
		{	// something went wrong
			System.err.printf("position %d,%d has char %c\n",x,y,board[x][y]);
			return;
		}
		board[x][y] = c;
		lastActiveBoardX = x%SQUARESIZE;
		lastActiveBoardY = y%SQUARESIZE;
		if (!isBoardOpen(new int[] {lastActiveBoardX, lastActiveBoardY}))
			lastActiveBoardX = lastActiveBoardY = -1;
	}
	
	/**
	 * Checks if the game is over: either one player has won 3 in a row or all small boards are closed 
	 * @param c who's turn it is to play
	 * @return true if game over, false if can still place pieces
	 */
	public boolean isGameFinished() {
		// create array of small boards
		float POINTSNEEDEDTOWIN = (NOSQUARESXY+1f)/2f;
		//System.out.println("Debug: POINTSNEEDEDTOWIN="+POINTSNEEDEDTOWIN);
		float[][] pointsBoard = new float[NOSQUARESXY][NOSQUARESXY];
		for (int x=0; x<NOSQUARESXY; x++)
		{
			for (int y=0; y<NOSQUARESXY; y++)
				pointsBoard[x][y] = pointsWon(new int[] {x, y}, boardState);
			//System.out.println(Arrays.toString(pointsBoard[x])); // prints transpose of points this way
		}
		// check for victory: all in a row
		for (int y=0; y<NOSQUARESXY; y++)
		{
			float sum = 0f;
			for (int x=0; x<NOSQUARESXY; x++)
			{
				sum += pointsBoard[x][y];
				if (isZeroEps(pointsBoard[x][y], 0.02f))
				{
					sum = 0f;
					break;
				}
			}
			if (sum>POINTSNEEDEDTOWIN-EPS)
			{
				System.out.println(">>>>P1 won row "+(y+1));
				return true;
			}
			else if (-sum>POINTSNEEDEDTOWIN-EPS)
			{
				System.out.println(">>>>P2 won row "+(y+1));
				return true;
			}
		}
		// check for victory: all in a column
		for (int x=0; x<NOSQUARESXY; x++)
		{
			float sum = 0f;
			for (int y=0; y<NOSQUARESXY; y++)
			{
				sum += pointsBoard[x][y];
				if (isZeroEps(pointsBoard[x][y], 0.02f))
				{
					sum = 0f;
					break;
				}
			}
			if (sum>POINTSNEEDEDTOWIN-EPS)
			{
				System.out.println(">>>>P1 won column "+(x+1));
				return true;
			}
			else if (-sum>POINTSNEEDEDTOWIN-EPS)
			{
				System.out.println(">>>>P2 won column "+(x+1));
				return true;
			}
		}
		// check for victory: all in main diag
		float sum = 0f;
		for (int i=0; i<NOSQUARESXY; i++)
		{
			sum += pointsBoard[i][i];
			if (isZeroEps(pointsBoard[i][i], 0.02f))
			{
				sum = 0f;
				break;
			}
		}
		if (sum>POINTSNEEDEDTOWIN-EPS)
		{
			System.out.println(">>>>P1 won main diag");
			return true;
		}
		else if (-sum>POINTSNEEDEDTOWIN-EPS)
		{
			System.out.println(">>>>P2 won main diag");
			return true;
		}
		// check for victory: all in off diag
		sum = 0f;
		for (int i=0; i<NOSQUARESXY; i++)
		{
			sum += pointsBoard[i][NOSQUARESXY-1-i];
			if (isZeroEps(pointsBoard[i][NOSQUARESXY-1-i], 0.02f))
			{
				sum = 0f;
				break;
			}
		}
		if (sum>POINTSNEEDEDTOWIN-EPS)
		{
			System.out.println(">>>>P1 won off diag");
			return true;
		}
		else if (-sum>POINTSNEEDEDTOWIN-EPS)
		{
			System.out.println(">>>>P2 won off diag");
			return true;
		}
		// --- check other secondary conditions : points + boards
		int count1=0, count2=0;
		for (int x=0; x<NOSQUARESXY; x++)
			for (int y=0; y<NOSQUARESXY; y++)
				if (pointsBoard[x][y]>EPS) count1++;
				else if (pointsBoard[x][y]<-EPS) count2++;
				else return false; // board is still open
		// --- check other secondary conditions : total points
		sum = 0f;
		for (int x=0; x<NOSQUARESXY; x++)
			for (int y=0; y<NOSQUARESXY; y++)
				sum += pointsBoard[x][y];
		if (sum>0.4f)
		{
			System.out.println(">>>>P1 won on points diff: " + (sum));
			return true;
		}
		else if (sum<-0.4f)
		{
			System.out.println(">>>>P2 won on points diff: " + (-sum));
			return true;
		}
		// --- check other secondary conditions : boards won
		if (count1>count2)
		{
			System.out.println(">>>>P1 won on small boards won diff: " + (count1-count2));
			return true;
		}
		else if (count2>count1)
		{
			System.out.println(">>>>P2 won on small boards won diff: " + (count2-count1));
			return true;
		}
		else
		{
			System.out.println("GAME OVER: TIE");
			return true;
		}
	}

	/**
	 * Main method reads args and plays game or tournament
	 * @param args arg should be 1-4 or V
	 * 			1. Play against human, computer is black
	 * 			2. Play against human, computer is white
	 * 			3. Play using files, this computer is black
	 * 			4. Play using files, this computer is white
	 *          V. View game (not implemented now)
	 */
	public static void main(String[] args) {
		int choice=-1;
		Scanner in = new Scanner(System.in);
		if (args.length>0)
		{
			if (args[0].charAt(0)=='V' || args[0].charAt(0)=='v')
			{
				choice=0;
			}
			else
			{
				try
				{
					choice = Integer.parseInt(args[0]);
				}
				catch (NumberFormatException e)
				{
					choice=-1;
				}
			}
		}
		if (choice<0 || choice>4)
		{
			System.out.println("1. Play against human, computer is black");
			System.out.println("2. Play against human, computer is white");
			System.out.println("3. Play using files, this computer is black");
			System.out.println("4. Play using files, this computer is white");
			while (choice <1 || choice > 4)
			{
				System.out.print("Make a choice:");
				try 
				{
					choice = in.nextInt();
				}
				catch (InputMismatchException e)
				{
					in.next();
					choice = -1;
				}
			}
		}	

		SuperTicTacToe player;
		switch (choice)
		{
			case 0:	// only reachable if given v or V as a command line argument
				player = new SuperTicTacToe(false, false);
				player.viewGame();
				break;
			case 1:
				player = new SuperTicTacToe(true, true);
				player.playGame();
				break;
			case 2:
				player = new SuperTicTacToe(true, false);
				player.playGame();
				break;
			case 3:
				player = new SuperTicTacToe(false, true);
				player.playGame();
				break;
			case 4:
				player = new SuperTicTacToe(false, false);
				player.playGame();
				break;
			default:
				System.exit(0);	
		}

		
		in.close();

	}

}
