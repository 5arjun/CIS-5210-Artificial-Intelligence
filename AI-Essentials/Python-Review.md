---
title: "AI Essentials: Python Review - For Loops, Comprehensions, and Generators"
date: 2026-01-27
tags: [Python, For-Loops, List-Comprehensions, Generators, AI-Essentials]
confidence: 0.80
source: handwritten
---

## For Loops

Basic **for** loop using `range`:
```
for x in range(5):
```

## List Comprehensions

List comprehensions replace loops!

**Double nested for loop vs list comprehension**:
```
for n in nums:
    for n in nums
        print(n*n)
```

**Example**: Squares
```
squares = [x*x for x in nums]
```
- Many different types of list comprehensions.

**Example lists**:
```
lst1 = [('a', 1), ('b', 2), ('c', 'hi')]
lst2 = ['x', 'a', 6]
```

## Dictionary and Set Comprehensions

**Dictionary comprehension**:
```
d = {k: v for k, v in lst1}
```
Equivalent with **for loops**:
```
d = dict()
for k, v in lst1:
    d[k] = v
```

**Set comprehension**:
```
s = {x for x in lst2}
```
Equivalent with **for loops**:
```
s = set()
for x in lst2:
    s.add(x)
```

## Generators

Generators are iterators with the **`yield`** keyword.

- **`yield`** each time `--next--` is called.
- Runs until **`yield`** statement is encountered.
- Next time, resumes where it left off.
- Values computed one at a time, as needed.
- Good for aggregating items.