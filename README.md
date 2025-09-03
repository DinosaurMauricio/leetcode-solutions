# LeetCode Solutions

Repository meant to only to track what I've learned and practiced over time.

Many solutions may contain unclean code or have O(n²) complexity, so there’s room for improvement. This is also meant as personal notes, highlighting insights and approaches that could lead to O(N) time and memory optimizations and serving as a reminder for future reference.

# Notes

Linked List Notes – Linked lists can be tricky if you’re not careful with references and variable assignments. Since nodes are passed by reference, reassigning or modifying pointers without caution can easily break the list.

Always keep track of which node points where otherwise if head is needed. Instead, a temporary variable can be used to traverse, otherwise you’ll lose your reference to the list.

- Two-pointer approach To find the middle of a list, you can have two pointers: one slow (moves one step) and one fast (moves two steps). The fast pointer reaches the end first, and the slow pointer will be at the middle.

```python
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
```

A neat way to reverse the list if needed:

```python
    node = None
    while head:
        temp = head.next
        head.next = node
        node = head
        head = temp
```

Sliding Window – A useful technique for analyzing strings (or arrays) with two pointers, typically left and right. The idea is to progressively expand or shrink the window while processing the current substring/subarray. Additional pointers or conditions can be added as needed

```python
s = "abcde"
left = 0

for right in range(len(s)):
    window = s[left:right+1]
```

It’s useful to remember that if we already know previous values don’t contain the answer (e.g., during a loop), we can move the starting point forward instead of restarting from the beginning. This turns a nested loop (O(n²)) into a single pass (O(n)).

This optimization is commonly applied in sliding window problems.

```python
s = "abcabcbb"
left = 0
seen = set()

for right in range(len(s)):
    while s[right] in seen:
        seen.remove(s[left])
        left += 1
    seen.add(s[right])
```

Two Pointers (Start & End) – A common technique is to place one pointer at the start of the array and the other at the end. The pointers move toward each other based on conditions, making it efficient for problems like pair sums

```python
nums = [1, 2, 3, 4, 5]
left, right = 0, len(nums) - 1

while left < right:
    print(nums[left], nums[right])
    left += 1
    right -= 1
```

Prefix & Suffix Products – By precomputing prefix and suffix products, we can speed up calculations and avoid redundant work. It reduces time complexity and avoiding extra memory operations.

```python
nums = [1, 2, 3, 4]
n = len(nums)

prefix = [1] * n
suffix = [1] * n

for i in range(1, n):
    prefix[i] = prefix[i-1] * nums[i-1]

for i in range(n-2, -1, -1):
    suffix[i] = suffix[i+1] * nums[i+1]

result = [prefix[i] * suffix[i] for i in range(n)]
```

Stacks – Remember that besides common operations (push, pop), remember to always peek at the top element without removing it.

```python
stack = [1, 2, 3]

top = stack[-1]
```

Queues – Useful when you need to process elements in first-in, first-out (FIFO) order, such as traversing a list of tasks or elements simultaneously.

```python
queue = deque([1, 2, 3])

queue.append(4)

first = queue.popleft()
```

Trees – Two common traversal approaches:

- DFS (Depth-First Search) – Explores as far as possible along each branch before backtracking. Often implemented recursively. Useful when you need to process nodes from leaves upward.

- BFS (Breadth-First Search) – Visits all nodes level by level. Usually implemented with a queue.

Traversal, depending on the problem, is sometimes better to process nodes bottom-up (e.g., counting) rather than top-down.

```python
def processTree(tree):
    if not tree:
        return True

    is_left_leaf = processTree(tree.left)
    is_right_leaf = processTree(tree.right)

processTree(root)
```

Hash Map Lookup – This can help efficiently to find target values. Instead of scanning all elements, you can build a hash map for quick lookups. For example, rather than checking every pair for target = x + y, you can rearrange it to y = target - x and simply check if y exists in the hash map.

```python
nums = [2, 7, 11, 15]
target = 9
lookup = {}

for x in nums:
    y = target - x
    if y in lookup:
        print(f"Pair found: ({x}, {y})")
    lookup[x] = True
```

Digit Manipulation with Modulo and Integer Division – We can extract and manipulate digits using % (modulo) and // (floor division). This is especially useful for tasks like reversing a number.

For example, with 123:

- % 10 gives the last digit (3).
- Multiply the result by 10 in the next step to shift digits.
- Use // 10 to remove the last digit and continue.

```python
num = 123
reversed_num = 0

while num > 0:
    reversed_num = reversed_num * 10 + num % 10
    num //= 10
```

Python Data Structures for Tracking Elements

- Sets – Keep unique elements and allow fast membership checks.
- Tuples – Immutable sequences; good for fixed references or keys in dictionaries.
- Dictionaries

Reordering & Dummy Values – This is a silly one but useful one, if the problem doesn’t restrict it, sometimes it helps to reorder data or add dummy values. This can simplify logic and reduce edge-case handling (e.g., avoiding out-of-bounds checks).

---

Using the [LeetCode Save Extension](https://chromewebstore.google.com/detail/mojbjmadgddjbhokmpgnceiplpdkaodj) to easily export and upload my submissions here.
