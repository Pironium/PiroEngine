#include "PiroRenderer.h"
#include "PiroShader.h"
#include "PiroMesh.h"

PiroRenderer::PiroRenderer()
{
    // Инициализация графической подсистемы и создание окна
    InitializeGraphics();

    // Загрузка шейдеров
    m_shader = new PiroShader("shaders/vertex.glsl", "shaders/fragment.glsl");

    // Создание камеры
    m_camera = new PiroCamera();
}

PiroRenderer::~PiroRenderer()
{
    delete m_shader;
    delete m_camera;
    // Освобождение ресурсов и завершение графической подсистемы
    TerminateGraphics();
}

void PiroRenderer::Render(PiroMesh* mesh)
{
    // Активация шейдера
    m_shader->Use();

    // Установка матрицы проекции и вида из камеры
    m_shader->SetMatrix4("projection", m_camera->GetProjectionMatrix());
    m_shader->SetMatrix4("view", m_camera->GetViewMatrix());

    // Установка позиции камеры
    m_shader->SetVector3("viewPosition", m_camera->GetPosition());

    // Установка модельной матрицы
    m_shader->SetMatrix4("model", mesh->GetModelMatrix());

    // Рендеринг меша
    mesh->Render();
}

void PiroRenderer::SetCameraPosition(const glm::vec3& position)
{
    m_camera->SetPosition(position);
}

void PiroRenderer::SetCameraRotation(float pitch, float yaw)
{
    m_camera->SetRotation(pitch, yaw);
}

void PiroRenderer::InitializeGraphics()
{
    // Инициализация графической подсистемы (например, OpenGL)

    // Создание окна и контекста
    // ...

    // Инициализация рендеринга
    // ...
}

void PiroRenderer::TerminateGraphics()
{
    // Освобождение ресурсов и завершение графической подсистемы

    // Закрытие окна и освобождение контекста
    // ...

    // Деинициализация рендеринга
    // ...
}
