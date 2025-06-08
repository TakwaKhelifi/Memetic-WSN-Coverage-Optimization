import random
from collections import deque
from variables import width, height, radius, estimated_sensors

RADIUS_SQUARED = radius * radius

def euclidean_distance_squared(x1, y1, x2, y2):
    return (x1 - x2)**2 + (y1 - y2)**2

# تُحسب مرة واحدة فقط
def generate_coverage_offsets():
    offsets = []
    for dy in range(-radius, radius + 1):
        for dx in range(-radius, radius + 1):
            if dx*dx + dy*dy <= RADIUS_SQUARED:
                offsets.append((dx, dy))
    return offsets

COVERAGE_OFFSETS = generate_coverage_offsets()

# بديل لـ deepcopy مخصص للمصفوفات الثنائية
def DeepCopy(matrix):
    return [row[:] for row in matrix]

def create_coverage_matrix():
    return [[0 for _ in range(width)] for _ in range(height)]

def compute_coverage(solution):
    coverage = create_coverage_matrix()
    for y in range(len(solution)):
        for x in range(len(solution[0])):
            if solution[y][x] == 1:
                for dx, dy in COVERAGE_OFFSETS:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < width and 0 <= ny < height:
                        coverage[ny][nx] += 1
    return coverage

def move_sensor_update_coverage(x, y, coverage):
    for dx, dy in COVERAGE_OFFSETS:
        nx, ny = x + dx, y + dy
        if 0 <= nx < width and 0 <= ny < height:
            coverage[ny][nx] += 1

def bfs_region(start_x, start_y, coverage, visited):
    region = []
    queue = deque()
    queue.append((start_x, start_y))
    visited[start_y][start_x] = True
    directions = [(1,0), (-1,0), (0,1), (0,-1)]

    while queue:
        x, y = queue.popleft()
        region.append((x, y))
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < width and 0 <= ny < height and not visited[ny][nx] and coverage[ny][nx] == 0:
                visited[ny][nx] = True
                queue.append((nx, ny))
    return region

def get_best_sensor_position(region, coverage):
    max_uncovered = 0
    best_pos = None

    for x, y in region:
        uncovered = 0
        for dx, dy in COVERAGE_OFFSETS:
            nx, ny = x + dx, y + dy
            if 0 <= nx < width and 0 <= ny < height and coverage[ny][nx] == 0:
                uncovered += 1
        if uncovered > max_uncovered:
            max_uncovered = uncovered
            best_pos = (x, y)
    return best_pos

def smart_add_sensors(solution, coverage):
    import math
    area_threshold = math.ceil(3.14 * radius**2 / 4)

    while True:
        visited = [[False for _ in range(width)] for _ in range(height)]
        added = False

        for y in range(height):
            for x in range(width):
                if not visited[y][x] and coverage[y][x] == 0:
                    region = bfs_region(x, y, coverage, visited)
                    if len(region) > area_threshold:
                        best = get_best_sensor_position(region, coverage)
                        if best:
                            bx, by = best
                            solution[by][bx] = 1
                            move_sensor_update_coverage(bx, by, coverage)
                            added = True
        if not added:
            break

def initialize_solution():
    solution = [[0 for _ in range(width)] for _ in range(height)]
    coverage = create_coverage_matrix()

    for _ in range(estimated_sensors):
        while True:
            x = random.randint(0, width - 1)
            y = random.randint(0, height - 1)
            if coverage[y][x] == 0:
                solution[y][x] = 1
                move_sensor_update_coverage(x, y, coverage)
                break

    smart_add_sensors(solution, coverage)
    return solution, coverage
