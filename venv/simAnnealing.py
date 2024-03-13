from objective import *
from generBag import *
from eval import *

def simulated_annealing():
    """
    Evaluate the fitness of the newly generated solution.
    If the solution violates the weight constraint, reject it with a certain probability determined by the current temperature and the degree of violation.
    If the solution satisfies the weight constraint, compare its fitness with that of the current solution.
    If the new solution is better (has a higher fitness), accept it.
    If the new solution is worse, accept it with a certain probability determined by the current temperature and the magnitude of the difference in fitness between the new and current solutions.
    Repeat until termination condition is met.
    """

    bag = generateBag()
    while evalSolution(bag) == 0:  # checks if solution exceeds threshold only
        bag = generateBag()
    newTemp = 100
    decayRate = 0.99
    flag = False

    print("\n\ngenerated bag: ", bag)
    print("all items: ", items)

    #temp loop
    while not flag:
        newTemp = (newTemp * decayRate)
        print(f"\n{newTemp}")
        decayRate -= 0.002
        if newTemp < 0.02:
            flag = True
        else:
            if evalSolution(bag) == 0:
                bag = generateBag()  # flat out refusal to accept any bag over weight threshold, making the algorithm have a degree of fault tolerance
                continue
            else:
                bag = objectiveFunction(newTemp, bag)
                # perturbSolution(bag, items)

    print("Final solution:", bag)
    print("Final solution ratio:", evalSolution(bag))