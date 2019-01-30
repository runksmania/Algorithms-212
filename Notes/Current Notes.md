# ***Day 1***

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
                T(n) for runtime of a program relative to size of its input.
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
        #### Code 1:
        ```
        var sum = 0;

        for(var i=1; i<=n; i*=2)
        {
            for(var j=1; j<=n; j++)
            {
                sum++;
            }
        }
        ```

        **O(n(logn + 1)) = O(nlogn)**

        - Analyzing:
            
            | Variable | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
            | -------- | - | - | - | - | - | - | - | - |
            |    n     | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
            |    #     | 1 | 4 | 6 | 12| 15| 18| 21| 32|
            
            | Algorithm Comparison | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 
            | -------------------- | - | - | - | - | - | - | - | - |
            |      nlogn           | 0 | 2 | 3 | 8 | 10| 12| 14| 24|
            |       n^2            | 1 | 4 | 9 | 16| 25| 36| 49| 64|
        
        #### Code 2:    
        ``` 
        var sum = 0;

            for(var i=1; i<=n; i*=2)
            {
                for(var j=1; j<=i; j++)
                {
                    sum++;
                }
            }
        ```

        ***O(nlogn)***

        - Analyzing:
            | Variable | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
            | -------- | - | - | - | - | - | - | - | - |
            |    n     | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
            |    #     | 1 | 3 | 3 | 7 | 7 | 7 | 7 | 7 |
            
            | Algorithm Comparison | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 
            | -------------------- | - | - | - | - | - | - | - | - |
            |      nlogn           | 0 | 2 | 3 | 8 | 10| 12| 14| 24|
            |       n^2            | 1 | 4 | 9 | 16| 25| 36| 49| 64|

    ### Code 3:
    ```
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
    ```
    
    ***O(n^2)***

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
            
            | Algorithm Comparison | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 
            | -------------------- | - | - | - | - | - | - | - | - |
            |      nlogn           | 0 | 2 | 3 | 8 | 10| 12| 14| 24|
            |       n^2            | 1 | 4 | 9 | 16| 25| 36| 49| 64|
