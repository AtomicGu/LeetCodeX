#include <iostream>
#include <string>
#include <vector>

using namespace std;

bool
is_right(const string& s)
{
  int n = 0;
  for (auto i : s) {
    if (i == '(') {
      ++n;
    } else {
      if (n == 0) {
        return false;
      }
      --n;
    }
  }
  return n == 0;
}

class Solution
{
public:
  vector<string> generateParenthesis(int n)
  {
    vector<string> ret;
    string s(n * 2, ' ');
    for (int i = (1 << n * 2) - 1; i >= 0; --i) {
      for (int j = 0; j < n * 2; ++j) {
        if (i & (1 << j)) {
          s[j] = '(';
        } else {
          s[j] = ')';
        }
      }
      if (is_right(s))
        ret.push_back(s);
    }
    return ret;
  }
};

int
main()
{
  auto sln = Solution();
  for (auto i : sln.generateParenthesis(3)) {
    cout << i << endl;
  }
}
