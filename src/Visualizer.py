import matplotlib.pyplot as plt
import matplotlib.patches as patches
from variables import height, width, radius

def draw_solution(solution):
    fig, ax = plt.subplots(figsize=(10, 10))
    ax.set_xlim(0, width)
    ax.set_ylim(0, height)
    ax.set_aspect('equal')
    ax.set_facecolor('white')

    # رسم الشبكة
    for x in range(width + 1):
        ax.axvline(x, color='black', linewidth=0.2)
    for y in range(height + 1):
        ax.axhline(y, color='black', linewidth=0.2)

    # رسم المستشعرات والتغطية
    for i in range(height):
        for j in range(width):
            if solution[i][j] == 1:
                # إحداثيات المركز
                cx = j + 0.5
                cy = height - i - 0.5  # لقلب الاتجاه العمودي (0 في الأسفل)

                # رسم دائرة التغطية
                coverage_circle = patches.Circle(
                    (cx, cy), radius, facecolor=(0, 1, 0, 0.2), edgecolor='green', linewidth=1
                )
                ax.add_patch(coverage_circle)

                # رسم نقطة المستشعر
                ax.plot(cx, cy, 'o', color='blue', markersize=4)

    plt.title("Sensor Network Coverage")
    plt.tight_layout()
    plt.show()
