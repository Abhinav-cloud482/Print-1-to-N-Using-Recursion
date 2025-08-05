##  Print 1 to N Using Recursion

This simple Python script demonstrates the use of a stack data structure to store and print numbers from 1 to N, where N is provided by the user.

---

## How It Works

1. The user is prompted to enter an integer N.

2. The program pushes integers from 1 to N onto a stack (implemented as a list).

3. It then pops and prints each element from the front of the stack using pop(0).

** Note : While stacks are typically LIFO (Last In, First Out), this script removes elements from the front of the list (pop(0)), which behaves like a queue (FIFO). This is not standard stack behavior and may affect performance for large N.

---

## Example

Enter N : 5

1 2 3 4 5

---

## Files
Print 1 to N Using Recursion.py – Main script file

---

## Note on Performance
Using pop(0) on a Python list has O(n) time complexity due to element shifting. For better performance with queue behavior, consider using collections.deque.

---

## Possible Improvements
- Use pop() for true stack behavior (prints in reverse order).

- Use deque for efficient FIFO behavior.

- Add input validation.

- Convert to a function or class for reusability.

---

## License
This project is open source and available under the MIT License.

---
