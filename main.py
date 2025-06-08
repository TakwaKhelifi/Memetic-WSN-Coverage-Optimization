import time
import csv

from src.variables import popSize, max_iteration, max_local_iteration, mp, cp, radius, width, height, estimated_sensors, alpha, beta, gamma
import src.variables
import src.Visualizer
from src.Initialization import initialize_solution, compute_coverage
from src.Evaluation import evaluate, sort_population_by_fitness
from src.Genetic_operations import apply_GOs
from src.HillClimbing import apply_local_search, hill_climbing
import os

base_folder = "results"
os.makedirs(base_folder, exist_ok=True)

def get_next_run_number():
    existing_folders = [
        name for name in os.listdir(base_folder)
        if os.path.isdir(os.path.join(base_folder, name)) and name.startswith("results")
    ]
    run_numbers = []
    for folder in existing_folders:
        name = folder.replace("results", "")
        if name.isdigit():
            run_numbers.append(int(name))
    return max(run_numbers, default=0) + 1

run_number = get_next_run_number()

# مجلد نتائج جديد
results_folder = os.path.join(base_folder, f"results{run_number}")
os.makedirs(results_folder, exist_ok=True)

# المسارات الكاملة للملفات
results_file = os.path.join(results_folder, "results.csv")
settings_file = os.path.join(results_folder, "settings.txt")
coverage_file = os.path.join(results_folder, "Coverage.csv")
solution_file = os.path.join(results_folder, "Solution.csv")



# بدء توقيت التنفيذ
start_time = time.time()
# إنشاء المجتمع الأولي
population = []
fitness_list = []
for _ in range(popSize):
    solution, coverage = initialize_solution()
    fitness = evaluate(solution, coverage)
    population.append(solution)
    fitness_list.append(fitness)

# حفظ معلمات التشغيل في ملف نصي
with open(settings_file, mode='w') as f:
    f.write(f"Population Size: {popSize}\n")
    f.write(f"Max Iterations: {max_iteration}\n")
    f.write(f"max local iteration: {max_local_iteration}\n")
    f.write(f"cp: {cp}\n")
    f.write(f"mp: {mp}\n")
    f.write(f"radius: {radius}\n")
    f.write(f"width: {width}\n")
    f.write(f"height: {height}\n")
    f.write(f"alpha: {alpha}\n")
    f.write(f"beta: {beta}\n")
    f.write(f"gamma: {gamma}\n")
    f.write(f"estimated sensors: {estimated_sensors}\n")
    f.write(f"Date/Time: {time.strftime('%Y-%m-%d %H:%M:%S')}\n")

# فتح ملف CSV لتسجيل أفضل القيم
with open(results_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Iteration', 'BestFitness', 'CoverageRatio', 'SensorCount'])

    for iteration in range(max_iteration):
        print(f"Iteration {iteration} / {max_iteration}")

        # ترتيب المجتمع حسب أفضلية الحلول
        population, fitness_list = sort_population_by_fitness(population, fitness_list)

        # تسجيل أفضل القيم الحالية
        writer.writerow([
            iteration + 1,
            round(variables.bestFitness, 4),
            round(variables.bestCoverageRatio, 4),
            variables.bestSensorNumber
        ])

        # تطبيق العمليات الجينية
        population = apply_GOs(population)

        # تطبيق البحث المحلي
        population, fitness_list = apply_local_search(population, fitness_list)
        
        # تحسين اكثر لافضل حل
        variables.bestSolution, variables.bestFitness = hill_climbing(variables.bestSolution, variables.bestFitness)
        variables.bestCoverage = compute_coverage(variables.bestSolution)

        # إعادة التقييم بعد التحديثات
        fitness_list = []
        for sol in population:
            coverage = compute_coverage(sol)
            fitness = evaluate(sol, coverage)
            fitness_list.append(fitness)
        
    # تحسين نهائي لافضل حل
    print("enhance the final best solution")
    variables.bestSolution, variables.bestFitness = hill_climbing(variables.bestSolution, variables.bestFitness)
    variables.bestCoverage = compute_coverage(variables.bestSolution)

    writer.writerow([
        max_iteration + 1,
        round(variables.bestFitness, 4),
        round(variables.bestCoverageRatio, 4),
        variables.bestSensorNumber
    ])

# حساب زمن التنفيذ النهائي
end_time = time.time()
execution_time = end_time - start_time

# حفظ زمن التنفيذ في ملف الإعدادات
with open(settings_file, mode='a') as f:
    f.write(f"Execution Time: {execution_time:.2f} seconds\n")
    
# طباعة النتائج النهائية
print("\n The best fitness:", round(variables.bestFitness, 4))
print("The coverage ratio:", round(variables.bestCoverageRatio, 4))
print("The sensors count:", variables.bestSensorNumber)
print("Compilation time is: {:.2f} s".format(execution_time))

# حفظ الحل الأفضل وغطائه في ملفات منفصلة
with open(solution_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(variables.bestSolution)

with open(coverage_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(variables.bestCoverage)

# رسم الشبكة
Visualizer.draw_solution(variables.bestSolution)
