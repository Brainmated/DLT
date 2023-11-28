public class AIGame extends SuperTicTacToe{
	private SuperTicTacToe game;
    private SuperTicTacToeAI greedy;
    private SuperTicTacToeAI minMax;


    public AIGame(SuperTicTacToe game, boolean againstHuman, boolean computerFirst) {
        super(againstHuman, computerFirst);  // Call to the SuperTicTacToe constructor
        this.game = game;
        this.greedy = new greedy(game);
        this.minMax = new minMax(game);
    }

    public void compete() {
        char currentTurn = 'X'; // Assume 'X' is the first player

        while (!game.isGameFinished()) {
            int[] move;
            if (currentTurn == 'X') {
                move = greedy.nextMove(game, currentTurn);
                game.implementMove(move, currentTurn, game.getBoard());
                currentTurn = 'O';
            } else {
                move = minMax.nextMove(game, currentTurn);
                game.implementMove(move, currentTurn, game.getBoard());
                currentTurn = 'X';
            }
        }

        // After the game is over, print the board and the result
        game.printBoard(game.getBoard());
        if (game.getWinner() != ' ') {
            System.out.println("The winner is: " + game.getWinner());
        } else {
            System.out.println("The game ended in a tie.");
        }
    }

}
