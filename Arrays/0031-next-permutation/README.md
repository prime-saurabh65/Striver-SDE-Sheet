# 31. Next Permutation

**Difficulty:** Medium

---

## Problem Statement

A permutation of an array of integers is an arrangement of its elements into a sequence or linear order.

For example, for `arr = [1,2,3]`, the following are all the permutations of `arr`:

```
[1,2,3]
[1,3,2]
[2,1,3]
[2,3,1]
[3,1,2]
[3,2,1]
```

The **next permutation** of an array of integers is the next lexicographically greater permutation of its elements.

More formally, if all the permutations of the array are sorted in lexicographical order, then the next permutation is the permutation that immediately follows the current arrangement.

If such an arrangement is not possible, rearrange the array into the **lowest possible order** (i.e., sorted in ascending order).

For example:

- The next permutation of `[1,2,3]` is `[1,3,2]`.
- The next permutation of `[2,3,1]` is `[3,1,2]`.
- The next permutation of `[3,2,1]` is `[1,2,3]`.

Given an integer array `nums`, modify it in-place to represent its next permutation.

The replacement must be **in-place** and use only **constant extra memory**.

---

## Examples

### Example 1

**Input**

```
nums = [1,2,3]
```

**Output**

```
[1,3,2]
```

---

### Example 2

**Input**

```
nums = [3,2,1]
```

**Output**

```
[1,2,3]
```

---

### Example 3

**Input**

```
nums = [1,1,5]
```

**Output**

```
[1,5,1]
```

---

## Constraints

- `1 <= nums.length <= 100`
- `0 <= nums[i] <= 100`

---

## Topics

- Array
- Two Pointers