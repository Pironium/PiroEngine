#pragma once

#include "Graphics/Shader.h"
#include "Graphics/Texture.h"
#include "Graphics/Mesh.h"

class WaterEffect {
public:
    WaterEffect(int screenWidth, int screenHeight) {
        // Инициализация текстур и шейдера для водных эффектов
        waterShader = new Shader("Shaders/water_vertex.glsl", "Shaders/water_fragment.glsl");
        waterTexture = new Texture("Textures/water_normal.png");
        waterMesh = new Mesh("Models/water_plane.obj");

        // Остальная инициализация и настройка параметров водных эффектов
        // ...

        screenWidth_ = screenWidth;
        screenHeight_ = screenHeight;
    }

    ~WaterEffect() {
        delete waterShader;
        delete waterTexture;
        delete waterMesh;
    }

    void Update(float deltaTime) {
        // Обновление водных эффектов
        // ...

        // Применение шейдера
        waterShader->Use();

        // Отправка текстур и параметров шейдера
        waterShader->SetTexture("normalMap", *waterTexture);
        // ...

        // Отрисовка водных эффектов
        waterMesh->Draw();
    }

private:
    Shader* waterShader;
    Texture* waterTexture;
    Mesh* waterMesh;
    int screenWidth_;
    int screenHeight_;
};
