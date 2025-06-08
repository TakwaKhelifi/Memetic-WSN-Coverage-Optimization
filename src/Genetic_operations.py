import random
from Initialization import initialize_solution
from variables import width, height, mp, cp, popSize, good_solution

def crossover(solution1, solution2):

    crossover_point1 = random.randint(0, width - 1)
    crossover_point2 = random.randint(0, height - 1)

    for j in range(crossover_point2, height):
        for i in range(crossover_point1 if j == crossover_point2 else 0, width):
            solution1[j][i], solution2[j][i] = solution2[j][i], solution1[j][i]


    return solution1, solution2

def mutate(individual):
    total_cells = width * height
    start = random.randint(0, total_cells - 1)

    for offset in range(total_cells):
        idx = (start + offset) % total_cells
        row, col = divmod(idx, width)
        if individual[row][col] == 1:
            individual[row][col] = 0
            return individual

    return individual


def apply_GOs(population):
    """
    تطبيق التقاطع والطفرة على مجتمع الحلول.
    """
    offspring = []
    genetic_limit = int(popSize * good_solution)

    for i in range(0, popSize - 1, 2):
        if i < genetic_limit:
            if random.random() < cp:
                child1, child2 = crossover(population[i], population[i + 1])
            else:
                child1 = population[i]
                child2 = population[i + 1]

            if random.random() < mp:
                child1 = mutate(child1)
            if random.random() < mp:
                child2 = mutate(child2)

            offspring.append(child1)
            offspring.append(child2)
        else:
            new_sol1, _ = initialize_solution()
            new_sol2, _ = initialize_solution()
            offspring.append(new_sol1)
            offspring.append(new_sol2)


    if popSize % 2 != 0:
        new_sol, _ = initialize_solution()
        offspring.append(new_sol)

    return offspring
