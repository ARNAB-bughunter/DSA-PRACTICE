## Two-Pointer Pattern

### Concept

Use two indices (pointers) that move toward each other — or in the same
direction — across a sorted structure to avoid the O(n²) brute-force
nested loop. Each comparison eliminates one end of the search space, so
the whole array is scanned in **O(n)**.

Two-pointer only works reliably when the array is **sorted** (or the
pointers are moving through it in a way where order is guaranteed) —
this is what lets you decide *which* pointer to move based on the
comparison result.

### Core Idea

```
left = 0
right = n - 1

while left < right:
    if condition_met(nums[left], nums[right]):
        # record answer
        left += 1
        right -= 1
    elif need_bigger_value:
        left += 1
    else:
        right -= 1
```

At each step, you shrink the window `[left, right]` by exactly one side,
so the total number of steps is bounded by `n`.

---

### Complexity

| Operation                | Time  | Space |
| ------------------------- | ----- | ----- |
| Single two-pointer pass (sorted input) | O(n) | O(1) |
| Sort + two-pointer | O(n log n) | O(1) (or O(n) if sort isn't in-place) |
---

### Interview Pattern

Use **Two Pointer** when:

* The array is sorted, or can be sorted without losing needed info (e.g. index-independent problems).
* You're looking for a pair/triplet/subarray satisfying a sum or comparison condition.
* You want to eliminate brute-force nested loops (O(n²) or O(n³) → O(n) or O(n²)).
* There's a clear, provable rule for which pointer to move at each step (sorted-order logic, or a greedy "this side can't be the answer" argument).

**Keyword:** Pair/Triplet + Sorted (or sortable) + Sum/Max/Min condition → Think Two Pointer.
