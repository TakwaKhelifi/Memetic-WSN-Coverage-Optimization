from variables import height, width, radius, alpha, beta, gamma
from Initialization import DeepCopy, euclidean_distance_squared
import variables



def find(node, parent):
    if parent[node] != node:
        parent[node] = find(parent[node], parent)
    return parent[node]

def union(node1, node2, parent):
    root1 = find(node1, parent)
    root2 = find(node2, parent)
    if root1 != root2:
        parent[root2] = root1

# التحقق من وجود مجموعات مستشعرات معزولة
def has_isolated_groups(solution):
    rows, cols = len(solution), len(solution[0])
    sensor_positions = [(i, j) for i in range(rows) for j in range(cols) if solution[i][j] == 1]

    if not sensor_positions:
        return False

    parent = {pos: pos for pos in sensor_positions}

    for i in range(len(sensor_positions)):
        for j in range(i + 1, len(sensor_positions)):
            x1, y1 = sensor_positions[i]
            x2, y2 = sensor_positions[j]
            if euclidean_distance_squared(x1, y1, x2, y2) <= (2*radius)**2:
                union((x1, y1), (x2, y2), parent)

    roots = set(find(pos, parent) for pos in sensor_positions)
    return len(roots) > 1

#def max_coverage(coverage):
 #   return max(max(row) for row in coverage)

# تقييم الحل
def evaluate(solution, coverage):
#    if retries > 10:
 #       raise ValueError("Too many retries in evaluate: still invalid solution.")
  #      return -100

   # if has_isolated_groups(solution) or max_coverage(coverage) > Cmax:
    #    print("Solution rejected")
     #   solution = initialize_solution()
      #  coverage = compute_coverage(solution)
       # return evaluate(solution, coverage, retries + 1)

    total_cells = height * width
    estimated_sensor_count = int((height * width) / (3.14 * radius * radius))

    covered_cells = 0
    overlap_cells = 0
    n_sensors = 0
    penalty = 0
    
    for i in range(height):
        for j in range(width):
            cov = coverage[i][j]
            sol = solution[i][j]
            if cov > 0:
                covered_cells += 1
            if cov > 1:
                overlap_cells += cov - 1
                if sol == 1:
                    penalty = 0.5
            if sol == 1:
                n_sensors += 1


    coverage_ratio = covered_cells / total_cells
    sensor_ratio = estimated_sensor_count / n_sensors if n_sensors > 0 else 0
    overlap_ratio = overlap_cells / covered_cells if covered_cells > 0 else 0

    fitness = alpha * coverage_ratio + beta * sensor_ratio + gamma * overlap_ratio - penalty 
    
    if fitness > variables.bestFitness :
        variables.bestFitness = fitness
        variables.bestCoverageRatio = coverage_ratio
        variables.bestSensorNumber = n_sensors
        variables.bestSolution = DeepCopy(solution)
        variables.bestCoverage = DeepCopy(coverage)

    return fitness

def sort_population_by_fitness(population, fitness):
    combined = list(zip(fitness, population))
    combined.sort(reverse=True, key=lambda x: x[0])  # الترتيب تنازلي حسب الـ fitness
    sorted_fitness, sorted_population = zip(*combined)
    return list(sorted_population), list(sorted_fitness)
