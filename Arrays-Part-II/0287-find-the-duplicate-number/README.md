# [287. Find the Duplicate Number](https://leetcode.com/problems/find-the-duplicate-number/)

**Difficulty:** Medium

---

## Problem Statement

Given an array of integers `nums` containing `n + 1` integers where each integer is in the range `[1, n]` inclusive.

There is only **one repeated number** in `nums`. Return this repeated number.

You must solve the problem **without modifying the array** and using **only constant extra space**.

---

## Examples

### Example 1

**Input**

```text
nums = [1,3,4,2,2]
```

**Output**

```text
2
```

---

### Example 2

**Input**

```text
nums = [3,1,3,4,2]
```

**Output**

```text
3
```

---

### Example 3

**Input**

```text
nums = [3,3,3,3,3]
```

**Output**

```text
3
```

---

## Constraints

- `1 <= n <= 10^5`
- `nums.length == n + 1`
- `1 <= nums[i] <= n`
- Every integer appears exactly once except for **one integer**, which appears **two or more times**.

---

## Follow-up

- How can we prove that at least one duplicate number must exist in `nums`?
- Can you solve the problem in **O(n)** time complexity?

---

## Topics

- Array
- Two Pointers
- Binary Search
- Bit Manipulation