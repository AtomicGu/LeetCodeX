#include <algorithm>
#include <iostream>

// 插入
void
insertion_sort(int* head, int* tail)
{
  int* p = head;
  while (++p < tail) {
    int temp = *p;
    int* q = p;
    while (--q >= head) {
      if (*q > temp)
        *(q + 1) = *q;
      else {
        *(q + 1) = temp;
        break;
      }
    }
  }
}

// 选择
void
selection_sort(int* head, int* tail)
{
  for (; head < tail; ++head) {
    int* min_p;
    for (int* p = head; p < tail; ++p) {
      if (*p < *min_p)
        min_p = p;
    }
    std::swap(*head, *min_p);
  }
}

// 冒泡
void
bubble_sort(int* head, int* tail)
{
  for (; head < tail; ++head) {
    for (int* p = head; ++p < tail;) {
      if (*(p - 1) > *p)
        std::swap(*(p - 1), *p);
    }
  }
}

// 快速
void
quick_sort(int* head, int* tail)
{
  if (tail - head <= 1)
    return;
  int *a = head, *b = tail;
  {
    int pivot = *head;
    while (true) {
      while (*--b > pivot)
        ;
      *a = *b;
      do {
        if (++a >= b)
          goto END;
      } while (*a <= pivot);
      *b = *a;
    }
  END:
    *b = pivot;
  }
  quick_sort(head, b);
  quick_sort(b + 1, tail);
}

// 归并
void
merge_sort(int* head, int* tail)
{
  if (tail - head <= 1)
    return;

  int* mid = head + (tail - head) / 2;
  merge_sort(head, mid);
  merge_sort(mid, tail);

  int* buf = new int[tail - head];
  for (int *a = head, *b = mid, *c = buf;; ++c) {
    if (*a < *b) {
      *c = *a;
      if (++a == mid) {
        memcpy(c + 1, b, (tail - b) * sizeof(int));
        break;
      }
    } else {
      *c = *b;
      if (++b == tail) {
        memcpy(c + 1, a, (mid - a) * sizeof(int));
        break;
      }
    }
  }

  memcpy(head, buf, (tail - head) * sizeof(int)); // 实际可以优化
  delete[] buf;
}

// 堆排序
void
head_sort(int* head, int* tail)
{
  std::make_heap(head, tail);
  std::sort_heap(head, tail);
}

// 计数
void
count_sort(int* head, int* tail, int max = 10)
{
  int* counters = new int[max];
  for (int i = 0; i < max; ++i) {
    counters[i] = 0;
  }

  for (int* p = head; p < tail; ++p) {
    ++counters[*p];
  }

  for (int i = 1; i < max; ++i) {
    counters[i] += counters[i - 1];
  }

  int* results = new int[tail - head];
  for (int* p = tail; --p >= head;) {
    results[--counters[*p]] = *p; // 注意这个前自减
  }

  memcpy(head, results, (tail - head) * sizeof(int));
  delete[] results;
}

// 基数
void
radix_sort(int* head, int* tail)
{
  for (int i = 1; i != 0; i <<= 1) {
    std::stable_sort(head, tail, [i](int a, int b) {
      return (a & i) < (b & i);
    }); // 位运算比关系运算还要低优先
  }
}

#define ARRAY_LENTH(arr) (sizeof(arr) / sizeof(arr[0]))

int
main()
{
  int nums[] = { 0, 1, 7, 3, 8, 1, 6, 2, 2, 5 };
  radix_sort(nums, nums + ARRAY_LENTH(nums));
  for (auto i : nums) {
    std::cout << i << ' ';
  }
  std::cout << std::endl;

  getchar();
}
