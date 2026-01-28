---
title: "Python Functions Review - AI Essentials Lab"
date: 2026-01-27
tags: [python, functions, programming-basics, ai-essentials, syntax]
confidence: 0.805
source: handwritten
---

## Python Functions Review

### Basic Function Syntax

**What is the basic structure of a function definition?**

```python
def function_name(argument):
    line 1
    return mean, median, mode
```

### Key Function Characteristics

- **No function overloading** — Python does not support multiple function definitions with the same name
- **Multiple return values** — Functions can return multiple values as a tuple

### Function Arguments

#### Default Values

Default values make arguments optional:

```python
def my_fun(a, b=3, d="hello"):
    pass
```

#### Named Arguments (Keyword Arguments)

Functions can be called with arguments out of order if specified by name:

```python
def my_fun(a, b, c):
    pass

# Can be called as:
my_fun(c=40, b=2, a=13)
my_fun(b=16, a=1, c=3)
```

#### Variable-Length Arguments: *args

Accepts a variable number of positional arguments as a tuple:

```python
def print_func(*args):
    pass

# Can be called as:
print_func('a', 'b', 'c')

# Or with unpacking:
lst = ['a', 'b', 'c']
print_func(*lst)
```

#### Variable-Length Keyword Arguments: **kwargs

Accepts a variable number of keyword arguments:

```python
def print_kwargs(**kwargs):
    pass

# Can be called as:
print_kwargs(name="Joe", age=30)

# Or with unpacking:
my_dict = {'name': 'Joe', 'age': 30}
print_kwargs(**my_dict)
```

### Advanced Function Concepts

**Dynamic Scope** — Functions see the most current value of variables in their scope

**First Class Objects** — Functions have special properties:
- Can be passed as arguments to other functions
- Can be returned as values from other functions
- Can be assigned to variables
- Can be stored in data structures