import java.awt.*;
import javax.swing.*;

public class PiroEngineGUI {
    private JFrame mainFrame;
    private JPanel canvasPanel;
    private JButton renderButton;
    private JTextArea codeEditor;
    private JMenuBar menuBar;
    private JMenu fileMenu;
    private JMenuItem openMenuItem;
    private JMenuItem saveMenuItem;
    
    public PiroEngineGUI() {
        // Initialize the main frame
        mainFrame = new JFrame("PiroEngine GUI");
        mainFrame.setSize(800, 600);
        mainFrame.setLayout(new BorderLayout());
        mainFrame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        
        // Create a canvas panel for rendering
        canvasPanel = new JPanel();
        canvasPanel.setBackground(Color.BLACK);
        mainFrame.add(canvasPanel, BorderLayout.CENTER);
        
        // Create a button for rendering
        renderButton = new JButton("Render");
        mainFrame.add(renderButton, BorderLayout.SOUTH);
        
        // Create a code editor using JTextArea
        codeEditor = new JTextArea();
        codeEditor.setFont(new Font("Monospaced", Font.PLAIN, 14));
        JScrollPane codeScrollPane = new JScrollPane(codeEditor);
        mainFrame.add(codeScrollPane, BorderLayout.WEST);
        
        // Create a menu bar
        menuBar = new JMenuBar();
        mainFrame.setJMenuBar(menuBar);
        
        // Create a file menu
        fileMenu = new JMenu("File");
        menuBar.add(fileMenu);
        
        // Create open and save menu items
        openMenuItem = new JMenuItem("Open");
        saveMenuItem = new JMenuItem("Save");
        fileMenu.add(openMenuItem);
        fileMenu.add(saveMenuItem);
        
        // Display the main frame
        mainFrame.setVisible(true);
    }
    
    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            new PiroEngineGUI();
        });
    }
}
