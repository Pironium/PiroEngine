import java.util.ArrayList;
import java.util.List;

public class Renderer {
    private List<Renderable> renderables;
    private Shader shader;
    private Camera camera;

    public Renderer() {
        renderables = new ArrayList<>();
        shader = new Shader();
        camera = new Camera();
    }

    public void addRenderable(Renderable renderable) {
        renderables.add(renderable);
    }

    public void render() {
        shader.use();
        shader.setMat4("viewProjection", camera.getViewProjectionMatrix());

        for (Renderable renderable : renderables) {
            renderable.render();
        }
    }
}
