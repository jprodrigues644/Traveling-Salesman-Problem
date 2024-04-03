import random
from utils import perturbate_solution, calculate_cost, generate_random_solution, random_2opt
from load import load_symmetric_matrix , load_instance

def opt2_neighborhood(num_cities):
    neighborhood = []


    for i in range(num_cities - 1):
        for j in range(i + 2, num_cities):
            neighborhood.append((i, i + 1, j, (j + 1) % num_cities))

    return neighborhood


def best_improver_2_opt(matrix, current_solution, current_score, opt2_move):
    best_solution = current_solution
    best_score = current_score
    improvement_found = False

    
    for move in opt2_move:
        i, i1, j, j1 = move

        # Skip if i and j are the same (no distance between the same city)
        if i == j or i1 == j1 or i ==j1 or i1 ==j:
            continue
       
        new_solution = current_solution[:i1] + current_solution[i:j+1][::-1] + current_solution[j1+1:]
        # Calculer le coût de la nouvelle solution
        new_score = calculate_cost(matrix, new_solution)

        if new_score < best_score:
            best_solution = new_solution
            best_score = new_score
            improvement_found = True

                
    return best_solution, best_score, improvement_found


def worst_improver_2_opt(matrix, current_solution, current_score, opt2_move):
    
    worst_solution = current_solution
    worst_score = 0
    deterioration_found = False
    
    for move in opt2_move:
        i, i1, j, j1 = move

        # Skip if i and j are the same (no distance between the same city)
        if i == j or i1 == j1 or i ==j1 or i1 ==j:
            continue
       
        new_solution = current_solution[:i1] + current_solution[i:j+1][::-1] + current_solution[j1+1:]
        # Calculer le coût de la nouvelle solution
        new_score = calculate_cost(matrix, new_solution)
    
        # Vérifier s'il y a une détérioration
        if new_score < current_score and new_score >= worst_score :
            worst_solution = new_solution
            worst_score = new_score
            deterioration_found = True
       
    if worst_score == 0 : 
        worst_score = current_score 
            
    return worst_solution, worst_score, deterioration_found

def first_improver_2_opt(matrix,current_solution, current_score, opt2_move):
    
    first_solution = current_solution.copy()
    first_score = current_score
    improvement_found = False   
    
    for move in opt2_move:
        i, i1, j, j1 = move

        # Skip if i and j are the same (no distance between the same city)
        if i == j or i1 == j1 or i ==j1 or i1 ==j:
            continue
       
        new_solution = current_solution[:i1] + current_solution[i:j+1][::-1] + current_solution[j1+1:]
        # Calculer le coût de la nouvelle solution
        new_score = calculate_cost(matrix, new_solution)
    
        # Vérifier s'il y a une détérioration
        if new_score < first_score:
            first_solution = new_solution
            first_score = new_score
            improvement_found = True
            break
            
    return first_solution, first_score, improvement_found


def descent_2_opt(initial_solution, matrix, pivot_rule, opt2_neighborhood, improvement_found):
    current_solution = initial_solution
    current_score = calculate_cost(matrix, current_solution)

    while improvement_found:
       # Move this line outside the loop

        # Générer le voisinage
        neighborhood = opt2_neighborhood(len(current_solution))

        for _ in neighborhood:

            new_solution, new_score, move_improvement_found = pivot_rule(matrix, current_solution, current_score, neighborhood)
            #print(new_solution, new_score, move_improvement_found)
            if move_improvement_found and new_score < current_score :
                current_solution = new_solution
                current_score = new_score
                improvement_found = True
                break
            elif not move_improvement_found:
                improvement_found = False
                break
       
        
    return current_solution, current_score

def local_search_iterated_2_opt(initial_solution, matrix, neighborhood_generator, pivot_rule, num_perturbations, max_evaluations):
    current_solution = initial_solution
    current_score = calculate_cost(matrix, current_solution)
    best_solution = current_solution
    best_score = current_score
    evaluations = 0

    while evaluations < max_evaluations:
        improvement_found = True

        while improvement_found:
            improvement_found = False
            neighborhood = neighborhood_generator(len(current_solution))

            for _ in neighborhood:
                new_solution, new_score, improvement = pivot_rule(matrix, current_solution, current_score, neighborhood)

                if improvement and new_score < current_score:
                    current_solution = new_solution
                    current_score = new_score
                    improvement_found = True
                    break

                evaluations += 1

                if evaluations >= max_evaluations:
                    break

            if current_score < best_score:
                best_solution = current_solution
                best_score = current_score

        for _ in range(num_perturbations):
            perturbation = perturbate_solution(best_solution)
            perturbation_score = calculate_cost(matrix, perturbation)

            if perturbation_score < best_score:
                best_solution = perturbation
                best_score = perturbation_score

            evaluations += 1

            if evaluations >= max_evaluations:
                break

    return best_solution, best_score, evaluations

def sampled_walk_2_opt(initial_solution, matrix, num_evaluations, lambda_value):
    current_solution = initial_solution
    current_score = calculate_cost(matrix, current_solution)
    evaluations = 0

    while evaluations < num_evaluations:
        # Générer λ voisins
        #neighbors = [generate_random_solution(len(current_solution)) for _ in range(lambda_value)]
        # Générer λ voisins par des swaps
        neighbors = [random_2opt(current_solution) for _ in range(lambda_value)]
        # Evaluer les λ voisins
        #print(neighbors)
        scores = [calculate_cost(matrix, neighbor) for neighbor in neighbors]

        # Sélectionner le meilleur voisin
        best_neighbor = neighbors[scores.index(min(scores))]

        # Remplacement de la solution courante si le voisin est meilleur
        
        score_neighbor = calculate_cost(matrix, best_neighbor)
        if  score_neighbor < current_score:
            current_solution = best_neighbor
            current_score = score_neighbor                    
        evaluations += 1

    return current_solution, current_score, evaluations; 
 