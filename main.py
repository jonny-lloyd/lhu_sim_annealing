import random
from items import *

knapsackCapacity = 100


def generateInitialBag():
    bag = []
    for item in items:
        randChoice = random.randint(0, 1)
        if randChoice == 1:  # selecting whether items are chosen or not randomly
            bag.append(item)
    return bag


def evalSolution(solution):  # if return is 0 discard solution, else compare returned ratio to best, if better overwrite with new result and new ratio
    """
    pass in current bag, add up weight then val then find solution, if solution is over threshold then punish,
    else return ratio and compare to alredy best ratio, if already best ratio is worse,
    then make current bag the new bag
    """

    print("entering eval")
    totalWeight = 0
    totalVal = 0

    for item in solution:
        totalWeight += item["weight"]
    if totalWeight > 100:
        print("Exceeds capacity, weight is: ", totalWeight)
        return 0
    else:
        for item in solution:
            totalVal += item["value"]

        ratio = totalVal/totalWeight

        print("total val:", totalVal)
        print("total weight:", totalWeight)
        print("ratio:", ratio)
        return ratio  # higher the ratio the more val per unit of weight


def perturbSolution(knapsack, allItems):
    """
    find lowest val ratio item and replace with a random non-duplicate. This is an intuitive algorithmic approach that
    makes locally optimal choices at each step with the hope of finding a globally optimal solution

    maybe should only call when random is called for SA bc of heat, so it compares stochastic rather than just keeps
    going through making most optimal (maybe make most optimal algo (so 3 in total) as well to compare answer?)
    """
    print("\nentering perturbation function")
    counter = 0
    lowRatioItem = +999
    flag = True
    print("This is length of all items list: ", len(allItems))
    print("This is length of knapsack items: ", len(knapsack))

    for item in knapsack:
        """
        find item with lowest val/weight ratio item
        """

        itemRatio = item["value"] / item["weight"]
        print("\nName:", item["name"], " V/W ratio:", itemRatio)  # "Index:", itemIndex
        if itemRatio < lowRatioItem:
            lowRatioItem = itemRatio
            lowRatioItemName = item["name"]
            itemIndex = counter  # TODO find index so can be replaced by new random item and check if new item is non dup
            print("Item count is:", itemIndex, "Item name is:", lowRatioItemName)
        counter += 1


    while flag:  # while i havent found a non dup
        '''
        replacing lowest val/weight item with random non-dup item - idea is continuous clean up /refine the solution 
        through successive iterations of item replacement
        '''

        randomItem = allItems[random.randint(1, len(allItems)) - 1]
        print("\n\nLOWEST RATIO IS:", lowRatioItemName)
        print("Random item: ", randomItem)
        for x in knapsack:  # think this needs to move
            if x["name"] == randomItem["name"]:
                print("duplicate is: ", x["name"])
                flag = False  # only flags when found -- flag up means were ok, flag down means dup

        if not flag:
            print("dup found, starting again")
            flag = True

        else:
            print("No duplicate found, proceeding...\n\n")
            break

    print("Old knapsack:", knapsack)
    knapsack[itemIndex] = randomItem
    print("New knapsack:", knapsack)

    return




initialBag = generateInitialBag()
print("\n\ngenerated bag: ", initialBag)
print("all items: ", items)

evalSolution(initialBag)
perturbSolution(initialBag, items)




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
