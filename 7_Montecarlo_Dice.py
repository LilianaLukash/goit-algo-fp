import random
import matplotlib.pyplot as plt

# Кількість симуляцій
num_simulations = 1000000
sum_counts = {i: 0 for i in range(2, 13)}

# Виконання симуляцій
for _ in range(num_simulations):
    roll1 = random.randint(1, 6)
    roll2 = random.randint(1, 6)
    roll_sum = roll1 + roll2
    sum_counts[roll_sum] += 1

# Обчислення ймовірностей для кожної суми
probabilities = {sum_val: (count / num_simulations) * 100 for sum_val, count in sum_counts.items()}

theoretical_probabilities = {
    2: 2.78, 3: 5.56, 4: 8.33, 5: 11.11, 6: 13.89,
    7: 16.67, 8: 13.89, 9: 11.11, 10: 8.33, 11: 5.56, 12: 2.78
}

# Відображення результатів
fig, ax = plt.subplots()
ax.bar([k - 0.15 for k in probabilities.keys()], probabilities.values(), width=0.3, label='Монте-Карло', color='skyblue')
ax.bar([k + 0.15 for k in theoretical_probabilities.keys()], theoretical_probabilities.values(), width=0.3, label='Теоретичні', color='orange')

ax.set_xlabel('Сума')
ax.set_ylabel('Ймовірність (%)')
ax.set_title('Порівняння Монте-Карло та теоретичних ймовірностей')
plt.xticks(range(2, 13))
ax.legend()

plt.show()
#probabilities
