import random
from utils import perturbate_solution, random_swap, calculate_cost, generate_random_solution
from load import load_symmetric_matrix ,load_instance
def swap_neighborhood(num_cities):
    neighborhood = []

    for i in range(num_cities - 1):
        for j in range(i + 1, num_cities):
            neighborhood.append((i, j))

    return neighborhood



#Meilleur Améliorant 

def best_improver_swap(matrix,current_solution , current_score , swap_move):
    # on compare le score de chaque solution et on recupere son indice
    best_solution = current_solution
    best_score = current_score
    improvement_found = False

    for move in swap_move:
        i, j = move
        new_solution = current_solution.copy()
        new_solution[i], new_solution[j] = new_solution[j], new_solution[i]


        new_score = calculate_cost(matrix, new_solution)


        if new_score < best_score:
            best_solution = new_solution
            best_score = new_score
            improvement_found = True
    
        
    return best_solution, best_score, improvement_found

#Moins bon ameliorant 
def worst_improver_swap(matrix,current_solution , current_score , swap_move):
     # on compare le score de chaque solution et on recupere son indice

    worst_solution = current_solution
    worst_score = 0 
    deterioration_found = False

    for move in swap_move:
        i, j = move
        new_solution = current_solution.copy()
        new_solution[i], new_solution[j] = new_solution[j], new_solution[i]

        # Calculer le coût de la nouvelle solution
        new_score = calculate_cost(matrix, new_solution)

        # Vérifier s'il y a une détérioration
        if new_score < current_score and new_score >= worst_score :
            worst_solution = new_solution
            worst_score = new_score
            deterioration_found = True
          
        if  worst_score > 10000 :
            worst_score =  worst_score - 9999
            
    if worst_score == 0 : 
        worst_score = current_score     

    return worst_solution, worst_score, deterioration_found
#Premier Ameliorant
def first_improver_swap(matrix,current_solution, current_score, swap_move):
    first_solution = current_solution.copy()
    first_score = current_score
    improvement_found = False
    new_solution = first_solution


    for move in swap_move :
        
        i, j = move

        if first_score >= current_score:
            new_solution[i], new_solution[j] = new_solution[j], new_solution[i]

            new_score = calculate_cost(matrix, new_solution)

        if new_score < first_score:
            first_solution = new_solution
            first_score = new_score
            improvement_found = True
            break
        
        # """ if  first_score > 10000 :
        # first_score =  first_score - 9999 """
    #current_score = new_score

    return first_solution, first_score, improvement_found

def descent_swap(initial_solution, matrix, pivot_rule, swap_neighborhood, improvement_found):
    current_solution = initial_solution
    current_score = calculate_cost(matrix, current_solution)

    while improvement_found:
      

        # Générer le voisinage
        neighborhood = swap_neighborhood(len(current_solution))

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

def local_search_iterated_swap(initial_solution, matrix, neighborhood_generator, pivot_rule, num_perturbations, max_evaluations):
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



def sampled_walk_swap(initial_solution, matrix, num_evaluations, lambda_value):
    current_solution = initial_solution
    current_score = calculate_cost(matrix, current_solution)
    evaluations = 0

    while evaluations < num_evaluations:
        # Générer λ voisins
        #neighbors = [generate_random_solution(len(current_solution)) for _ in range(lambda_value)]
        # Générer λ voisins par des swaps
        neighbors = [random_swap(current_solution) for _ in range(lambda_value)]
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

    return current_solution, current_score,evaluations; 
