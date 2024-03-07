import random

items = [
    {'name': 'iron_sword', 'weight': 25, 'value': 15},
    {'name': 'wooden_bow', 'weight': 15, 'value': 15},
    {'name': 'apple', 'weight': 1, 'value': 3},
    {'name': 'sweetroll', 'weight': 1, 'value': 5},
    {'name': 'dragon_bone', 'weight': 25, 'value': 500},
    {'name': 'steel_mace', 'weight': 20, 'value': 25},
    {'name': 'elven_bow', 'weight': 12, 'value': 150},
    {'name': 'honey_nut_treat', 'weight': 2, 'value': 8},
    {'name': 'mead', 'weight': 3, 'value': 10},
    {'name': 'health_potion', 'weight': 0.5, 'value': 50},
    {'name': 'mana_potion', 'weight': 0.5, 'value': 50},
    {'name': 'stamina_potion', 'weight': 0.5, 'value': 50},
    {'name': 'scroll_of_fireball', 'weight': 0.2, 'value': 25},
    {'name': 'lockpick', 'weight': 0.1, 'value': 10},
    {'name': 'torch', 'weight': 0.5, 'value': 5},
    {'name': 'daedric_armour', 'weight': 30, 'value': 1000},
    {'name': 'sapphire_necklace', 'weight': 1, 'value': 600},
    {'name': 'silver_ring', 'weight': 1, 'value': 50},
    {'name': 'ebony_dagger', 'weight': 15, 'value': 200},
    {'name': 'diamond_ring', 'weight': 1, 'value': 800},
    {'name': 'dwemer_cog', 'weight': 1, 'value': 25},
    {'name': 'bear_pelt', 'weight': 3, 'value': 15},
    {'name': 'honeycomb', 'weight': 0.1, 'value': 8},
    {'name': 'broom', 'weight': 2, 'value': 5},
    {'name': 'frost_salts', 'weight': 0.2, 'value': 100},
    {'name': 'void_salts', 'weight': 0.2, 'value': 200},
    {'name': 'gold_ring', 'weight': 1, 'value': 100},
    {'name': 'glass_sword', 'weight': 17, 'value': 300}
]
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
    find lowest val ratio item and replace with random non-duplicate, this is a intuitive algorithmic approach that
    makes locally optimal choices at each step with the hope of finding a globally optimal solution

    maybe should only call when random is called for SA bc of heat, so it compares stochastic rather than just keeps
    going through making most optimal (maybe make most optimal as well to compare answer?)
    """
    print("entering perturbation function")
    counter = 0
    lowRatioItem = -999
    flag = False
    print("This is length of all items list: ", len(allItems))

    for item in knapsack:
        """
        find item with lowest val/weight ratio item
        """

        itemRatio = item["value"] / item["weight"]
        print("Name:", item["name"], " V/W ratio:", itemRatio)
        if itemRatio < lowRatioItem:
            lowRatioItem = itemRatio
            lowRatioItemName = item["name"]
            itemIndex = counter  # TODO find index so can be replaced by new random item and check if new item is non dup
            print("Item count is:", itemIndex, "Item name is:", lowRatioItemName)
        counter += 1

        while not flag:
            """
            replacing lowest val/weight item with random non-dup item - idea is continuous clean up 
            """

            randomItem = allItems[random.randint(1, len(allItems)) - 1]
            print("\n\nRandom item: ", randomItem)
            print("Low val item:ERRPR", lowRatioItemName)
            for x in knapsack:  # think this needs to move
                if x["name"] == randomItem["name"]:
                    print("duplicate is: ", x["name"])
                else:
                    print("no duplicate found, item is:", x["name"])
                    flag = True  # check this is the right logic and check its not regen random item
            """
            if dup found then generate new random item and start again
            """


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
