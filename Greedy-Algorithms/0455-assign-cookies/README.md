# [455. Assign Cookies](https://leetcode.com/problems/assign-cookies/)

**Difficulty:** Easy

---

## Problem Statement

Assume you are an awesome parent and want to give your children some cookies. However, you can give **each child at most one cookie**.

Each child `i` has a **greed factor** `g[i]`, which is the minimum size of a cookie required to satisfy that child. Each cookie `j` has a size `s[j]`.

If `s[j] >= g[i]`, you can assign cookie `j` to child `i`, making the child content.

Your goal is to maximize the number of content children and return that maximum number.

---

## Examples

### Example 1

**Input**

```text
g = [1,2,3], s = [1,1]
```

**Output**

```text
1
```

**Explanation**

```text
There are 3 children with greed factors [1,2,3] and 2 cookies of sizes [1,1].

Only the child with greed factor 1 can be satisfied.

Hence, the maximum number of content children is 1.
```

---

### Example 2

**Input**

```text
g = [1,2], s = [1,2,3]
```

**Output**

```text
2
```

**Explanation**

```text
There are 2 children with greed factors [1,2] and 3 cookies of sizes [1,2,3].

All children can be satisfied.

Hence, the maximum number of content children is 2.
```

---

## Constraints

- `1 <= g.length <= 3 × 10^4`
- `0 <= s.length <= 3 × 10^4`
- `1 <= g[i], s[j] <= 2^31 - 1`

---

## Note

This problem is the same as **[LeetCode 2410: Maximum Matching of Players With Trainers](https://leetcode.com/problems/maximum-matching-of-players-with-trainers/)**.

---

## Topics

- Array
- Two Pointers
- Greedy
- Sorting