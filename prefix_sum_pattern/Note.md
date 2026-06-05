## LeetCode 303 — Range Sum Query (Immutable)

### Concept: Prefix Sum

Use a prefix sum array to answer range sum queries in **O(1)** time.

### Range Sum Formula

sum(left,right)=prefix[right+1]-prefix[left]

### Example

```python
nums = [-2, 0, 3, -5, 2, -1]

prefix = [0, -2, -2, 1, -4, -2, -3]
```

Find:

```python
sumRange(2, 5)
```

Calculation:

```python
prefix[6] - prefix[2]
= -3 - (-2)
= -1
```

### Code Template

```python
class NumArray:

    def __init__(self, nums):
        self.prefix = [0]

        for num in nums:
            self.prefix.append(self.prefix[-1] + num)

    def sumRange(self, left, right):
        return self.prefix[right + 1] - self.prefix[left]
```

### Complexity

| Operation        | Time | Space |
| ---------------- | ---- | ----- |
| Build Prefix Sum | O(n) | O(n)  |
| sumRange()       | O(1) | O(1)  |

### Interview Pattern

Use **Prefix Sum** when:

* Multiple range sum queries exist.
* Array is immutable (no updates).
* Fast query response is required.

**Keyword:** Range Sum → Think Prefix Sum.
