#include <iostream>
#include <queue>
#include <unordered_map>
#include <vector>

using namespace std;

class Node
{
public:
  unordered_map<Node*, double> tos;
};

class Solution
{
public:
  vector<double> calcEquation(vector<vector<string>>& equations,
                              vector<double>& values,
                              vector<vector<string>>& queries)
  {
    for (size_t i = 0; i < equations.size(); ++i) {
      auto& AiBi = equations[i];
      auto& fr = nodes[AiBi[0]];
      if (!fr) {
        fr = new Node();
      }
      auto& to = nodes[AiBi[1]];
      if (!to) {
        to = new Node();
      }
      fr->tos[to] = values[i];
      to->tos[fr] = 1 / values[i];
    };

    vector<double> ans;
    for (size_t i = 0; i < queries.size(); ++i) {
      auto& CjDj = queries[i];
      ans.push_back(search(nodes[CjDj[0]], nodes[CjDj[1]]));
    }

    return move(ans);
  }

  double search(Node* fr, Node* to)
  {
    if (!fr || !to)
      return -1;

    unordered_map<Node*, bool> walked;
    walked[fr] = true;

    struct QueueItem
    {
      Node* p;
      double dist;
    };
    queue<QueueItem> q;
    q.push({ fr, 1 });
    while (!q.empty()) {
      auto a = q.front();
      if (a.p == to)
        return a.dist;

      for (auto i : a.p->tos) {
        if (walked[i.first])
          continue;
        q.push({ i.first, a.dist * i.second },1 );
      }

      q.pop();
      walked[a.p] = true;
    }

    return -1;
  }

private:
  unordered_map<string, Node*> nodes;
};

int
main()
{
  vector<vector<string>> equations{ { "a", "b" }, { "b", "c" } };
  vector<double> values{ 2.0, 3.0 };
  vector<vector<string>> queries{
    { "a", "c" }, { "b", "a" }, { "a", "e" }, { "a", "a" }, { "x", "x" }
  };

  Solution sln;
  auto ans = sln.calcEquation(equations, values, queries);

  for (auto i : ans) {
    cout << i << endl;
  }

  getchar();
}

/*
C++ 写起来实在太难用了：
1. 不支持用声明式的语法描述数据结构
   初始化个map那真他妈叫一个费劲
   虽然可以使用 constexpr map = parse_map("{....}") 的方式自定义语法，但目前还没见人这么用过！
2. 不支持匿名结构体
   57行，还得专门写个结构体；函数同时返回成功标志，还得专门准备个std::pair类型。
   要是pair套pair：a.first->first.first.first，真是脑溢血反人类代码。
3. 强类型不是问题，类型推导很差劲
   C的遗毒！变量声明是：<类型> <变量名>，非得把类型写在前面，实际上变量名才更重要好吗！
   <变量名>[:<类型>] 这种语法不香吗？
4. 调试困难
   我他妈调试模式下输个node[i]，它都给我报0x?????无法访问阿！调试表达式简直是个屁！
   没有debug()命令，只能手动渐进点断点！狗屎！
5. 调试信息晦涩难懂
   尤其是STL，妈的，一堆泛型，还有重载导致的名称粉碎，一个类型签名他们的几十个字母，四五层嵌套，这他妈是人读的？
   更别提STL里面各种奇奇怪怪的类型命名了，各STL实现还不一致！你当我是STL专家？
   C++的报错信息，只有提示你”这里错了“的作用，完全不能告诉你原因，对解决错误毫无帮助。
   
   体验一下：
   没有与参数列表匹配的 重载函数 "std::queue<_Tp, _Sequence>::push
    [其中 _Tp=QueueItem, _Sequence=std::deque<QueueItem, std::allocator<QueueItem>>]" 实例
    -- 参数类型为:  ({...}, int) -- 对象类型是:  std::queue<QueueItem, std::deque<QueueItem, std::allocator<QueueItem>>>
6. 传参难
   Python的传参真是艺术！超级方便好吗！
   只是，把可变参数放在运行期做没有问题，把静态重载也放在运行期确实有浪费效率，要是全都要就好了！
*/
