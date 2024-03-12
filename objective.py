from main import *


def objectiveFunction(temp, solution):
    """
    Evaluate the fitness of the newly generated solution.
    If the solution violates the weight constraint, reject it with a certain probability determined by the current temperature and the degree of violation.
    If the solution satisfies the weight constraint, compare its fitness with that of the current solution.
    If the new solution is better (has a higher fitness), accept it.
    If the new solution is worse, accept it with a certain probability determined by the current temperature and the magnitude of the difference in fitness between the new and current solutions.
    Repeat this process for a certain number of iterations or until a termination condition is met.

    so ill accept a better generated bag, if newly generated bag is worse but meets temp threshold then ill accept
    """

    print("\nEntering objective function")
    solutionFitness = evalSolution(solution)
    print(solutionFitness)
    newSolution = generateBag()
    newSolutionFitness = evalSolution(newSolution)

    if newSolutionFitness > solutionFitness:
        print("Accepting new solution")
        solution = newSolution
        print("Solution is now:", solution)
        return solution
    else:
        randomVal = random.randint(1, 100)
        if randomVal > temp:
            print("rand is greater than temp threshold, so we accept")
            solution = newSolution
            return solution
        else:
            print("rand threshold lower than temp threshold, so we deny")
            return solution