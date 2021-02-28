class Solution:
    def closestCost(self, baseCosts: List[int], toppingCosts: List[int],
                    target: int) -> int:
        toppingCosts.sort(reverse=True)

        def greedy(target):
            ite = iter(toppingCosts)
            i = next(ite)
            while True:
                if i < target:
                    target -= i
                elif i == target:
                    break
                else:
                    try:
                        i = next(ite)
                    except StopIteration:
                        if -(target - i) < target:
                            return target - i
                        break
            return target

        return target - min(map(lambda x: greedy(target - x), baseCosts),
                            key=abs)
