import random
from utils import generate_random_solution, calculate_cost,
from load import   generate_random_solution,  random_solution, matrix, swap_neighborhood, best_improver_swap

from opt2 import opt2_neighborhood

def perturbate_solution(solution):
    # Appliquer une perturbation en échangeant deux éléments aléatoires
    perturbed_solution = solution.copy()
    idx1, idx2 = random.sample(range(len(solution)), 2)
    perturbed_solution[idx1], perturbed_solution[idx2] = perturbed_solution[idx2], perturbed_solution[idx1]
    return perturbed_solution

def local_search_iterated(initial_solution, matrix, neighborhood_generator, pivot_rule, num_perturbations, max_evaluations):
    current_solution = initial_solution
    current_score = calculate_cost(matrix, current_solution)
    best_solution = current_solution
    best_score = current_score
    evaluations = 0

    while evaluations < max_evaluations:
        improvement_found = True

        while improvement_found:
            improvement_found = False

            # Générer le voisinage
            neighborhood = neighborhood_generator(len(current_solution))

            for _ in neighborhood:
                new_solution, new_score, improvement_found  = pivot_rule(current_solution,current_score, neighborhood)
                
                # Vérifier s'il y a une amélioration
                if new_score < current_score:
                    current_solution = new_solution
                    current_score = new_score
                    improvement_found = True
                    break  # Sortir du voisinage après la première amélioration

                evaluations += 1

                # Vérifier le critère d'arrêt
                if evaluations >= max_evaluations:
                    break

            # Mettre à jour la meilleure solution rencontrée
            if current_score < best_score:
                best_solution = current_solution
                best_score = current_score

        # Appliquer une perturbation à la meilleure solution
        for _ in range(num_perturbations):
            perturbation = perturbate_solution(best_solution)
            perturbation_score = calculate_cost(matrix, perturbation)

            # Vérifier si la perturbation améliore la solution
            if perturbation_score < best_score:
                best_solution = perturbation
                best_score = perturbation_score

            evaluations += 1

            # Vérifier le critère d'arrêt
            if evaluations >= max_evaluations:
                break

    return best_solution, best_score, evaluations

print("test")
print(local_search_iterated( random_solution,matrix, swap_neighborhood, best_improver_swap, 5 , 1 ))
