import random


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
