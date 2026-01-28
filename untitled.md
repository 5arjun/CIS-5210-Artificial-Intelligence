---
title: "AI Essentials Python Review: Functions, Classes, and Iterators"
date: 2026-01-28
tags: [Python, Functions, Classes, Inheritance, List-Comprehensions, Generators]
confidence: 0.77
source: handwritten
---

## AI Essentials / Python Review 1/3: Functions

- **Functions**
  - Syntax: `def function_name(argument):`
    ```
    line 1
    return mean, median, mode
    ```
  - No function overloading
  - Can return multiple values (as tuple)
  - Default values for arguments (optional): `def my_fun(b, c=3, d="hello")`
  - Functions can be called with args out of order if specified:
    - Ex: `def myfun(a, b, c)` can be called as `myfun(c=40, b=2, a=13)` or `myfun(b=16, a=1, c=3)`

- **`*args`**: Accepts variable number of args (as tuple)
  - Ex: `def printfunc(*args)` can be called as `printfunc('a', 'b', 'c')`
  - Or: `lst = ['a', 'b', 'c']; printfunc(*lst)`

- **`**kwargs`**: Accepts variable number of keyword args
  - Ex: `def print_kwargs(**kwargs)` can be used as `print_kwargs(name="Joe", age=30)`
  - Or: `my_dict = {"name": "Joe", "age": 30}; print_kwargs(**my_dict)`

- **Dynamic Scope**: Sees most current value of vars

- **First Class Objects**:
  - Functions can be passed as args to other functions
  - Returned as values from other functions
  - Assigned to vars or stored in data structures

## AI Essentials / Python Review 2/3: Classes & Inheritance

- **Classes Example**:
  ```
  class Student:
      univ = "upenn"  # class attribute

      def __init__(self, name, dept):
          self.student_name = name
          self.student_dept = dept

      def print_details(self):
          print("Name: " + self.student_name)
          print("Dept: " + self.student_dept)

  student1 = Student("Jake", "cis")
  student1.print_details()
  # Alternative: Student.print_details(student1)
  ```

- Every method begins with `self` var

- **Extending Classes**:
  ```
  class AIStudent(Student):
      def __init__(self, name, dept):
          Student.__init__(self, name, dept)
  ```

- **Redefining Methods**: New `__init__` using same name in subclass (what you want to #**)

- **Magic Methods**: Begin with double underscore (`__str__`, `__len__`, `__add__`, etc)

- **Duck Typing**: Establishes suitability of object based on presence of methods
  - Does it swim like a duck? Quack like a duck? It's a duck

## AI Essentials / Python Review 3/3: Loops, Comprehensions, Generators

- **For Loops**:
  ```
  for x in range(5):
      ...
  ```

- **List Comprehensions** replace loops!
  - Double nested for loop vs list comprehension:
    ```
    for n in nums:
        for n in nums:
            print(n*n)
    ```

- **Dictionary & Set Comprehensions**:
  ```
  lst1 = [('a', 1), ('b', 2), ('c', 'hi')]
  lst2 = ['x', 'a', 6]
  d = {k: v for k, v in lst1}
  s = {x for x in lst2}

  # Equivalent traditional:
  d = dict()
  s = set()
  for k, v in lst1:
      d[k] = v
  for x in lst2:
      s.add(x)
  ```

- **squares = [x*x for x in nums]` (many diff types of list comprehensions)

- **Generators**:
  - Iterators with `yield` keyword
  - Yield each time `next()` is called; runs until `yield` statement encountered
  - Resumes where it left off next time
  - Values computed one at a time, as needed
  - Good for aggregating items