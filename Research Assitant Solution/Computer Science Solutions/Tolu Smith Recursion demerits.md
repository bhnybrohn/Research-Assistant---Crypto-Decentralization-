2. COMPUTER SCIENCE
•	Bad reasons for using recursions for Fibonacci series
                     Fibonacci is simply a sequence such that each number of the sequence is the         sum of the two preceding numbers, and the sequence starts from 0 and 1 e.g. 0,1,2,3,5,8…. Recursion by definition is “when a thing is defined in terms of itself.” In this case we are referring to mathematical or programmatic functions. With respect to a programming function, recursion happens when a function calls itself within its own definition. It calls itself over and over again until a base condition is met that breaks the loop.
                        Its demerits arise when each line of each call requiring its own stack, hence leading to memory exhaustion or max call stack size exceeded error also the longer processing time as the number gets larger, due to a lot of pushing-popping going on underground. Its major advantage is that recursion adds clarity and reduces the time needed to write and debug code.