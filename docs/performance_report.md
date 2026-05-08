<img width="600" height="400" alt="binary-and-linear-search-animations" src="https://github.com/user-attachments/assets/8c4b4461-7dc3-4f09-8e6e-0bde287d4aa3" />

# Extreme Performance & System Constraint Analysis

[![Performance Testing](https://img.shields.io/badge/Testing-Performance-blue?style=for-the-badge&logo=python)](tests/performance_test.py)

## 1. Abstract
This report documents the stress testing of the DSA Final Project system, focusing on the efficiency, scalability, and stability of the Binary Search Algorithm under extreme data loads of up to 2,000,000 records. The analysis evaluates retrieval speed, memory usage, and system responsiveness during repeated operations and large dataset processing.

---

## 2. Methodology

- **Data Schema**: Records include `id`, `title`, `author`, `location`, `shelf`, `available`, and `date_added` (v1.0.2).
- **Hardware**: Local System (Windows)
- **Software**: Python 3.x, Iterative Binary Search, and Optimized Universal Search
- **Constraint Checks**:
  - Large dataset handling
  - Memory allocation stability
  - Performance consistency
  - System responsiveness under repeated execution

---

## 3. Scalability Results

| Dataset Size | Binary Search | Linear Search | Estimated Memory |
| :--- | :--- | :--- | :--- |
| 100 | 0.00000078 | 0.00005800 | 0.01 MB |
| 1,000 | 0.00000148 | 0.00058570 | 0.10 MB |
| 10,000 | 0.00000179 | 0.00614630 | 1.03 MB |
| 100,000 | 0.00000227 | 0.08103540 | 10.30 MB |
| 500,000 | 0.00000271 | 0.44425830 | 51.66 MB |
| 1,000,000 | 0.00000350 | 0.92582640 | 103.42 MB |
| 2,000,000 | 0.00000330 | 2.07454800 | 207.07 MB |

### Observations

- Binary Search maintained extremely fast retrieval times even as dataset size increased.
- Universal Search performance scaled proportionally with dataset growth while remaining stable.
- Memory consumption increased predictably based on dataset size.
- The system remained responsive during high-load testing conditions.

---

## 4. Stability Test Results (100k Records)

The following table represents performance consistency across multiple consecutive runs.

| Iteration | Binary Search (s) | Linear Search (s) | Status |
| :--- | :--- | :--- | :--- |
| 1 - 20 | Consistent (~0.000003s) | Consistent (~0.04s) | **OK** |

### Stability Analysis

- No performance degradation was observed during repeated executions.
- Binary Search maintained stable logarithmic retrieval performance.
- Universal Search operations remained responsive across all test iterations.
- No crashes or unexpected interruptions occurred during testing.

---

## 5. System Failures & Constraints

No critical system failures were recorded within the tested parameters.

### 5.1 Bottleneck Analysis

- **Large Dataset Handling**: The system remained operational and responsive while processing millions of records.
- **Memory Usage**: Large datasets required increased memory allocation, especially during data organization and retrieval operations.
- **Linear Search Optimization**: v1.0.2 improved search efficiency using optimized string concatenation and single-pass matching techniques.
- **Binary Search Efficiency**: The logarithmic time complexity of Binary Search ensured consistent and scalable retrieval performance across all dataset sizes.

---

## 6. Conclusion

The performance analysis demonstrates that the Smart Library Search and Management System can efficiently handle large-scale datasets while maintaining fast and stable retrieval operations. The Binary Search Algorithm consistently delivered high-speed record searching with minimal performance degradation as data volume increased.

The results confirm that Binary Search is highly suitable for scalable library management systems requiring efficient and reliable book retrieval operations. Additionally, the system maintained operational stability under repeated stress testing and large dataset conditions.

<br>

<p align="center">
  <img src="https://eldrex.landecs.org/logo/byte-me-maybe-final.svg" width="85" />
  <br><br>
  <strong>DSA Final Project 2026</strong>
  <br>
  <i>Group 1 • Byte Me Maybe</i>
</p>
