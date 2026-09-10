# Tower of Hanoi Assignment

## Solution Overview

The goal is to determine two things from a given Tower of Hanoi state:

1. Which peg the disks originally started on.
2. How many moves were made to reach the given state.

A direct simulation is not practical because a Tower of Hanoi sequence can contain up to **2^n - 1** moves. Since the assignment allows up to 64 disks, simulating every move would be far too slow.

The solution uses the recursive structure of Tower of Hanoi instead. For any set of **k** disks, the largest disk splits the optimal sequence into two parts:

- Before the largest disk moves.
- After the largest disk moves.

This lets the program skip entire groups of moves instead of generating them one at a time.

## Step-by-Step Approach

### 1. Store the current position of every disk

The input gives the disks currently present on pegs A, B, and C. I convert that into a python dictionary:

position[disk] = peg

For example, the state:

1, 2, 3

becomes:

disk 1 -> A
disk 2 -> B
disk 3 -> C

This makes it easy to check the current peg of any disk, especially the largest disk in each recursive call.

### 2. Handle the all-on-one-peg case

If every disk is on the same peg, the assignment says to treat that state as the initial state. In that case, the answer is that peg with 0 moves.

### 3. Try each peg as the possible starting peg

The input does not tell us whether the disks originally started on A, B, or C, so I try all three possibilities.

For each possible starting peg, I call the recursive **disk_moves** function. If the state cannot be reached from that peg, the function returns -1.

### 4. Find the destination for the current recursive problem

The assignment fixes the smallest disk's movement in the counterclockwise order:

A -> C -> B -> A

Because of this, the destination of a group of disks depends on whether the number of disks is odd or even.

For an odd number of disks, the destination is counterclockwise from the starting peg. For an even number of disks, it is clockwise.

The remaining peg becomes the spare peg.

### 5. Check the largest disk

This is the main part of the solution.

For **k** disks, disk k is the largest disk in the current recursive problem.

#### Case 1: The largest disk is still on the starting peg

The largest disk has not moved yet, so the target state must occur in the first part of the Hanoi sequence.

The problem can therefore be reduced to the first **k - 1** disks:

disk_moves(k - 1, start, ...)

#### Case 2: The largest disk is on its destination peg

The largest disk has already moved.

Before that move could happen, the first **k - 1** disks had to be moved out of the way. That takes:

**2^(k-1) - 1**

moves, followed by one move for disk **k**.

So exactly:

**2^(k-1)**

moves have already happened.

The smaller disks are now continuing from the spare peg, so I recursively calculate the remaining moves and add:

1 << (k - 1)

to the result.

#### Case 3: The largest disk is on the third peg

That state cannot occur in the required optimal sequence because the largest disk only moves once, directly from its source to its destination.

The function returns -1.

### 6. Check the allowed move range

The assignment requires the move count to be between **0** and **2^n - 2**, inclusive. If a result is outside that range, it is not accepted.

If none of A, B, or C can produce the given state, the program returns:

impossible

## Time and Space Complexity

### Time Complexity: O(n)

The recursive function processes one disk at each level:

**T(n) = T(n - 1) + O(1)**

so one attempt takes **O(n)** time.

The program tries at most three possible starting pegs. Since three is a constant:

**3 * O(n) = O(n)**


The input parsing also takes **O(n)** time, so the overall time complexity remains:

**O(n)**

This is much better than simulating the Tower of Hanoi sequence, which can require **O(2^n)** moves.

### Space Complexity: O(n)

The **position** dictionary stores one entry for each disk, which takes **O(n)** space.

The recursive call stack can also contain up to **n** calls, so it uses **O(n)** space.

Therefore, the overall space complexity is:

O(n)

## Use of LLMs

I used ChatGPT during the assignment mainly as a discussion and review tool.

I used ChatGPT mainly to reason through and validate my approach. I first used it to dry-run a brute-force recursive solution that explores all possible legal moves, which helped confirm why that approach would become impractical for larger values of n. I then used it to discuss ways to reduce the time complexity. The key observation we focused on was the position of the largest disk: if it is still on the source peg, the target state must be in the first recursive half; if it has moved to the destination peg, then 2^(n-1) moves have already occurred. From there, I adapted that reasoning into the recursive implementation, worked through the edge cases, and used it to review the complexity and generate additional test cases for validation.

Additionally, I used it to generate additional test cases, including a 64-disk case, so I could test the solution without relying only on the sample input.

The final solution was tested against the sample cases provided in the assignment as well as the additional test cases.