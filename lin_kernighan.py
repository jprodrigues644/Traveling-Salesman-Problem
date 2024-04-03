import random
from utils import  calculate_cost

def lin_kernighan(matrix):
    num_cities = len(matrix)
    # Initialize the best tour with a random tour
    best_tour = generate_random_tour(num_cities)
    best_cost = calculate_cost(matrix, best_tour)

   
        # Perform one iteration of the Lin-Kernighan algorithm
    tour = lin_kernighan_iteration(matrix, best_tour)
    #print("tour", best_cost)       
            # Calculate the cost of the new tour
    tour_cost = calculate_cost(matrix, tour)

            # Update the best tour if the new cost is lower
    if tour_cost < best_cost:
            best_tour = tour
            best_cost = tour_cost
            
    return best_tour, best_cost

def lin_kernighan_iteration(matrix, current_tour):
    num_cities = len(matrix)

    for i in range(num_cities):
        t1 = current_tour[i]
        x1 = current_tour[i - 1], t1
        y1_candidates = get_y1_candidates(matrix, current_tour, t1, x1)

        for y1 in y1_candidates:
            i = reset_index(current_tour, y1[0])
            xi_condition_a = matrix[y1[1]][current_tour[0]] > 0
            xi_condition_b = check_condition_b(current_tour, i)

            if xi_condition_a and xi_condition_b:
                t_prime = update_tour(current_tour, i, y1[1])
                update_current_tour(matrix, current_tour, t_prime)

    return current_tour

def get_y1_candidates(matrix, current_tour, t1, x1):
    return [(t1, t2) for t2 in current_tour if matrix[t1][t2] != 9999 and (t1, t2) != x1]

def reset_index(current_tour, y1_value):
    return current_tour.index(y1_value)

def check_condition_b(current_tour, i):
    return all(current_tour[i - 1] != current_tour[s] for s in range(i))

def update_tour(current_tour, i, y1_value):
    return current_tour[:i] + [y1_value] + current_tour[i:]

def update_current_tour(matrix, current_tour, t_prime):
    t_prime_cost = calculate_cost(matrix, t_prime)
    current_tour_cost = calculate_cost(matrix, current_tour)

    if t_prime_cost < current_tour_cost:
        current_tour[:] = t_prime
        # print("update cost", T_prime_cost)

def generate_random_tour(num_cities):
    tour = list(range(num_cities))
    random.shuffle(tour)
    return tour



def local_search_lin_kernighan(initial_tour,matrix, max_iterations=1000):
    current_tour = initial_tour.copy()
    current_cost = calculate_cost(matrix, current_tour)
    #print("current cost",current_cost)

    for _ in range(max_iterations):
        # Apply Lin-Kernighan iteration to improve the current tour
        updated_tour, updated_cost  = lin_kernighan(matrix)

        # Verifie si le cout de la nouvelle solutionn  est inferieur au cout courrant
    
        #print("update cost",updated_cost)
        if  updated_cost < current_cost:
            current_tour = updated_tour
            current_cost = updated_cost
            #print("Current Cost", current_cost)
    return current_tour, current_cost

# best_tour, best_cost = lin_kernighan(matrix)
# print("Meilleure tournée :", best_tour)
# print("Coût de la meilleure tournée :", best_cost)

# print("Local Search Lin kernunghan ")
# print(local_search_lin_kernighan(random_solution, matrix))