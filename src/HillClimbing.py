import random
from Initialization import DeepCopy, compute_coverage, euclidean_distance_squared
from variables import R, height, width, radius, max_local_iteration, popSize, top_solutions
from Evaluation import evaluate

def update_coverage(coverage, x1, y1, x2, y2):
    rows, cols = len(coverage), len(coverage[0])

    # إزالة تأثير المستشعر القديم
    for i in range(max(0, x1 - radius), min(rows, x1 + radius + 1)):
        for j in range(max(0, y1 - radius), min(cols, y1 + radius + 1)):
            if euclidean_distance_squared(i, j, x1, y1) <= R:
                coverage[i][j] = max(0, coverage[i][j] - 1)

    # إضافة تأثير المستشعر الجديد
    for i in range(max(0, x2 - radius), min(rows, x2 + radius + 1)):
        for j in range(max(0, y2 - radius), min(cols, y2 + radius + 1)):
            if euclidean_distance_squared(i, j, x2, y2) <= R:
                coverage[i][j] += 1

    return coverage

def hill_climbing(initial_solution, current_fitness):
    rows = height
    cols = width

    current = DeepCopy(initial_solution)
    current_coverage = compute_coverage(current)

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]

    for _ in range(max_local_iteration):
        candidate = DeepCopy(current)
        candidate_coverage = DeepCopy(current_coverage)

        # اختيار موقع عشوائي للبحث عن مستشعر
        start_x = random.randint(0, rows - 1)
        start_y = random.randint(0, cols - 1)

        found = False
        for i in range(rows * cols):
            idx = (start_x * cols + start_y + i) % (rows * cols)
            x = idx // cols
            y = idx % cols
            if candidate[x][y] == 1:
                found = True
                break

        if not found:
            continue

        improved = False
        for dx, dy in directions:
            best_in_direction = None
            best_fitness = current_fitness

            for step in range(1, 2 * radius + 1):
                nx = x + dx * step
                ny = y + dy * step

                if 0 <= nx < rows and 0 <= ny < cols:
                    if candidate_coverage[nx][ny] > 1:
                        mx = x - dx * step
                        my = y - dy * step
                    elif candidate_coverage[nx][ny] == 0:
                        mx = x + dx * step
                        my = y + dy * step
                    else:
                        continue

                    if 0 <= mx < rows and 0 <= my < cols and candidate[mx][my] == 0:
                        temp = DeepCopy(candidate)
                        temp_coverage = DeepCopy(candidate_coverage)
                        temp[x][y] = 0
                        temp[mx][my] = 1

                        temp_coverage = update_coverage(temp_coverage, x, y, mx, my)
                        new_fitness = evaluate(temp, temp_coverage)

                        if new_fitness > best_fitness:
                            best_in_direction = (mx, my)
                            best_fitness = new_fitness
                        else:
                            break  # توقف عند أول فشل بعد تحسن

            if best_in_direction:
                mx, my = best_in_direction
                candidate[x][y] = 0
                candidate[mx][my] = 1
                candidate_coverage = update_coverage(candidate_coverage, x, y, mx, my)
                candidate_fitness = evaluate(candidate, candidate_coverage)

                if candidate_fitness >= current_fitness*0.99:
                    current = candidate
                    current_coverage = candidate_coverage
                    current_fitness = candidate_fitness
                    improved = True

    return current, current_fitness

def apply_local_search(population, fitnessList):
    offspring = []
    limit = int(popSize * top_solutions)

    for i in range(limit):
        improved_solution, improved_fitness = hill_climbing(population[i], fitnessList[i])
        offspring.append(improved_solution)
        fitnessList[i] = improved_fitness

    offspring.extend(population[limit:])
    return offspring, fitnessList

