#include <vector>
#include <unordered_map>

// Класс для хранения вершинных данных
class VertexData {
public:
    // Конструктор
    VertexData(float x, float y, float z) : x_(x), y_(y), z_(z) {}

    // Геттеры для координат
    float getX() const { return x_; }
    float getY() const { return y_; }
    float getZ() const { return z_; }

private:
    float x_, y_, z_;
};

// Класс для кеширования вершинных данных
class VertexCacheOptimizer {
public:
    // Конструктор
    VertexCacheOptimizer() {}

    // Оптимизировать вершинные данные
    std::vector<VertexData> optimize(std::vector<VertexData>& vertices) {
        std::vector<VertexData> optimizedVertices;
        std::unordered_map<VertexData, size_t> cache;
        
        for (const VertexData& vertex : vertices) {
            // Проверяем, есть ли вершина в кеше
            if (cache.find(vertex) != cache.end()) {
                // Используем вершину из кеша
                optimizedVertices.push_back(vertices[cache[vertex]]);
            } else {
                // Добавляем вершину в кеш и в оптимизированные данные
                cache[vertex] = optimizedVertices.size();
                optimizedVertices.push_back(vertex);
            }
        }
        
        return optimizedVertices;
    }
};

int main() {
    // Пример использования
    std::vector<VertexData> inputVertices = {
        VertexData(0.0f, 0.0f, 0.0f),
        VertexData(1.0f, 0.0f, 0.0f),
        VertexData(0.0f, 1.0f, 0.0f),
        VertexData(1.0f, 1.0f, 0.0f),
        // Допустим, здесь есть много других вершин
    };

    VertexCacheOptimizer optimizer;
    std::vector<VertexData> optimizedVertices = optimizer.optimize(inputVertices);

    // Теперь optimizedVertices содержит оптимизированные данные
    return 0;
}
