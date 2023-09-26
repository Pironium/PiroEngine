import random

class GeneticOptimizer:
    def __init__(self, population_size, mutation_rate, fitness_function):
        self.population_size = population_size
        self.mutation_rate = mutation_rate
        self.fitness_function = fitness_function
        self.population = self.initialize_population()

    def initialize_population(self):
        population = []
        for _ in range(self.population_size):
            # Генерация случайных генотипов
            genotype = [random.uniform(0, 1) for _ in range(self.fitness_function.num_parameters)]
            population.append(genotype)
        return population

    def mutate(self, genotype):
        mutated_genotype = []
        for gene in genotype:
            if random.random() < self.mutation_rate:
                # Мутация гена
                mutated_gene = gene + random.uniform(-0.1, 0.1)
                mutated_gene = max(0, min(1, mutated_gene))  # Ограничение значений от 0 до 1
                mutated_genotype.append(mutated_gene)
            else:
                mutated_genotype.append(gene)
        return mutated_genotype

    def select_parents(self):
        # Выбор родителей на основе приспособленности
        parents = []
        for _ in range(2):
            fitness_values = [self.fitness_function(genotype) for genotype in self.population]
            total_fitness = sum(fitness_values)
            normalized_fitness = [f / total_fitness for f in fitness_values]
            parent_index = random.choices(range(self.population_size), weights=normalized_fitness)[0]
            parents.append(self.population[parent_index])
        return parents

    def crossover(self, parent1, parent2):
        # Скрещивание двух родителей
        crossover_point = random.randint(1, len(parent1) - 1)
        child_genotype = parent1[:crossover_point] + parent2[crossover_point:]
        return child_genotype

    def evolve(self, num_generations):
        for _ in range(num_generations):
            new_population = []
            for _ in range(self.population_size // 2):
                parent1, parent2 = self.select_parents()
                child1 = self.crossover(parent1, parent2)
                child2 = self.crossover(parent2, parent1)
                child1 = self.mutate(child1)
                child2 = self.mutate(child2)
                new_population.extend([child1, child2])
            self.population = new_population

# Пример использования
if __name__ == "__main__":
    def fitness_function(genotype):
        # Пример функции приспособленности (может быть заменена на любую другую)
        return sum(genotype)

    optimizer = GeneticOptimizer(population_size=100, mutation_rate=0.1, fitness_function=fitness_function)
    optimizer.evolve(num_generations=50)
    best_genotype = max(optimizer.population, key=fitness_function)
    print("Best Genotype:", best_genotype)
