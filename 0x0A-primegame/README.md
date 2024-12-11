# 0x0A. Prime Game

## Task 0: Prime Game

Maria and Ben are playing a game where they take turns picking prime numbers from a set of consecutive integers starting from 1 up to and including `n`. Once a player picks a prime number, that number and all its multiples are removed from the set. The player who cannot make a move (because there are no remaining prime numbers to pick) loses the round.

The game is played for `x` rounds, where `n` may differ for each round. Maria always goes first, and both players play optimally. The task is to determine who wins the most rounds.

### **Function Prototype**
```python
def isWinner(x, nums)
```

- **x**: The number of rounds.
- **nums**: A list of integers `n`, representing the upper bound of the set for each round.

### **Return**
- Return the name of the player who wins the most rounds.
- If there is a tie, return `None`.

### **Constraints**
- `n` and `x` will not be larger than 10,000.
- No external libraries or imports are allowed for this task.

### **Example**

Given the input `x = 3` and `nums = [4, 5, 1]`, the game proceeds as follows:

1. **First round (n = 4):**
   - Maria picks 2 and removes 2 and 4, leaving [1, 3].
   - Ben picks 3 and removes 3, leaving [1].
   - Ben wins because Maria cannot pick a prime number.

2. **Second round (n = 5):**
   - Maria picks 2 and removes 2 and 4, leaving [1, 3, 5].
   - Ben picks 3 and removes 3, leaving [1, 5].
   - Maria picks 5 and removes 5, leaving [1].
   - Maria wins because Ben cannot pick a prime number.

3. **Third round (n = 1):**
   - There are no prime numbers to pick, so Ben wins by default.

**Result:** Ben wins the most rounds.

### **Example Usage**
```python
#!/usr/bin/python3

isWinner = __import__('0-prime_game').isWinner

print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))
```

**Output:**
```bash
Winner: Ben
```
