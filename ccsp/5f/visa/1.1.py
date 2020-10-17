def search_best_path(fr:Node,to:Node,
    current_poss:float,current_cost:int,
    best_poss:float,best_cost:int) -> Union[Path, None]:

    if fr is to:
        return current_cost, current_poss, []

    # 剪枝
    if current_poss < best_poss - 1e-4:
        return None
    if current_cost > best_cost:
        return None

    best_poss = 0.0
    best_cost = inf
    best_path = None
    for node,(poss,cost) in fr.tos.items():
        node: Node
        poss: float
        cost: int

        temp = search_best_path(node, to, current_poss*poss, 
            current_cost+cost)
        if temp is None:
            continue

        node_cost, node_poss, path = temp
        if node_poss > temp_best_poss
        best_cost = node_cost
        best_poss = node_poss
        temp_best_path = path
