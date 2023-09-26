public class GameObject
{
    private Vector3 position;
    private Mesh mesh;
    private Texture texture;

    public GameObject(Vector3 position, Mesh mesh, Texture texture)
    {
        this.position = position;
        this.mesh = mesh;
        this.texture = texture;
    }

    public void Render()
    {
        // Код для отрисовки объекта с учетом позиции, меша и текстуры
    }

    public void Update()
    {
        // Код для обновления состояния объекта, например, физика
    }
}
