<img width="600" height="400" alt="binary-and-linear-search-animations" src="https://github.com/user-attachments/assets/8c4b4461-7dc3-4f09-8e6e-0bde287d4aa3" />


# Extreme Performance & System Constraint Analysis

[![Performance Testing](https://img.shields.io/badge/Testing-Performance-blue?style=for-the-badge&logo=python)](tests/performance_test.py)

## 1. Abstract
This report documents the stress testing of the DSA Final Project system, focusing on data structures under extreme load (up to 2,000,000 records) and stability over repeated iterations.

## 2. Methodology
- **Data Schema**: Records only include `id`, `title`, `author`, and `date_added` as per requirements.
- **Hardware**: Local System (Windows)
- **Software**: Python 3.x, Recursive Merge Sort, Iterative Binary Search
- **Constraint Checks**: Recursion depth limits, Memory allocation failures, and Performance drift.

## 3. Scalability Results
| Dataset Size | Operation | Time (seconds) | Estimated Memory |
| :--- | :--- | :--- | :--- |
| 100 | Merge Sort (Random) | 0.00023040 | 0.01 MB |
| 100 | Binary Search | 0.00000080 | 0.01 MB |
| 100 | Universal Search | 0.00004240 | 0.01 MB |
| 1,000 | Merge Sort (Random) | 0.00314090 | 0.10 MB |
| 1,000 | Binary Search | 0.00000122 | 0.10 MB |
| 1,000 | Universal Search | 0.00045190 | 0.10 MB |
| 10,000 | Merge Sort (Random) | 0.04884020 | 1.03 MB |
| 10,000 | Binary Search | 0.00000190 | 1.03 MB |
| 10,000 | Universal Search | 0.00423630 | 1.03 MB |
| 100,000 | Merge Sort (Random) | 0.72376430 | 10.30 MB |
| 100,000 | Binary Search | 0.00000234 | 10.30 MB |
| 100,000 | Universal Search | 0.07563090 | 10.30 MB |
| 500,000 | Merge Sort (Random) | 4.43567670 | 51.66 MB |
| 500,000 | Binary Search | 0.00000308 | 51.66 MB |
| 500,000 | Universal Search | 0.37509300 | 51.66 MB |
| 1,000,000 | Merge Sort (Random) | 10.44375640 | 103.42 MB |
| 1,000,000 | Binary Search | 0.00000323 | 103.42 MB |
| 1,000,000 | Universal Search | 0.99700470 | 103.42 MB |
| 2,000,000 | Merge Sort (Random) | 21.50745260 | 207.07 MB |
| 2,000,000 | Binary Search | 0.00000329 | 207.07 MB |
| 2,000,000 | Universal Search | 1.68052580 | 207.07 MB |

## 4. Stability Test Results (100k Records)
The following table represents performance consistency across multiple consecutive runs.

| Iteration | Merge Sort (s) | Universal Search (s) | Status |
| :--- | :--- | :--- | :--- |
| 1 - 20 | Consistent (~0.6s) | Consistent (~0.04s) | **OK** |

## 5. System Failures & Constraints
No critical system failures were recorded within the tested parameters.

### 5.1 Bottleneck Analysis
- **Recursion Depth**: The current Merge Sort implementation is recursive. Without adjusting `sys.setrecursionlimit`, it fails at approximately 10^4 - 10^5 elements depending on stack state.
- **Memory Slicing**: `merge_sort(data[:mid])` creates a copy of the list. At 2M elements, this leads to $O(n \log n)$ space complexity, which can trigger a `MemoryError` even if total RAM is sufficient, due to fragmentation.
- **Linear Search**: At 2,000,000 elements, `universal_search` takes significant time, making it the primary UX bottleneck.

---

<p align="center">
  <img src="https://eldrex.landecs.org/logo/byte-me-maybe-final.svg" width="85" />
  <br><br>
  <strong>DSA Final Project 2026</strong>
  <br>
  <i>Group 1 • Byte Me Maybe</i>
</p>
