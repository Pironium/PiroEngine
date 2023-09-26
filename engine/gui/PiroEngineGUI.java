// PiroEngineGUI.java

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class PiroEngineGUI {
    private JFrame frame;
    private JPanel mainPanel;
    private JButton createGameButton;
    private JButton openGameButton;
    private JTextArea gameListTextArea;

    public PiroEngineGUI() {
        frame = new JFrame("PiroEngine GUI");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(800, 600);

        mainPanel = new JPanel();
        mainPanel.setLayout(new BorderLayout());

        createGameButton = new JButton("Create New Game");
        openGameButton = new JButton("Open Existing Game");
        gameListTextArea = new JTextArea();

        createGameButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                // Add code here to create a new game project
                gameListTextArea.append("New game created!\n");
            }
        });

        openGameButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                // Add code here to open an existing game project
                gameListTextArea.append("Opening existing game...\n");
            }
        });

        mainPanel.add(createGameButton, BorderLayout.NORTH);
        mainPanel.add(openGameButton, BorderLayout.CENTER);
        mainPanel.add(new JScrollPane(gameListTextArea), BorderLayout.SOUTH);

        frame.getContentPane().add(mainPanel);
        frame.setVisible(true);
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(new Runnable() {
            @Override
            public void run() {
                new PiroEngineGUI();
            }
        });
    }
}
