import matplotlib.pyplot as plt
import numpy as np

def draw_tree(x, y, angle, length, depth):
    if depth == 0:
        return
    x_end = x + int(np.cos(np.radians(angle)) * length)
    y_end = y + int(np.sin(np.radians(angle)) * length)

    plt.plot([x, x_end], [y, y_end], 'k-', lw=1)

    new_length = length * 0.8  # Зменшуємо довжину гілки

    # Рекурсивно малюємо наступні гілки
    draw_tree(x_end, y_end, angle - 45, new_length, depth - 1)
    draw_tree(x_end, y_end, angle + 45, new_length, depth - 1)

def pythagoras_tree(depth):
    plt.figure(figsize=(10, 8))
    draw_tree(0, 0, 90, 100, depth)  # Початкові координати та кут
    plt.axis('off')
    plt.show()

# Викликаємо функцію для візуалізації дерева Піфагора з заданим рівнем рекурсії
while True:
    choice = input("Введіть глибину рекурсії для дерева Піфагора, для виходу нажміть E чи e ")
    if choice.lower() == "e" or choice.lower() == "exit":
        break
    try:
        n = int(choice)
        pythagoras_tree(n)
    except ValueError:
        print("Програма працює лише з цілими числами")
    
