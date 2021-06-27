#include <algorithm>
#include <iostream>

struct ListNode
{
  int val;
  ListNode* next;
  ListNode()
    : val(0)
    , next(nullptr)
  {}
  ListNode(int x)
    : val(x)
    , next(nullptr)
  {}
  ListNode(int x, ListNode* next)
    : val(x)
    , next(next)
  {}
};

class Solution
{
public:
  ListNode* swapPairs(ListNode* head)
  {
    auto a = head;
    if (!a)
      return nullptr;

    auto b = a->next;
    if (!b)
      return a;

    a->next = swapPairs(b->next);
    b->next = a;
    return b;
  }
};

int
main()
{
  Solution sln;
  auto head =
    new ListNode(1, new ListNode(2, new ListNode(3, new ListNode(4))));
  head = sln.swapPairs(head);

  while (head) {
    std::cout << head->val << std::endl;
    head = head->next;
  }

  getchar();
}
