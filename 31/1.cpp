#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

class Solution
{
public:
  void nextPermutation(vector<int>& nums)
  {
    for (size_t i = nums.size() - 1; i != SIZE_MAX; --i) {
      size_t j;
      size_t k = SIZE_MAX;
      int max = INT_MAX;
      for (j = nums.size() - 1; j != i; --j) {
        if (nums[j] > nums[i] && nums[j] <= max) {
          max = nums[j];
          k = j;
        }
      }
      if (k != SIZE_MAX) {
        std::swap(nums[k], nums[i]);
        std::sort(nums.begin() + i + 1, nums.end());
        return;
      }
    }
    std::reverse(nums.begin(), nums.end());
  }
};

int
main()
{
  Solution sln;
  vector<int> v{ 1, 3, 2 };
  sln.nextPermutation(v);

  for (auto i : v) {
    std::cout << i << std::endl;
  }

  getchar();
}
