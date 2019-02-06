# Header here

## ***Day 1***

***Coursebook online free link in syllabus***

### Algorithm
  
- A Step by step process that produces a consistant result.
  - What do we want to know?
        - Does the program halt?
        - Does it run correctly?
        - How long does it take?  (BigO or time complexity).
        - How much storage does it take? (BigO or memory complexity).
    - When is the algorithm correct?
      - Correct for a test case if it works for the case.
      - Correct for a problem if it works for all possible test cases.

### Model of Computation

- Specifies the primitive operations a computer is assumed to support, and their costs.
  - Computation resources
    - CPU runtime, memory usage, messages sent along the network.

  - Resource consumption
    - Size of input.
    - Primary resources:
      - Time (usually most important)
        - T(n) for runtime of a program relative to size of its input.
        - Space
        - Best Case
          - Is minimum resources possible. symbol: Ω
        - Worst Case
          - Resource consumption is the maximum resource. symbol: O.
        - Average Case
          - Average resource consumption.  No special symbol.
        - Best Case = Worst Case
          - symbol: Θ

    - Specify resource consumption as a function of the inputs size.

## ***Day2***

### Algorithm Analysis

- Formal name: Asymptotic Analysis
- Estimation that groups algorithms based on growth rate.
- Unable to tell us for sure how one algorithm will perform relative to another.
- We care about worst case behavior.
- If adding previous non linear.
- If not added possibly linear.
- Approaching a solution at an exponential rate is logarithmic growth.
- Nested loops independent varialbes multiply.
- External loops independent variables add.
  - What is the analysis of the following codes?
    - Code 1:
      ~~~javascript
      var sum = 0;

      for(var i=1; i<=n; i*=2)
      {
        for(var j=1; j<=n; j++)
        {
          sum++;
        }
      }
      ~~~

      - **O(n(logn + 1)) = O(nlogn)**

      - Analyzing:

        | Variable | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
        | -------- | - | - | - | - | - | - | - | - |
        |    n     | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
        |    #     | 1 | 4 | 6 | 12| 15| 18| 21| 32|

        | Algorithm Comparison | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
        | -------------------- | - | - | - | - | - | - | - |
        |      nlogn           | 0 | 2 | 3 | 8 | 10| 12| 14|
        |       n^2            | 1 | 4 | 9 | 16| 25| 36| 49|

    - Code 2:

      ~~~javascript
      var sum = 0;

      for(var i=1; i<=n; i*=2)
      {
        for(var j=1; j<=i; j++)
        {
          sum++;
        }
      }
      ~~~

      - ***O(nlogn)***

        - Analyzing:

            | Variable | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
            | -------- | - | - | - | - | - | - | - | - |
            |    n     | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
            |    #     | 1 | 3 | 3 | 7 | 7 | 7 | 7 | 7 |

            | Algorithm Comparison | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
            | -------------------- | - | - | - | - | - | - | - |
            |      nlogn           | 0 | 2 | 3 | 8 | 10| 12| 14|
            |       n^2            | 1 | 4 | 9 | 16| 25| 36| 49|

    - Code 3:

      ~~~javascript
      for(var j = 2; j < a.length; j++)
      {
        key = A[j];
        i = j-1;

        while(var i > 0 and A[i] > key)
        {
          A[i+1] =A[i];
          i--;
        }
      }
      ~~~

      - ***O(n^2)***

        - Analyzing:

            | Helping Table | 1 | 2 | 3 | 4 |
            | ------------- | - | - | - | - |
            |      j        | 2 | 3 | 4 | 5 |
            |      i        | 1 | 2 | 3 | 4 |

            | Variable | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
            | -------- | - | - | - | - | - | - | - |
            | a.length | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
            |    #     | 1 | 3 | 6 | 10| 15| 21| 28|
            |  delta   | - | 2 | 3 | 4 | 5 | 6 | 7 |

            | Algorithm Comparison | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
            | -------------------- | - | - | - | - | - | - | - |
            |      nlogn           | 0 | 2 | 3 | 8 | 10| 12| 14|
            |       n^2            | 1 | 4 | 9 | 16| 25| 36| 49|

## ***Day3***

- Types of Algorithms
  - Divide and Conquer
    - Step 1:
      - Do a small bit of work
    - Step 2:
      - Recursively call that does same work on subset of original data.
    - Final step (sometimes)
      - Recombine results
    - Binary Search
      - Analyzing:

        |     n    | 1 | 2 | 4 | 6 | 8 |
        | -------- | - | - | - | - | - |
        |   steps  | 1 | 2 | 3 | 3 | 4 |

    - Recursion tree
      - n(1) -> n(2) -> n(3)
    - Recurrence equation
      - T(n) = 1 + T(n/2)
      - How to make.
        - Right Guess:
          - $Guess: T(n) = c*Log(n)$
          - using substitution...
          - $T(n) <= 1 + c*Log(n/2)$
          - $T(n) <= 1 + c*(Log(n) - Log(2))$
          - $T(n) <= 1 + c*(Log(n) - 1)$
          - $T(n) <= 1 + cLog(n) - c$
          - $When c=1,$ terms cancel out, thus..
          - $T(n) <= log(n)$
        - Wrong Guess
          - Guess: $T(n) = cn$
          - $T(n) <= 1 + c(n/2)$
          - if $c = 2$
          - $T(n) <= 1 + n$
          - not our guess so wrong. (except if forgot a property)
    - Merge sort
      - recursion 2x
      - work n
      - T(n) = n + 2t(n/2)
        |     n      | 1 | 2 | 4 | 8 | 16 |
        | ---------- | - | - | - | - | -- |
        |   steps    | 1 | 4 | 12| 32| 80 |
        | rateChange | - | 2 | 3 | 4 | 5  |
      - using recursion tree
        - n -> (n/2)*2 -> (n/4)*4 -> (1)*8
        - depth log(n)
        - every level do n work
        - efficiency depth * workPerLevel
        - = nlog(n)
    - recurrence relation
      - $T(n) = 2T(n/2) + n$
      - $Guess: c*N*Log(N)$
      - $T(n) <= 2(c(n/2)Log(n/2)) + n$
      - $c*n*Log(n) + n$
      - $c*n*(Log(n) - 1) + n$
      - $c*n*Log(n) - c*n + n$
      - $when c = 1$
      - $nLog(n) + n$
    - Master cases
      - Case 1:
        - $f(n) = O(n^(logb^(a-e)))$ for some $e >0$
        - then $T(n) = Θ(n^(logb^(a-e)))$
        - $T(n) = 9T(n/3) + n$
          - Try
          - $T(n) = 2T(n/4) + 1$
          - $a = 2, b = 4, f(n) = 1$
          - $1 = n^(log4^(2-e)))$
          - when $e=1$
          - $n^(Log4^1) = n^0 = 1$
          - $Θ(n^(log(4^2)) = Θ(\sqrt(n))$
      - Case 2:
      - Case 3:
        - $f(n) = Ω(n^(logb^(a+e)))$
        - for some $e > 0$ and $af(n/b) <= cf(n)$
        - where $c < 1$ and all large $n$
        - then $T(n) = Θ(f(n))$

## Greedy Algorithms
  
- Greedy Algorithms:
  - Definition: For each deciision point do whatever makes the most sense/work at that point.
    - Examples:
      - should i take sleep slope or shallow?
        - Steep
      - take old arcata rd or 101 to get to Eureka
        - 101
  - Implicit assumption is we are trying to minimize expensive work.
  - Many greedy algorithms use priority queues, or heaps to manage decision making.
  - Cons:
    - get caught in local maximums.
      - stops whenever something goes against the solution.
      - Example:
        - **1-0 knapsack problem**
          - fiven a bunch of stones with associated weights and values and a fixed-sized bag, how much value can we store?

          | rocks | weight | value|
          | ----- | ------ | ---- |
          | rock1 |   5    |  10  |
          | rock2 |   5    |  10  |
          | rock3 |   7    |  15  |
          | pack  |   10   |  -   |
          - Greedy says grab rock 3, but best to grab both rock1 and rock2.
          - Greedy inefficient.
        - **Double knapsack problem**
          - allowed to chisel off portions of the rock.

          | rocks | weight | value|
          | ----- | ------ | ---- |
          | rock1 |   5    |  10  |
          | rock2 |   5    |  10  |
          | rock3 |   7    |  15  |
          | rock3 |   7    |  15  |
          | pack  |   10   |  -   |
          - Greedy says take b and chisel 3lb off another b.
          - Greedy is best.
      - Huffman Coding
        - Common compression algorithm for zip files.
        - Uses binary trees and a greedy algorithm.
        - Works by finding patterns in sequences.
          - very acheivalbe in ascii
          - consider ascii string 'aaa'
          - binary version is 001100001 is a, thus 'aaa' is 001100001  001100001  001100001
          - run a substitution algorithm with shortcut characters.
          - thus if 'a' becomes single bit 0, the sequence then becomes 000, which is a savings of 21 bits or 87.5% compression
          - goal map long wasteful bit sequences into shorter bit sequences.
            - Example:
              - String 'aaabbc', what binary mapping would yield shortest sequence.
              - option 1: a = 01, b = 1, c = 0
                - 010101110
              - option 2: a = 0, b = 1, c = 01
                - 0001101
              Best to give most common characters the shortest mappings.
          - **Algorithm**
            - Step 1: build a frequency map of all unique chars in the file
            - Step 2: build a forest based on fruqency distrubtion.
              - each tree in forest has a value(char) and weight(frequency)
            - Step 3: Until there exists a forest, merge forests based on weight.
              - We will throw all forests in a min pq
              - while the pq is not empty:
                - pop off top two forests, merge. push resulting forest back onto pq.