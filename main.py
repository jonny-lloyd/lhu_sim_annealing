"""
essentially trying to compare an opportunistic (finds worst val/weight ratio then swaps a random item) against stochastic
(can still swap for worse solutions if its below temp, swaps entire bag) algorithm
"""
from simAnnealing import *

knapsackCapacity = 100


def main():
    simulated_annealing()


if __name__ == "__main__":
    main()









# general idea
#  generate random bag, compare initial to new generated bag using fitness rating (which is val/wieght ratio), if fitness higher then is new best solution
#  and worse solutions can be picked depending on temp (dont know if this applies to 0 score/fitness solutions).
#
#  If solution is already pretty good it needs to be optimised/built on instead of compleletly abondoning it and hoping a random generated solution will be accepted at high temp.
#  therefore, will need a 'perturbSolution(solution, allItems)', this will  scan through list of items in current promising knapsack solution,
#  if a particular item has a low val/weight (in solution that is optimal), you can switch it for a random non
#  duplicate item from the list of all items (find new random item from big list then see if == to any items
#  in solution), then return improved optimal solution, if mew fitness score is higher then replace original with perturbSolution.

# considerations for above, how often perturbSolution will excecute? need to create a low val ratio threshold,
# maybe just store threshold of lowest ratio item and if lower ratio comes along it is replaced it, store index of lowest item as well as ratio and randomly replace it (this works well if new replacement is bad, running perturbSolution will replace it again anyway)
# Need to consider how close solution is to max capacity, if its v far off will never be optimal, however SA might do this for me anyways

# could run SA in parallel and reference parallel that was spoke about in ai lit review, comparing my perturbSolution to traditional SA

# COMPLETE
# if new bag > weight capacity, delete, regenerate and rerun loop, else then evaluate
