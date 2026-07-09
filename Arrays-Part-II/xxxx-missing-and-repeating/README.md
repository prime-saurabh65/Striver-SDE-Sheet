# [Missing And Repeating](https://www.geeksforgeeks.org/problems/find-missing-and-repeating2512/1)

**Difficulty:** Easy

---

## Problem Statement

Given an unsorted array `arr[]` of size `n`, containing elements from the range `1` to `n`, it is known that **one number in this range is missing**, and **another number occurs twice** in the array.

Find both the **repeating number** and the **missing number**.

Return the result as:

```text
[repeating, missing]
```

---

## Examples

### Example 1

**Input**

```text
arr[] = [2, 2]
```

**Output**

```text
[2, 1]
```

**Explanation**

```text
Repeating number is 2 and the missing number is 1.
```

---

### Example 2

**Input**

```text
arr[] = [1, 3, 3]
```

**Output**

```text
[3, 2]
```

**Explanation**

```text
Repeating number is 3 and the missing number is 2.
```

---

### Example 3

**Input**

```text
arr[] = [4, 3, 6, 2, 1, 1]
```

**Output**

```text
[1, 5]
```

**Explanation**

```text
Repeating number is 1 and the missing number is 5.
```

---

## Constraints

- `2 <= n <= 10^6`
- `1 <= arr[i] <= n`

---

## Topics

- Array
- Hashing
- Math
- Bit Manipulation
```