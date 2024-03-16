def greedy_algorithm(items, budget):
    # Спочатку розраховуємо співвідношення калорій до вартості для кожної страви
    item_ratios = {item: items[item]["calories"] / items[item]["cost"] for item in items}
    # Сортування страв за співвідношенням калорій до вартості у спадному порядку
    sorted_items = sorted(item_ratios.items(), key=lambda x: x[1], reverse=True)
    
    selected_items = {}
    total_cost = 0
    total_calories = 0
    for item, ratio in sorted_items:
        if total_cost + items[item]["cost"] <= budget:
            selected_items[item] = items[item]
            total_cost += items[item]["cost"]
            total_calories += items[item]["calories"]
    
    return selected_items, total_calories

def dynamic_programming(items, budget):
    item_names = list(items.keys())
    n = len(item_names)
    dp = [[0 for x in range(budget + 1)] for x in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, budget + 1):
            if items[item_names[i-1]]["cost"] <= w:
                dp[i][w] = max(items[item_names[i-1]]["calories"] + dp[i-1][w-items[item_names[i-1]]["cost"]], dp[i-1][w])
            else:
                dp[i][w] = dp[i-1][w]

    # Визначення вибраних страв
    w = budget
    selected_items = {}
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i-1][w]:
            item = item_names[i-1]
            selected_items[item] = items[item]
            w -= items[item]["cost"]
    
    total_calories = dp[n][budget]
    return selected_items, total_calories

# Дані про їжу
items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

# Виконання алгоритмів
budget = 100
greedy_result, greedy_calories = greedy_algorithm(items, budget)
dynamic_result, dynamic_calories = dynamic_programming(items, budget)

print(f'Menu from greedy {greedy_result}, Total calories: {greedy_calories} ')
print(f'Menu from dynamic {dynamic_result}, Total calories: {dynamic_calories} ')
