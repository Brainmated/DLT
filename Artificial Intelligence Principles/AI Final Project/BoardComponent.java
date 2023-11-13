import java.awt.Graphics;
import java.awt.Graphics2D;
import java.awt.Stroke;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;
import javax.imageio.ImageIO;
import javax.swing.JComponent;
import java.awt.geom.Ellipse2D;
import java.awt.geom.Line2D;
import java.awt.BasicStroke;
import java.awt.Color;
import java.awt.Font;

public class BoardComponent extends JComponent {

	private static final long serialVersionUID = 1L;
	
	private SuperTicTacToe gs;
	private int boardsize, squaresize, squareNo;
	private BufferedImage image, clock;
	private char[][] board;
	private int[] activeboard = {-1,-1};
	private int[] times = {0, 0};
	private int[] lastMove = {-1,-1};
	
	public BoardComponent(SuperTicTacToe gs)
	{
		this.gs = gs;
		this.boardsize = SuperTicTacToe.BOARDSIZE;
		this.squaresize = SuperTicTacToe.SQUARESIZE;
		this.squareNo = SuperTicTacToe.NOSQUARESXY;
		this.board = new char[boardsize][boardsize];
		try {
			image = ImageIO.read(new File("images/board.jpg"));
			clock = ImageIO.read(new File("images/clock.png"));
		} catch (IOException e) {
			e.printStackTrace();
			System.exit(-1);
		}		
	}
	
	public void updateBoard(SuperTicTacToe gs, int times[], int lastMove[])
	{
		this.board = gs.getBoard();
		this.activeboard = gs.getActiveBoard();
		this.times = times;
		this.lastMove = lastMove;
		repaint();
	}
	
	private void paintEligible(int x, int y, int size, Graphics2D g2)
	{
		Stroke oldStroke = g2.getStroke();
		g2.setStroke(new BasicStroke(7));

		g2.setColor(Color.GREEN);
		g2.drawRect(x+size/4, y+size/4, size/2, size/2);
		
		g2.setStroke(oldStroke);
	}
	
	private void paintaPiece(int x, int y, int size, boolean isP1, Graphics2D g2)
	{
		Stroke oldStroke = g2.getStroke();
		g2.setStroke(new BasicStroke(size/8));
		
		if (isP1)
		{
			g2.setColor(Color.WHITE);
			Line2D.Double line1 = new Line2D.Double(x+size/6, y+size/6, x+5*size/6, y+5*size/6);
			g2.draw(line1);
			Line2D.Double line2 = new Line2D.Double(x+size/6, y+5*size/6, x+5*size/6, y+size/6);
			g2.draw(line2);
			g2.setColor(Color.BLACK);
			g2.setStroke(new BasicStroke(size/12));
			g2.draw(line1);
			g2.draw(line2);
		}
		else
		{
			g2.setColor(Color.BLACK);
			Ellipse2D.Double circleOut = new Ellipse2D.Double(x+size/8, y+size/8, 3*size/4, 3*size/4);
			g2.draw(circleOut);
			g2.setColor(Color.WHITE);
			g2.setStroke(new BasicStroke(size/12));
			g2.draw(circleOut);
		}
		
		g2.setStroke(oldStroke);
	}	
	
	private void paintaPieceOnTop(int x, int y, int size, boolean isP1, float transparency, Graphics2D g2)
	{
		Stroke oldStroke = g2.getStroke();
		g2.setStroke(new BasicStroke(size/8));
		
		if (isP1)
		{
			g2.setColor(new Color(1.0f,1.0f,1.0f,transparency));
			Line2D.Double line1 = new Line2D.Double(x+size/6, y+size/6, x+5*size/6, y+5*size/6);
			g2.draw(line1);
			Line2D.Double line2 = new Line2D.Double(x+size/6, y+5*size/6, x+5*size/6, y+size/6);
			g2.draw(line2);
			g2.setColor(new Color(0f,0f,0f,transparency));
			g2.setStroke(new BasicStroke(size/12));
			g2.draw(line1);
			g2.draw(line2);
		}
		else
		{
			g2.setColor(new Color(0f,0f,0f,transparency));
			Ellipse2D.Double circleOut = new Ellipse2D.Double(x+size/8, y+size/8, 3*size/4, 3*size/4);
			g2.draw(circleOut);
			g2.setColor(new Color(1.0f,1.0f,1.0f,transparency));
			g2.setStroke(new BasicStroke(size/12));
			g2.draw(circleOut);
		}
		
		g2.setStroke(oldStroke);
	}
	
	private String intToString(int x)
	{
		int x10 = x/10;
		x = x%10;
		return x10+""+x;
	}
	
	private String timeToString(int t)
	{
		return intToString(t/60)+":"+intToString(t%60);
	}
	
	public void paintComponent(Graphics g)
	{
		g.drawImage(image, 50, 50, null);
		
		int dy = (image.getHeight()+1)/boardsize;
		int dx = (image.getWidth()+1)/boardsize;
		
		int origX = 50 + (image.getWidth() - dx*boardsize +1)/2;
		int origY = 50 + (image.getHeight() - dy*boardsize +1)/2;
		
		Graphics2D g2 = (Graphics2D) g;
		
		// draw lines
		g2.setColor(Color.YELLOW);
		for (int i=0; i<=boardsize; i++)
		{
			g2.draw(new Line2D.Double(origX+i*dx, origY, origX+i*dx, origY+boardsize*dy));
			g2.draw(new Line2D.Double(origX, origY+i*dy, origX+boardsize*dx, origY+i*dy));
		}
		
		Stroke oldStroke = g2.getStroke();
		g2.setStroke(new BasicStroke(5));
		g2.setColor(Color.CYAN);
		for (int i=0; i<=squareNo; i++)
		{
			g2.draw(new Line2D.Double(origX+i*dx*squaresize, origY, origX+i*dx*squaresize, origY+boardsize*dy));
			g2.draw(new Line2D.Double(origX, origY+i*dy*squaresize, origX+boardsize*dx, origY+i*dy*squaresize));			
		}
		
		g2.setStroke(oldStroke);
		
		// print rows and columns
		g2.setColor(Color.BLUE);
		g2.setFont(new Font(null,Font.PLAIN, 300/boardsize));
		for (int i=1; i<=boardsize; i++)
		{
			char c = (char) ('a'+i-1);
			g2.drawString(c+"", 50+i*dx-3*dx/5, 40);
			g2.drawString(i+"", 50-230/boardsize, 50+i*dy-7*dy/20);			
		}
		
		// draw the pieces and count them
		boolean gameDone = gs.isGameFinished();
		int count1=0, count2=0;
		for (int y=0; y<boardsize; y++)
		{
			for (int x=0; x<boardsize; x++)
			{
				if (board[x][y]==SuperTicTacToe.P1) 
				{
					count1++;
					paintaPiece(50+x*dx, 50+y*dy, dx, true, g2);
				}
				if (board[x][y]==SuperTicTacToe.P2)
				{
					count2++;
					paintaPiece(50+x*dx, 50+y*dy, dx, false, g2);
				}
				if (board[x][y]==SuperTicTacToe.SPACE && !gameDone && gs.inActiveBoard(new int[] {x,y}))
					paintEligible(50+x*dx, 50+y*dy, dx, g2);
			}
		}
		
		// draw small boards won
		for (int y=0; y<squareNo; y++)
		{
			for (int x=0; x<squareNo; x++)
			{
				float points = gs.pointsWon(new int[] {x, y}, board);
				if (points>0.1f) 
				{
					paintaPieceOnTop(50+x*dx*squaresize, 50+y*dy*squaresize, dx*squaresize, true, 0.8f*points, g2);
				}
				if (points<-0.1f)
				{
					paintaPieceOnTop(50+x*dx*squaresize, 50+y*dy*squaresize, dx*squaresize, false, -0.8f*points, g2);
				}
			}
		}
		
		
		g.drawImage(clock, 900, 150, null);
		g.drawImage(clock, 900, 550, null);
		paintaPiece(900, 50, 100, true, g2);
		paintaPiece(900, 450, 100, false, g2);
		g2.setColor(Color.ORANGE);
		g2.setFont(new Font(null,Font.PLAIN, 40));
		g2.drawString(intToString(count1), 928, 115);
		g2.drawString(intToString(count2), 928, 515);
		g2.setColor(Color.RED);
		g2.drawString(timeToString(times[0]), 980, 350);
		g2.drawString(timeToString(times[1]), 980, 750);
		
		if (lastMove[0]+lastMove[1]>0)
			g2.drawString("*", origX+lastMove[0]*dx+dx/2-7, origY+lastMove[1]*dy+dy/2+20);
	}
}
