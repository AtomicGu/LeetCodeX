from common import TreeNode


class Solution:
    def findMode(self, root):
        if root is None:
            return []

        counter_max = 0
        most_nums = []

        current = 0
        counter = 0

        def mid_root_search(node):
            nonlocal counter_max, most_nums, current, counter
            if node is None:
                return
            mid_root_search(node.left)
            if node.val != current:
                if counter == counter_max:
                    most_nums.append(current)
                elif counter > counter_max:
                    most_nums = [current]
                    counter_max = counter
                current = node.val
                counter = 1
            else:
                counter += 1
            mid_root_search(node.right)
            return

        mid_root_search(root)
        if counter == counter_max:
            most_nums.append(current)
        elif counter > counter_max:
            most_nums = [current]
        return most_nums


root = TreeNode.from_heap([1, None, 2])
sln = Solution()
ans = sln.findMode(root)
print(ans)
