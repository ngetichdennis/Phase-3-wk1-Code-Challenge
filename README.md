## Code Challenge
Challenge 1: 
There are N boxes (numbered from 0 to N−1) arranged in a row. The K-th box contains A[K] bricks. In one move you can take one brick from some box and move it to a box next to it (on the left or on the right). What is the minimum number of moves needed to end up with exactly 10 bricks in every box?


Write a function:

function solution(A);

that, given an array A of N integers, returns the minimum number of moves needed to end up with exactly 10 bricks in every box. If this is not possible, the function should return −1.

Examples:

1. For A = [7, 15, 10, 8], the function should return 7. You can perform the following sequence of moves:
   - move three bricks from box number 1 to the box on the left: [10, 12, 10, 8];
   - move two bricks from box number 1 to the box on the right: [10, 10, 12, 8];
   - finally, move two bricks from box number 2 to the last box: [10, 10, 10, 10].


2. For A = [11, 10, 8, 12, 8, 10, 11], the function should return 6. You can perform the following sequence of moves:
    - move a brick from box number 0 to box number 2 (using two moves);
    - move a brick from the last box two positions to the left (using two moves);
    - move a brick from the middle box to each of its neighbors (another two moves).


3. For A = [7, 14, 10], the function should return −1. It is not possible to end up with exactly 10 bricks in each box.
 

Challenge 2: 
Write a function:


function solution(A);


that, given an array A consisting of N integers, returns the maximum sum of two numbers whose digits add up to an equal sum. If there are no two numbers whose digits have an equal sum, the function should return -1.

Examples: 
1. Given A = [51, 71, 17, 42], the function should return 93. There are two pairs of numbers whose digits add up to an equal sum: (51, 42) and (17, 71).  The first pair sums up to 93.
2. Given A = [42, 33, 60], the function should return 102. The digits of all numbers in A add up to the same sum, and choosing to add 42 and 60 gives the result 102.
3. Given A = [51, 32, 43], the function should return -1, since all numbers in A have digits that add up to different, unique sums.
 

Challenge 3: 
Write a function solution that, given an integer N, returns a string of length N containing as many different lower-case letters ('a'-'z') as possible, in which each letter occurs an equal number of times.

Examples:

1. Given N = 3, the function may return "fig", "pea", "nut", etc. Each of these strings contains three different letters with the same number of occurrences.

2. Given N = 5, the function may return "mango", "grape", "melon", etc.

3. Given N = 30, the function may return "aabbcc...oo" (each letter from 'a' to 'o' occurs twice). The string contains 15 different letters.
Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..200,000].