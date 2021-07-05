#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int
binary_search(vector<int>& nums, int target, int left, int right)
{
  if (right - left == 1)
    return nums[left] == target ? left : -1;

  int mid = (left + right) / 2;
  if (nums[mid] <= target) {
    return binary_search(nums, target, mid, right);
  }

  return binary_search(nums, target, left, mid);
}

class Solution
{
public:
  int search(vector<int>& nums, int target)
  {
    if (nums.size() < 1)
      return -1;
    return binary_search(nums, target, 0, nums.size());
  }
};
