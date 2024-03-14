
'''Алгоритм Дейкстри шукає найкоротший шлях від початкової вершини до всіх інших вершин
 у зваженому графі, де ваги ребер є невід'ємними. Використання бінарної купи (або пріоритетної черги)
   дозволяє оптимізувати вибір наступної вершини з найменшою вартістю шляху, зменшуючи тим самим загальну 
   складність алгоритму.'''

import heapq

def dijkstra(graph, start_vertex):
    INF = float('inf')
    distances = {vertex: INF for vertex in graph}
    distances[start_vertex] = 0

    priority_queue = [(0, start_vertex)]
    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        # Якщо відстань у купі більша, значить ми вже знайшли кращий шлях
        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
                
    return distances

# Приклад графу
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

# Виклик алгоритму для початкової вершини 'A'
distances = dijkstra(graph, 'A')
print(distances)
