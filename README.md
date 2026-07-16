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
python daily_temperatures.py
```

## Problems

### Array & String

| Problem | File |
|---------|------|
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
| Top K Frequent Elements | `top_k_frequent_elements.py` |
| Pascal's Triangle | `Pascal_Triangle.py` |
| Majority Element | `majority_element.py` |
| Single Number | `single_number.py` |
| Sort Colors | `sort_colors.py` |
| Next Permutation | `next_permutation.py` |
| Find the Duplicate Number | `find_the_duplicate_number.py` |

### Binary Search

| Problem | File |
|---------|------|
| Search Insert Position | `search_insert_position.py` |
| Search a 2D Matrix | `search_a_2D_matrix.py` |
| Find First and Last Position of Element in Sorted Array | `find_first_and_last_position_of_element_in_sorted_array.py` |
| Search in Rotated Sorted Array | `search_in_rotated_sorted_array.py` |
| Median of Two Sorted Arrays | `median_of_two_sorted_array.py` |

### Linked List

| Problem | File |
|---------|------|
| Intersection of Two Linked Lists | `intersection_of_two_linked_lists.py` |
| Reverse Linked List | `reverse_linked_list.py` |
| Palindrome Linked List | `palindrome_linked_list.py` |
| Linked List Cycle | `linked_list_cycle.py` |
| Add Two Numbers | `add_two_numbers.py` |
| Merge Two Sorted Lists | `merge_two_sorted_lists.py` |
| Remove Nth Node From End of List | `remove_nth_node_from_end_of_list.py` |
| Swap Nodes in Pairs | `swap_nodes_in_pairs.py` |
| Copy List with Random Pointer | `copy_list_with_random_pointer.py` |
| Sort List | `sort-list.py` |

### Tree

| Problem | File |
|---------|------|
| Binary Tree Inorder Traversal | `binary_tree_inorder_traversal.py` |
| Binary Tree Level Order Traversal | `binary_tree_level_order_traversal.py` |
| Invert Binary Tree | `invert_binary_tree.py` |
| Diameter of Binary Tree | `diameter_of_binary_tree.py` |
| Validate Binary Search Tree | `validate_binary_search_tree.py` |
| Convert Sorted Array to Binary Search Tree | `convert_sorted_array_to_binary_search_tree.py` |
| Construct Binary Tree from Preorder and Inorder Traversal | `construct_binary_tree_from_preorder_and_inorder_traversal.py` |

### Graph

| Problem | File |
|---------|------|
| Number of Islands | `number_of_islands.py` |
| Course Schedule | `course_schedule.py` |

### Backtracking & DFS

| Problem | File |
|---------|------|
| Permutations | `permutations.py` |
| Subsets | `subsets.py` |
| Combination Sum | `combination_sum.py` |
| Generate Parenthesis | `generate_parenthesis.py` |
| Word Search | `word_search.py` |
| Palindrome Partitioning | `palindrome_partitioning.py` |

### Stack

| Problem | File |
|---------|------|
| Decode String | `decode_string.py` |
| Daily Temperatures | `daily_temperatures.py` |
| Largest Rectangle in Histogram | `largest_rectangle_in_histogram.py` |

### Greedy

| Problem | File |
|---------|------|
| Jump Game | `jump_game.py` |
| Jump Game II | `jump_game_ii.py` |
| Partition Labels | `partition_labels.py` |

### Dynamic Programming

| Problem | File |
|---------|------|
| House Robber | `house_robber.py` |
| Perfect Squares | `perfect_squares.py` |
| Word Break | `word_break.py` |
| Maximum Product Subarray | `maximum_product_subarray.py` |
| Longest Increasing Subsequence | `longest_increasing_subsequence.py` |
| Longest Palindromic Substring | `longest_palindromic_substring.py` |

### Trie

| Problem | File |
|---------|------|
| Implement Trie (Prefix Tree) | `implement_trie_prefix_tree.py` |

## Workflow

Use `pytemplate.md` as a starting point for new problems:

1. Write the spec in a `.md` file (input, output, steps, requirements).
2. Implement the function in a matching `.py` file.
3. Add test cases under `if __name__ == "__main__":` and run locally.

## License

MIT — see [LICENSE](LICENSE).
