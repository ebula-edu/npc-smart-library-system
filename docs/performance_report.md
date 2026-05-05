<img width="600" height="400" alt="binary-and-linear-search-animations" src="https://github.com/user-attachments/assets/8c4b4461-7dc3-4f09-8e6e-0bde287d4aa3" />

# Extreme Performance & System Constraint Analysis

[![Performance Testing](https://img.shields.io/badge/Testing-Performance-blue?style=for-the-badge&logo=python)](tests/performance_test.py)

## 1. Abstract
This report documents the stress testing of the DSA Final Project system, focusing on data structures under extreme load (up to 2,000,000 records) and stability over repeated iterations.

## 2. Methodology
- **Data Schema**: Records include `id`, `title`, `author`, `location`, `shelf`, `available`, and `date_added` (v1.0.2).
- **Hardware**: Local System (Windows)
- **Software**: Python 3.x, Optimized Recursive Merge Sort, Iterative Binary Search, Optimized Universal Search
- **Constraint Checks**: Recursion depth limits, Memory allocation failures, and Performance drift.

## 3. Scalability Results
| Dataset Size | Operation | Time (seconds) | Estimated Memory |
| :--- | :--- | :--- | :--- |
| 100 | Merge Sort (Random) | 0.00023020 | 0.01 MB |
| 100 | Binary Search | 0.00000078 | 0.01 MB |
| 100 | Universal Search | 0.00005800 | 0.01 MB |
| 1,000 | Merge Sort (Random) | 0.00328120 | 0.10 MB |
| 1,000 | Binary Search | 0.00000148 | 0.10 MB |
| 1,000 | Universal Search | 0.00058570 | 0.10 MB |
| 10,000 | Merge Sort (Random) | 0.04909320 | 1.03 MB |
| 10,000 | Binary Search | 0.00000179 | 1.03 MB |
| 10,000 | Universal Search | 0.00614630 | 1.03 MB |
| 100,000 | Merge Sort (Random) | 0.71871090 | 10.30 MB |
| 100,000 | Binary Search | 0.00000227 | 10.30 MB |
| 100,000 | Universal Search | 0.08103540 | 10.30 MB |
| 500,000 | Merge Sort (Random) | 4.77777680 | 51.66 MB |
| 500,000 | Binary Search | 0.00000271 | 51.66 MB |
| 500,000 | Universal Search | 0.44425830 | 51.66 MB |
| 1,000,000 | Merge Sort (Random) | 10.58086070 | 103.42 MB |
| 1,000,000 | Binary Search | 0.00000350 | 103.42 MB |
| 1,000,000 | Universal Search | 0.92582640 | 103.42 MB |
| 2,000,000 | Merge Sort (Random) | 22.94351230 | 207.07 MB |
| 2,000,000 | Binary Search | 0.00000330 | 207.07 MB |
| 2,000,000 | Universal Search | 2.07454800 | 207.07 MB |

## 4. Stability Test Results (100k Records)
The following table represents performance consistency across multiple consecutive runs.

| Iteration | Merge Sort (s) | Universal Search (s) | Status |
| :--- | :--- | :--- | :--- |
| 1 - 20 | Consistent (~0.6s) | Consistent (~0.04s) | **OK** |

## 5. System Failures & Constraints
No critical system failures were recorded within the tested parameters.

### 5.1 Bottleneck Analysis
- **Recursion Depth**: Resolved in v1.0.2 by increasing `sys.setrecursionlimit`. However, iterative approaches are still preferred for safety.
- **Memory Slicing**: Still present due to recursive architecture; $O(n \log n)$ space complexity remains a concern for extremely constrained environments.
- **Universal Search**: Optimized in v1.0.2 using string concatenation and single-pass matching, significantly reducing overhead for large datasets.

<br>

<p align="center">
  <img src="https://eldrex.landecs.org/logo/byte-me-maybe-final.svg" width="85" />
  <br><br>
  <strong>DSA Final Project 2026</strong>
  <br>
  <i>Group 1 • Byte Me Maybe</i>
</p>
