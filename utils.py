import random

def maximum(liste):
    maxi = liste[0]
    for i in liste:
        if i >= maxi:
            maxi = i
    return maxi

#Solution aleatoire
def generate_random_solution(num_cities):

    solution = list(range(0, num_cities ))
    random.shuffle(solution)
    return solution

def perturbate_solution(solution):
    # Appliquer une perturbation en échangeant deux éléments aléatoires
    perturbed_solution = solution.copy()
    idx1, idx2 = random.sample(range(len(solution)), 2)
    perturbed_solution[idx1], perturbed_solution[idx2] = perturbed_solution[idx2], perturbed_solution[idx1]
    return perturbed_solution

def calculate_cost(matrix, solution):
    cost = 0
    num_cities = len(solution)

    for i in range(num_cities - 1):
        # Ajouter la distance entre la ville i et la ville suivante dans la solution
        cost += matrix[solution[i] ][solution[i + 1] ]
       
    # Ajouter la distance entre la dernière ville et la première ville (cycle)
    
    cost += matrix[solution[num_cities - 1] ][solution[0] ]
    
    return cost

def random_swap(solution):
    # Selectioner des incides aléaltoires 
    i, j = random.sample(range(len(solution)), 2)

    # Perform swap
    new_solution = solution.copy()
    new_solution[i], new_solution[j] = new_solution[j], new_solution[i]

    return new_solution

def random_2opt(solution):
    # Select two distinct indices randomly
    i, j = random.sample(range(len(solution)), 2)
    i, j = min(i, j), max(i, j)
    
    # Perform 2-opt swap
    new_solution = solution[:i] + solution[i:j+1][::-1] + solution[j+1:]

    return new_solution