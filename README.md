# collatz-conjecture
This script creates graphs of the Collatz Conjecture.

There are variables to change the formula to different numbers than 3x+1 and /2.
My overall finding was that the chaotic behavior demonstrated by 3x+1 and /2 sequences is essentially just the same as the boring behavior demonstrated by x+1 and /2 sequences, but 3x+1 spikes whenever it encounters a number with only odd prime factors.

Generated graphs look like:

![Figure_1](https://user-images.githubusercontent.com/96557890/179048312-92fc6d0b-da32-43c1-abdc-bd513b35b193.png)

And the list of steps is printed in the console:
```
Odds: n*3+1  Evens: n/2
Step 0:   1         = 25 	 Prime Factors: 2 [5, 5]
Step 1:  25 * 3 + 1 = 76 	 Prime Factors: 3 [2, 2, 19]
Step 2:  76 / 2     = 38 	 Prime Factors: 2 [2, 19]
Step 3:  38 / 2     = 19 	 Prime Factors: 1 [19]
Step 4:  19 * 3 + 1 = 58 	 Prime Factors: 2 [2, 29]
Step 5:  58 / 2     = 29 	 Prime Factors: 1 [29]
Step 6:  29 * 3 + 1 = 88 	 Prime Factors: 4 [2, 2, 2, 11]
Step 7:  88 / 2     = 44 	 Prime Factors: 3 [2, 2, 11]
Step 8:  44 / 2     = 22 	 Prime Factors: 2 [2, 11]
Step 9:  22 / 2     = 11 	 Prime Factors: 1 [11]
Step 10: 11 * 3 + 1 = 34 	 Prime Factors: 2 [2, 17]
Step 11: 34 / 2     = 17 	 Prime Factors: 1 [17]
Step 12: 17 * 3 + 1 = 52 	 Prime Factors: 3 [2, 2, 13]
Step 13: 52 / 2     = 26 	 Prime Factors: 2 [2, 13]
Step 14: 26 / 2     = 13 	 Prime Factors: 1 [13]
Step 15: 13 * 3 + 1 = 40 	 Prime Factors: 4 [2, 2, 2, 5]
Step 16: 40 / 2     = 20 	 Prime Factors: 3 [2, 2, 5]
Step 17: 20 / 2     = 10 	 Prime Factors: 2 [2, 5]
Step 18: 10 / 2     = 5  	 Prime Factors: 1 [5]
Step 19:  5 * 3 + 1 = 16 	 Prime Factors: 4 [2, 2, 2, 2]
Step 20: 16 / 2     = 8  	 Prime Factors: 3 [2, 2, 2]
Step 21:  8 / 2     = 4  	 Prime Factors: 2 [2, 2]
Step 22:  4 / 2     = 2  	 Prime Factors: 1 [2]
Step 23:  2 / 2     = 1  	 Prime Factors: 0 []
Loop [4, 2, 1]
```
