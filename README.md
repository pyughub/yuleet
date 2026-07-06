# yuleet

Personal LeetCode-style algorithm practice in Python (with occasional C++).

Each problem lives in a pair of files:

- `problem_name.md` — problem statement, approach, and requirements
- `problem_name.py` — solution with a runnable `__main__` test block

## Getting started

Requires Python 3.10+.

Run any solution directly:

```bash
python spiral_matrix.py
python linked_list_cycle.py
```

## Problems

| Topic | File |
|-------|------|
| Two Sum | `two_sum.py` |
| Three Sum | `three_sum.py` |
| Container With Most Water | `container_with_most_water.py` |
| Trapping Rain Water | `trapping_rain_water.py` |
| Move Zeroes | `move_zeroes.py` |
| Rotate Array | `rotate_array.py` |
| Maximum Subarray | `maximum_subarray.py` |
| Merge Intervals | `merge_intervals.py` |
| Product of Array Except Self | `product_of_any_array_except_self.py` |
| Subarray Sum Equals K | `subarray_sum_equals_k.py` |
| Longest Substring Without Repeating Characters | `longest_substring_without_repeating_characters.py` |
| Find All Anagrams in a String | `find_all_anagrams_in_a_string.py` |
| Group Anagrams | `group_anagram.py` |
| Longest Consecutive Sequence | `longest_consecutive_sequence.py` |
| Set Matrix Zeroes | `set_matrix_zeros.py` |
| Spiral Matrix | `spiral_matrix.py` |
| Intersection of Two Linked Lists | `intersection_of_two_linked_lists.py` |
| Reverse Linked List | `reverse_linked_list.py` |
| Palindrome Linked List | `palindrome_linked_list.py` |
| Linked List Cycle | `linked_list_cycle.py` |

## Workflow

Use `pytemplate.md` as a starting point for new problems:

1. Write the spec in a `.md` file (input, output, steps, requirements).
2. Implement the function in a matching `.py` file.
3. Add test cases under `if __name__ == "__main__":` and run locally.

## License

MIT — see [LICENSE](LICENSE).
