#include <iostream>
#include <vector>

using namespace std;

class Solution
{
public:
  int jump(vector<int>& nums)
  {
    auto steps = vector<int>(nums.size());
    steps[steps.size() - 1] = 0;

    for (int index = steps.size() - 1; --index >= 0;) {
      if (nums[index] + index + 1 >= nums.size()) {
        steps[index] = 1;
      } else {
        int min = INT_MAX;
        for (int i = index + nums[index]; i > index; --i) {
          if (steps[i] < min) {
            min = steps[i];
          }
        }
        if (min != INT_MAX) {
          ++min;
        }
        steps[index] = min;
      }
    }

    return steps[0];
  }
};

int
main()
{
  auto sln = Solution();
  auto nums = vector<int>{ 2, 3, 0, 1, 4 };

  cout << sln.jump(nums) << endl;
  getchar();
}
