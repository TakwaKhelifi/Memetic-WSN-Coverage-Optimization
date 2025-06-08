import math
#network dimentions
width = 50
height = 50

# خصائص المستشعرات
radius = 5 
R = radius * radius
mu = 0.9 # packing dansity
estimated_sensors = int((width * height) / (math.pi * radius**2 * mu))

# local search matrics
max_local_iteration = 20

# genetic operations Propability
mp = 0.1 
cp=0.9

#general matrics
popSize = 30  # حجم المجتمع
max_iteration =  50 # أقصى عدد من التكرارات
Cmin = 0.75  # قيد التغطية
Cmax = 4  # قيد التغطية الزائدة

# fitness matrics
alpha = 0.6
beta = 0.45
gamma = -0.05

#selection Propabilities تجربة جديدة
top_solutions = 0.20
good_solution = 0.7 #0.50
#bad_solution =0.3

# best solution
bestSolution = [[0 for _ in range(width)] for _ in range(height)]
bestCoverage = [[0 for _ in range(width)] for _ in range(height)]
bestFitness = 0.00
bestCoverageRatio = 0.00
bestSensorNumber = 0

# إعدادات أخرى
#SEED = 42
