public class 3DModelRenderer {
    private Mesh3D mesh;
    private Shader3D shader;
    private Transform3D transform;

    public 3DModelRenderer(Mesh3D mesh, Shader3D shader, Transform3D transform) {
        this.mesh = mesh;
        this.shader = shader;
        this.transform = transform;
    }

    public void render(Camera3D camera) {
        shader.use();
        shader.setMat4("modelMatrix", transform.getModelMatrix());
        shader.setMat4("viewMatrix", camera.getViewMatrix());
        shader.setMat4("projectionMatrix", camera.getProjectionMatrix());

        mesh.draw();
    }
}
