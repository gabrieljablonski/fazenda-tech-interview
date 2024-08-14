# FazendaTech - Programming Challenge

## 02 - Algorithms and Time Complexity

This challenge is designed to test your knowledge of basic algorithms and time complexity.

### Problem 01 - Fibonacci Sequence + Time Complexity

The Fibonacci Sequence does not need an introduction.

A recursive implementation of the sequence is as follows:

```python
def fibonacci(n):
  if n <= 1:
    return n
  return fibonacci(n - 1) + fibonacci(n - 2)
```

The time complexity for this naive implementation is `O(2^n)`.

#### Your Task

1. Come up with a `O(n)` time complexity implementation of the Fibonacci Sequence. Bonus points for a solution that has `O(1)` space complexity, and another that has `O(n)` space complexity.
2. Come up with a `O(1)` time complexity implementation of the Fibonacci Sequence for `n <= 1000`. Bonus points for including both an approximate* solution, and an exact solution.

\* The "approximate" solution will require you to make some assumptions about the time complexity of auxiliary operations. Make those assumptions explicit.

<details>
  <summary>Hint!</summary>

  For task #2's "exact" solution, you can assume the "time complexity clock" only start running when `fibonacci(n)` runs. You can do anything you want before that!
</details>


### Problem 02 - Data Storage/Retrieval

Given a string, you need to calculate the count of each character in the string.

The output should include each character with its respective count, and also the case of the first occurence of that character on the string (e.g. `a` vs `A`).

For example, given the string `FazendaTech is a pioneer on Generative AI technology!`, the output should include something like this:

> [!NOTE]  
> Ideally, your output should be a bit more readable. This output structure is not a requirement, so try to make it a bit more readable.

```
f F 1
a a 5
z z 1
e e 8
n n 5
d d 1
t T 3
c c 2
h h 2
    7
i i 4
s s 1
p p 1
o o 4
r r 2
g G 2
v v 1
l l 1
y y 1
! ! 1
```

#### Your Task

> [!CAUTION]  
> Your solution should be in JavaScript. Bonus points if you include some useful TypeScript type definitions (don't go overboard on the definitions!)

1. Implement a function that receives a string and returns the output as described above.
2. What is the time complexity of your implementation?
3. Is this complexity optimal? If yes, why? If not, how would you improve it?

<details>
  <summary>Hint!</summary>

  Pretty much any problem similar to this can be solved using just arrays. But since you're using JavaScript, isn't there another data structure that seems better suited for counting?
</details>
