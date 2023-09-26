import java.util.List;

public class RenderingEngine {
    private List<Renderable> renderables;
    
    public RenderingEngine() {
        this.renderables = new ArrayList<>();
    }
    
    public void addRenderable(Renderable renderable) {
        renderables.add(renderable);
    }
    
    public void render() {
        for (Renderable renderable : renderables) {
            renderable.render();
        }
    }
}
