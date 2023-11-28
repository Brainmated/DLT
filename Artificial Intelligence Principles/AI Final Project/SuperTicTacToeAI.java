public class SuperTicTacToeAI {

    private int[] calculateHeuristic(SuperTicTacToe gs, char maxPlayer) {
        int[][] heuristic = new int[SuperTicTacToe.BOARDSIZE][SuperTicTacToe.BOARDSIZE];
        char[][] board = gs.getBoard();
        int[] activeboard = gs.getActiveBoard();

        // calculate heuristic
        for (int x=0; x<SuperTicTacToe.BOARDSIZE; x++) {
            for (int y=0; y<SuperTicTacToe.BOARDSIZE; y++) {
                if (gs.inActiveBoard(new int[] {x,y}) && board[x][y]==SuperTicTacToe.SPACE) {
                    if (gs.wouldWin(maxPlayer, new int[] {x,y})) {
                        heuristic[x][y]+=100;
                    } else if (gs.wouldWin(gs.getOpponent(maxPlayer), new int[] {x,y})) {
                        heuristic[x][y]+=90;
                    }

                    if (x == SuperTicTacToe.BOARDSIZE/2 && y == SuperTicTacToe.BOARDSIZE/2) {
                        heuristic[x][y] += 10; // Favor the center
                    }

                    if (gs.wouldEnableMoreBoards(new int[] {x,y})) {
                        heuristic[x][y] += 5; // Favor moves that give more options for the next move
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