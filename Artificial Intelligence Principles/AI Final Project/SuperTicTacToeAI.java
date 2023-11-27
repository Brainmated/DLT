import java.io.*;
import java.util.Scanner;

public class SuperTicTacToeAI {
	
	private File moveFile;
	private Scanner scanner;

	public SuperTicTacToeAI() {
		try {
			this.moveFile = new File("D:\\Programming in Java\\logs\\");
			this.scanner = new Scanner(moveFile);
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		}
	}

	public int[] nextMove(SuperTicTacToe gs, char maxPlayer, int currMove) {
		String name = "D:\\Programming in Java\\logs\\" + currMove + ".txt";  // Specify the directory
		File moveFile = new File(name);
	    if (moveFile.exists()) {
	        System.out.println("File " + name + " exists.");
	    } else {
	        System.out.println("File " + name + " does not exist.");
	    }
		Scanner scanner = null;
		try {
			scanner = new Scanner(moveFile);
		} catch (FileNotFoundException e) {
			e.printStackTrace();
			// handle error here, for instance by returning a default move
			return new int[]{0, 0};
		}
		
		if (scanner.hasNextLine()) {
			String nextMove = scanner.nextLine();
			String[] coordinates = nextMove.split(","); // assuming you store coordinates as "x,y"
			
			int x = Integer.parseInt(coordinates[0]);
			int y = Integer.parseInt(coordinates[1]);
	
			int[] move = new int[]{x, y};
	
			if (gs.inActiveBoard(move) && gs.getBoard()[x][y] == SuperTicTacToe.SPACE) {
				return move;
			}
		}
	
		return new int[]{0, 0}; // Return default move if no valid move found in file
	}
}
