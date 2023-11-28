public class MinMax extends SuperTicTacToeAI {

    private SuperTicTacToe game;
    final char aiPlayer = 'X';
    final char humanPlayer = 'O';

    public MinMax(SuperTicTacToe game) {
        this.game = game;
    }

    public int[] getBestMove(char[][] board) {
        int bestScore = Integer.MIN_VALUE;
        int[] bestMove = new int[2];

        for (int i = 0; i < board.length; i++) {
            for (int j = 0; j < board[i].length; j++) {
                if (game.checkMoveValidity(new int[] {i, j}, aiPlayer, board)) {
                    char[][] copy = copyBoard(board);
                    copy[i][j] = aiPlayer;
                    int score = minimax(copy, 0, false, Integer.MIN_VALUE, Integer.MAX_VALUE);

                    if (score > bestScore) {
                        bestScore = score;
                        bestMove[0] = i;
                        bestMove[1] = j;
                    }
                }
            }
        }

        return bestMove;
    }

    public int minimax(char[][] board, int depth, boolean isMaximizing, int alpha, int beta) {
        char winner = game.checkWinner(board);

        if (winner != '\0') {
            return score(winner);
        }

        if (isMaximizing) {
            int bestScore = Integer.MIN_VALUE;
            for (int i = 0; i < board.length; i++) {
                for (int j = 0; j < board[i].length; j++) {
                    if (board[i][j] == '\0') {
                        board[i][j] = aiPlayer;
                        int score = minimax(board, depth + 1, false, alpha, beta);
                        board[i][j] = '\0';
                        bestScore = Math.max(score, bestScore);
                        alpha = Math.max(alpha, score);

                        if (beta <= alpha) {
                            return bestScore;
                        }
                    }
                }
            }
            return bestScore;
        } else {
            int bestScore = Integer.MAX_VALUE;
            for (int i = 0; i < board.length; i++) {
                for (int j = 0; j < board[i].length; j++) {
                    if (board[i][j] == '\0') {
                        board[i][j] = humanPlayer;
                        int score = minimax(board, depth + 1, true, alpha, beta);
                        board[i][j] = '\0';
                        bestScore = Math.min(score, bestScore);
                        beta = Math.min(beta, score);

                        if (beta <= alpha) {
                            return bestScore;
                        }
                    }
                }
            }
            return bestScore;
        }
    }

    public int score(char winner) {
        if (winner == aiPlayer) {
            return 1;
        } else if (winner == humanPlayer) {
            return -1;
        } else {
            return 0;
        }
    }

    @Override
    public int[] nextMove(SuperTicTacToe gs, char maxPlayer) {
        return getBestMove(gs.getBoard());
    }
}