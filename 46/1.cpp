#include <iostream>
#include <vector>

using namespace std;

class Solution
{
public:
  vector<vector<int>> permute(vector<int>& nums)
  {
    vector<bool> choosed(nums.size(), false);
    return aaa(nums, choosed);
  }

  vector<vector<int>> aaa(vector<int>& nums, vector<bool>& choosed)
  {
    vector<vector<int>> a;

    for (int i = 0; i < choosed.size(); ++i) {
      if (!choosed[i]) {
        choosed[i] = true;
        for (auto j : aaa(nums, choosed)) {
          j.push_back(nums[i]);
          a.push_back(move(j));
        }
        choosed[i] = false;
      }
    }

    if (a.size() == 0) {
      a.push_back({});
    }

    return move(a);
  }
};

int
main()
{
  auto sln = Solution();
  auto nums = vector<int>{ 1, 2, 3 };

  for (auto i : sln.permute(nums)) {
    for (auto j : i) {
      cout << j << ' ';
    }
    cout << endl;
  }

  getchar();
}
