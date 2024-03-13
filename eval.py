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

        ratio = totalVal / totalWeight

        print("total val:", totalVal)
        print("total weight:", totalWeight)
        print("ratio:", ratio)
        return ratio  # higher the ratio the more val per unit of weight
