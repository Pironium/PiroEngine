#include <PiroEngine/Renderer.h>

// Код для рендеринга теней
void RenderShadows(const Scene& scene, const Light& light) {
    // Создаем фреймбуфер для генерации теней
    Framebuffer shadowMap;
    shadowMap.Initialize(light.GetShadowMapSize(), light.GetShadowMapSize());

    // Устанавливаем видовую и проекционную матрицы для генерации теней
    mat4 lightSpaceMatrix = light.CalculateLightSpaceMatrix();

    // Задаем шейдер для генерации теней
    Shader shadowShader("shaders/shadow.vs", "shaders/shadow.fs");
    shadowShader.Use();
    shadowShader.SetMat4("lightSpaceMatrix", lightSpaceMatrix);

    // Рендерим сцену во фреймбуфер
    shadowMap.Bind();
    glViewport(0, 0, light.GetShadowMapSize(), light.GetShadowMapSize());
    glClear(GL_DEPTH_BUFFER_BIT);
    
    for (const auto& object : scene.GetObjects()) {
        shadowShader.SetMat4("model", object.GetModelMatrix());
        object.Draw();
    }

    // Сохраняем теневую карту для использования в основном проходе рендеринга
    light.SetShadowMap(shadowMap.GetDepthTexture());
}
