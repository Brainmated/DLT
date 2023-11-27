import java.io.*;
import java.util.Scanner;

public class SuperTicTacToeAI {
	
	private File moveFile;
	private Scanner scanner;

	public SuperTicTacToeAI() {
		try {
			this.moveFile = new File("path_to_your_file");
			this.scanner = new Scanner(moveFile);
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		}
	}

	public int[] nextMove(SuperTicTacToe gs, char maxPlayer) {
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