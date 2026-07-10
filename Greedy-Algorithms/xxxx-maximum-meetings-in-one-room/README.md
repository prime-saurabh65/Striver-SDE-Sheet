# [Maximum Meetings in One Room](https://www.geeksforgeeks.org/problems/n-meetings-in-one-room-1587115620/1)

**Difficulty:** Medium

---

## Problem Statement

Given two arrays `s[]` and `f[]`, where `s[i]` and `f[i]` denote the start time and finish time of the `i`th meeting, respectively. There is only **one meeting room**.

A meeting can be scheduled only if its **start time is strictly greater** than the finish time of the previously selected meeting.

Find the **maximum number of meetings** that can be scheduled in the room such that no two selected meetings overlap.

Return the **1-based indices** of the selected meetings in **sorted (increasing) order**.

> **Note:** If multiple schedules are possible, prefer meetings with **earlier finish times**. If two meetings have the same finish time, prefer the meeting with the **smaller index**.

---

## Examples

### Example 1

**Input**

```text
s[] = [1, 3, 0, 5, 8, 5]
f[] = [2, 4, 6, 7, 9, 9]
```

**Output**

```text
[1, 2, 4, 5]
```

**Explanation**

```text
Attend the 1st meeting (1 to 2),
then the 2nd meeting (3 to 4),
then the 4th meeting (5 to 7),
and finally the 5th meeting (8 to 9).

This is the maximum number of meetings that can be attended.
```

---

### Example 2

**Input**

```text
s[] = [3]
f[] = [7]
```

**Output**

```text
[1]
```

**Explanation**

```text
Since there is only one meeting, it can be attended.
```

---

## Constraints

- `1 <= s.size() = f.size() <= 10^5`
- `0 <= s[i] <= f[i] <= 10^9`

---

## Topics

- Greedy
- Sorting
- Arrays