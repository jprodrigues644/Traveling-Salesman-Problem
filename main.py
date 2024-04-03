
from load import load_symmetric_matrix, load_instance
from utils import generate_random_solution, calculate_cost
from swap import swap_neighborhood, best_improver_swap, first_improver_swap,worst_improver_swap, descent_swap, local_search_iterated_swap, sampled_walk_swap
from opt2 import opt2_neighborhood, best_improver_2_opt , first_improver_2_opt ,  worst_improver_2_opt, descent_2_opt , local_search_iterated_2_opt, sampled_walk_2_opt
from lin_kernighan import local_search_lin_kernighan

print("*******************Traveling Salesman Problem********************")
print("-----------------------------------------------------------------")

#Iteration correspond au nombre d'execution pour chaque instance 
iteration = 10
while True:
    try:
        path = input("Rentrer le Chemin de l'instance : ")
        break
    except Exception as e:
        print(f"Erreur : {e}")
        
choice = 0
choice = int(input(" Rentrer 1 ou 2 Choisir un type d'instance : \n 1-Symetrique  \n 2-Asymetrique \n"))
while choice != 1 and choice != 2:
    choice = int(input("Entrer 1 ou 2 pour choisir un type d'instance : \n 1-Symetrique \n 2-Asymetrique \n"))
num_cities = 0
matrix = []

if choice == 1:
    num_cities, matrix = load_symmetric_matrix(path)
    print("Nombre de Villes à Parcourir : ", num_cities)
elif choice == 2:
    num_cities, matrix = load_instance(path)
    print("Nombre de Villes à Parcourir : ", num_cities)

costs = []
costs_descent_swap_best = []
costs_descent_swap_first = []
costs_descent_swap_worst = []
costs_descent_2opt_best = []
costs_descent_2opt_first = []
costs_descent_2opt_worst = []

costs_local_search_iterated_swap_best_5_1000 = []
costs_local_search_iterated_2opt_best_5_1000 = []

costs_local_search_iterated_swap_first_5_1000 = []
costs_local_search_iterated_2opt_first_5_1000 = []

costs_local_search_iterated_swap_worst_5_1000 = []
costs_local_search_iterated_2opt_worst_5_1000 =[]

costs_local_search_iterated_swap_best_7_1000 = []
costs_local_search_iterated_2opt_best_7_1000 = []

costs_local_search_iterated_swap_first_7_1000 = []
costs_local_search_iterated_2opt_first_7_1000 = []

costs_local_search_iterated_swap_worst_7_1000 = []
costs_local_search_iterated_2opt_worst_7_1000 =[]

costs_sampled_walk_swap_5 = []
costs_sampled_walk_2opt_5 = []

costs_sampled_walk_swap_7 = []
costs_sampled_walk_2opt_7 = []

# costs_local_search_lin_kernighan = []

# print(random_solution, score)

# print(local_search_lin_kernighan(random_solution,matrix,1000))


for i in range(iteration):
    #Descentes Swaps
    random_solution = generate_random_solution(num_cities)
    initial_cost = calculate_cost(matrix, random_solution)
    print("Initial cost", i ," : ", initial_cost)
    
    _, cost_descent_swap_best= descent_swap(random_solution, matrix, best_improver_swap, swap_neighborhood,True)
    costs_descent_swap_best.append(cost_descent_swap_best)
    _, cost_descent_swap_first = descent_swap(random_solution, matrix, first_improver_swap, swap_neighborhood,True)
    costs_descent_swap_first.append(cost_descent_swap_first)
    _, cost_descent_swap_worst= descent_swap(random_solution, matrix, worst_improver_swap, swap_neighborhood,True)
    costs_descent_swap_worst.append(cost_descent_swap_worst)
    
    #Descentes 2-Opt
    _, cost_descent_2opt_best = descent_2_opt(random_solution, matrix, best_improver_2_opt, opt2_neighborhood,True)
    costs_descent_2opt_best.append(cost_descent_2opt_best)
    _, cost_descent_2opt_first = descent_2_opt(random_solution, matrix, first_improver_2_opt, opt2_neighborhood,True)
    costs_descent_2opt_first.append(cost_descent_2opt_first)
    _, cost_descent_2opt_worst = descent_2_opt(random_solution, matrix, worst_improver_2_opt, opt2_neighborhood,True)
    costs_descent_2opt_worst.append(cost_descent_2opt_worst)
    
            #Recherche Local avec un parametre 5 
    #Recherches Bests-5
    
    _, cost_local_search_iterated_swap_best_5_1000,_= local_search_iterated_swap(random_solution, matrix,swap_neighborhood,best_improver_swap, 5, 1000)
    costs_local_search_iterated_swap_best_5_1000.append(cost_local_search_iterated_swap_best_5_1000)
    _, cost_local_search_iterated_2opt_best_5_1000, _ = local_search_iterated_2_opt(random_solution, matrix,opt2_neighborhood,best_improver_2_opt, 5, 1000)
    costs_local_search_iterated_2opt_best_5_1000.append(cost_local_search_iterated_2opt_best_5_1000)
    
    #Recherches First-5
    _, cost_local_search_iterated_swap_first_5_1000, _ = local_search_iterated_swap(random_solution, matrix,swap_neighborhood,first_improver_swap, 5, 1000)
    costs_local_search_iterated_swap_first_5_1000.append(cost_local_search_iterated_swap_first_5_1000)
    _, cost_local_search_iterated_2opt_first_5_1000, _ = local_search_iterated_2_opt(random_solution, matrix,opt2_neighborhood,best_improver_2_opt, 5, 1000)
    costs_local_search_iterated_2opt_first_5_1000.append(cost_local_search_iterated_2opt_first_5_1000)
    
    #Recherches Worst-5
    _, cost_local_search_iterated_swap_worst_5_1000, _ = local_search_iterated_swap(random_solution, matrix,swap_neighborhood,first_improver_swap, 5, 1000)
    costs_local_search_iterated_swap_worst_5_1000.append(cost_local_search_iterated_swap_worst_5_1000 )
    _, cost_local_search_iterated_2opt_worst_5_1000, _ = local_search_iterated_2_opt(random_solution, matrix,opt2_neighborhood,worst_improver_2_opt, 5, 1000)
    costs_local_search_iterated_2opt_worst_5_1000.append(cost_local_search_iterated_2opt_worst_5_1000)
    
        #Recherche local avec un parametre 7 
    
    #Recherches Best-7
   
    _, cost_local_search_iterated_swap_best_7_1000, _ = local_search_iterated_swap(random_solution, matrix,swap_neighborhood,best_improver_swap, 7, 1000)
    costs_local_search_iterated_swap_best_7_1000.append(cost_local_search_iterated_swap_best_7_1000)
    _, cost_local_search_iterated_2opt_best_7_1000, _ = local_search_iterated_2_opt(random_solution, matrix,opt2_neighborhood,best_improver_2_opt, 7, 1000)
    costs_local_search_iterated_2opt_best_7_1000.append(cost_local_search_iterated_2opt_best_7_1000)
    
    #Recherches First-7
    _, cost_local_search_iterated_swap_first_7_1000, _ = local_search_iterated_swap(random_solution, matrix,swap_neighborhood,first_improver_swap, 7, 1000)
    costs_local_search_iterated_swap_first_7_1000.append(cost_local_search_iterated_swap_first_7_1000)
    _, cost_local_search_iterated_2opt_first_7_1000, _ = local_search_iterated_2_opt(random_solution, matrix,opt2_neighborhood,first_improver_2_opt, 7, 1000)
    costs_local_search_iterated_2opt_first_7_1000.append(cost_local_search_iterated_2opt_first_7_1000)
    
    #Recherches Worst- 7 
    _, cost_local_search_iterated_swap_worst_7_1000, _ = local_search_iterated_swap(random_solution, matrix,swap_neighborhood,first_improver_swap, 7, 1000)
    costs_local_search_iterated_swap_worst_7_1000.append(cost_local_search_iterated_swap_worst_7_1000)
    _, cost_local_search_iterated_2opt_worst_7_1000, _ = local_search_iterated_2_opt(random_solution, matrix,opt2_neighborhood,worst_improver_2_opt, 7, 1000)
    costs_local_search_iterated_2opt_worst_7_1000.append(cost_local_search_iterated_2opt_worst_7_1000)
   
    
    # Sampled Walk Swap_5
  
    _, cost_sampled_walk_swap_5,_= sampled_walk_swap(random_solution, matrix, 1000, 5)
    costs_sampled_walk_swap_5.append(cost_sampled_walk_swap_5)
    #Sampled Walk 2-optr_2
    _, cost_sampled_walk_2_opt_5, _ = sampled_walk_2_opt(random_solution,matrix , 1000 , 5)
    costs_sampled_walk_2opt_5.append(cost_sampled_walk_2_opt_5)
    
    # Sampled Walk Swap_ 7
    _, cost_sampled_walk_swap_7,_= sampled_walk_swap(random_solution, matrix, 1000, 7)
    costs_sampled_walk_swap_7.append(cost_sampled_walk_swap_7)
    #Sampled Walk 2-optr_7
    _,cost_sampled_walk_2_opt_7, _ = sampled_walk_2_opt(random_solution,matrix , 1000 , 7)
    costs_sampled_walk_2opt_7.append(cost_sampled_walk_2_opt_7)
    print( i , "Execution Finished")
    #lin kerninghan #
    # _,cost_local_search_lin_kernighan = local_search_lin_kernighan(random_solution,matrix, 1000)
    # costs_local_search_lin_kernighan.append(cost_local_search_lin_kernighan)
    
    
   

print("---------------Descente Swap Best--------------")
print(costs_descent_swap_best)
print("---------------Descente Swap First--------------")
print(costs_descent_swap_first)
print("---------------Descente Swap Worst--------------")
print(costs_descent_swap_worst)

print("---------------Descente 2-Opt Best--------------")
print(costs_descent_2opt_best)
print("---------------Descente 2-Opt First--------------")
print(costs_descent_2opt_first)
print("---------------Descente 2-opt Worst--------------")
print(costs_descent_2opt_worst) 

print("---------------Recherche Local Iterée Swap Best 5 Perturbations--------------")
print(costs_local_search_iterated_swap_best_5_1000) 
print("---------------Recherche Local Iterée  2-opt Best 5 Perturbations--------------")
print(costs_local_search_iterated_2opt_best_5_1000) 
print("\n")
print("---------------Recherche Local Iterée Swap First 5 Perturbations--------------")
print(costs_local_search_iterated_swap_first_5_1000) 
print("---------------Recherche Local Iterée First 2-opt First 5 Perturbations--------------")
print(costs_local_search_iterated_2opt_first_5_1000) 
print("\n")
print("---------------Recherche Local Iterée Swap Worst 5 Perturbations--------------")
print(costs_local_search_iterated_swap_worst_5_1000) 
print("---------------Recherche Local Iterée 2-opt Worst  5 Perturbations--------------")
print(costs_local_search_iterated_2opt_worst_5_1000)
print("\n")


print("---------------Recherche Local Iterée Swap Best 7 Perturbations--------------")
print(costs_local_search_iterated_swap_best_7_1000) 
print("---------------Recherche Local Iterée  2-opt Best 7 Perturbations--------------")
print(costs_local_search_iterated_2opt_best_7_1000) 
print("\n")
print("---------------Recherche Local Iterée Swap First 7 Perturbations--------------")
print(costs_local_search_iterated_swap_first_7_1000) 
print("---------------Recherche Local Iterée First 2-opt First 7 Perturbations--------------")
print(costs_local_search_iterated_2opt_first_7_1000) 
print("\n")
print("---------------Recherche Local Iterée Swap Worst 7 Perturbations--------------")
print(costs_local_search_iterated_swap_worst_7_1000) 
print("---------------Recherche Local Iterée 2-opt Worst  7 Perturbations--------------")
print(costs_local_search_iterated_2opt_worst_7_1000)
print("\n")


print("--------------------Sampled Walk 5 Swap------------------------")
print(costs_sampled_walk_swap_5)
print("--------------------Sampled Walk 5 2-opt------------------------")
print(costs_sampled_walk_2opt_5)
print("\n")
print("--------------------Sampled Walk 7 Swap------------------------")
print(costs_sampled_walk_swap_7)
print("--------------------Sampled Walk 7 2-opt------------------------")
print(costs_sampled_walk_2opt_7)
print("\n")

# print("--------------Recherche Local Lin Kerninghan Simplifie---------------")
# print(costs_local_search_lin_kernighan)1