# **SMART LIBRARY SEARCH AND MANAGEMENT SYSTEM**

### *Applying the Binary Search Algorithm in a Library System for Navotas Polytechnic College*

**Course:** Data Structures and Algorithms  
**Group Number:** 1 – Byte Me Maybe  

**Group Members:**  
1. **Eldrex Delos Reyes Bula** – Lead Developer & Algorithm Architect  
2. **Mark Angelo Bernales** – UI/UX Designer  
3. **Joshua  – Documentation Lead  
4. [Member Name] – Quality Assurance  
5. [Member Name] – Data Analyst  
6. [Member Name] – System Integrator  
7. [Member Name] – Researcher  
8. [Member Name] – Researcher  
9. [Member Name] – Technical Writer  
10. [Member Name] – Project Coordinator  

**Date:** May 5, 2026  

---

## **ABSTRACT**

This study presents the development of a Smart Library Search and Management System designed to improve the efficiency of book retrieval and record management at Navotas Polytechnic College. The existing manual system is time-consuming and prone to human error, particularly as the number of records increases. 

To address this issue, the system implements the **Binary Search Algorithm**, which operates with a time complexity of $O(\log n)$, alongside an **Optimized Universal Search** for keyword-based discovery. The application was developed using **Python 3.x and the Tkinter GUI framework**, providing an intuitive interface that includes real-time tracking of book locations, shelf assignments, and borrowing availability. 

The system supports full **CRUD functionality (Create, Read, Update, Delete)**, ensuring effective data management while maintaining the sorted structure required for Binary Search. Results from version 1.0.2 show that the system significantly improves search speed, accuracy, and physical locating of materials through precise shelf-mapping.

---

# **I. INTRODUCTION**

## **The Scenario (Problem Statement)**

Libraries play a critical role in academic environments by providing access to learning resources. However, at Navotas Polytechnic College, book retrieval and record management are still performed manually. This results in inefficiencies such as slow searching, misplaced records, and increased reliance on staff assistance. 

A major pain point identified is the difficulty in knowing the exact physical location of a book once it is found in the records. Manual searching in the stacks without shelf-level data causes significant delays. As the number of books increases, the system becomes less manageable, leading to delays and reduced productivity. Therefore, a digital system is necessary to improve efficiency, accuracy, and accessibility.

---

## **The Algorithm**

This project utilizes the **Binary Search Algorithm** as the primary method for searching book records by ID. Binary Search is a divide-and-conquer algorithm that operates on a **sorted dataset**, repeatedly dividing the search space in half until the target value is found. 

Additionally, the system utilizes **Merge Sort ($O(n \log n)$)** to allow users to dynamically sort the library by Title, Author, or Date while keeping the underlying data structure optimized for search operations. For flexible keyword discovery, an **Optimized Universal Search** was implemented in v1.0.2 to scan IDs, Titles, Authors, Locations, and Shelf names in a single pass.

The algorithm selection is justified because:
* **Binary Search** operates in **$O(\log n)$** time complexity, making ID lookups near-instant.
* **Merge Sort** provides a stable, efficient sorting method for multi-criteria organization.
* It performs efficiently even with large datasets (stress-tested up to 2,000,000 records).

---

## **Project Objectives**

The project aims to:
1. Develop a functional desktop application using Python and Tkinter with a premium aesthetic.
2. Implement **Binary Search** for efficient book retrieval by ID.
3. Integrate **Location and Shelf tracking** to allow users to see exactly where books are.
4. Provide **Availability Status** (Available/Borrowed) for real-time inventory management.
5. Provide full CRUD functionality for managing records permanently via JSON.
6. Improve the efficiency and accuracy of library operations at Navotas Polytechnic College.

---

# **II. METHODS**

## **System Flow**

The system follows a structured workflow (v1.0.2):

1. **Input**  
   The user enters book details: **ID, Title, Author, Location, and Shelf assignment**, along with its **Availability status**.

2. **Processing**  
   * Data is stored and maintained in a **sorted JSON database**.
   * The system ensures the list is always sorted by ID for Binary Search compatibility.
   * Universal search logic pre-processes queries to scan all relevant fields simultaneously.

3. **Search Execution**  
   * **For ID Search**: The system identifies the middle element, compares it with the target, and eliminates half the dataset iteratively ($O(\log n)$).
   * **For Universal Search**: The system performs a single-pass filter across all book metadata.

4. **Output**  
   Results are displayed instantly in a modern, status-aware table (Treeview). If no results are found, the system provides dynamic "Not Found" feedback.

5. **Data Persistence**  
   All changes are saved to `data.json` to ensure data remains persistent across sessions.

---

## **Technical Design**

The system is developed using:
* **Python 3.x** as the programming language.
* **Tkinter (and ttk)** for the graphical user interface.
* **Pillow (PIL)** for high-resolution logo and icon rendering.

### **Component Interaction**
* **Input Panel**: Uses a two-column grid for efficient data entry of ID, Title, Author, Location, and Shelf.
* **Availability Toggle**: A checkbox allows quick status updates (Available/Borrowed).
* **Search Bar**: A real-time filtered search entry that updates the table as the user types.
* **Treeview Table**: Displays 7 columns: ID, Title, Author, Location, Shelf, Status, and Date Added.

### **CRUD Integration**
* **Create:** Adds a new record, automatically timestamping the entry and saving it to the sorted JSON file.
* **Read:** Uses Binary Search or Universal Search for rapid retrieval.
* **Update:** Modifies book details, including its physical location or availability status.
* **Delete:** Removes a record while maintaining the integrity of the JSON structure.

---

# **III. RESULTS**

## **GUI Gallery**

The system v1.0.2 features a **Indigo & Slate theme**, including:
* Clear sections for Management and Search.
* Status-coded table rows (Available/Borrowed).
* Visual feedback for empty search states.

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/7008dd50-be9f-4208-ab5e-f1c797f007fe" />
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/61d041ae-73fa-4d2f-921a-49ec37754b31" />
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/1f1e9ec1-9436-49c8-82cb-24d4ae310770" />


---

## **CRUD Verification**

| Operation | Description                               | Status |
| --------- | ----------------------------------------- | ------ |
| **Create**| Add book with ID, Location, and Shelf.    | **PASSED** |
| **Read**  | Search using Binary & Universal Search.   | **PASSED** |
| **Update**| Modify shelf location & availability.     | **PASSED** |
| **Delete**| Remove record and update JSON.            | **PASSED** |

---

# **IV. DISCUSSION**

## **Performance Analysis**

The system demonstrates high efficiency through the use of the **Binary Search Algorithm**. With a time complexity of **$O(\log n)$**, ID-based lookups are nearly instantaneous regardless of library size. 

In version 1.0.2, the implementation was further optimized to handle extreme stress tests. By increasing recursion limits and refining search passes, the system remains responsive even with datasets exceeding **2,000,000 records**, as documented in the internal Performance Report.

---

## **Real-World Application**

The system improves daily library operations by:
* **Precision Locating**: The new "Shelf" and "Location" fields eliminate time wasted searching physical stacks.
* **Inventory Clarity**: The "Availability" status prevents students from searching for books that are already out.
* **Scalability**: The robust sorting and searching algorithms allow the college library to grow without slowing down.
* **Modernization**: Transitioning from a manual system to a digital one reduces human error and reliance on staff memory.

---

## **Conclusion**

The Smart Library Search and Management System successfully applies Binary Search and other fundamental algorithms to a real-world institutional problem. The v1.0.2 update ensures the system is not just a digital record, but a practical tool for physical book retrieval. 

It demonstrates how theoretical concepts in Data Structures and Algorithms can be effectively applied to improve academic efficiency and resource accessibility.

---

## **REFERENCES (APA FORMAT)**

Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (2022). *Introduction to Algorithms* (4th ed.). MIT Press.

GeeksforGeeks. (2023). *Binary Search*. https://www.geeksforgeeks.org/binary-search/

Lutz, M. (2013). *Learning Python* (5th ed.). O'Reilly Media.

Python Software Foundation. (2024). *tkinter — Python interface to Tcl/Tk*. https://docs.python.org/3/library/tkinter.html

---

## **APPENDIX: GROUP CONTRIBUTION TABLE**

| Member Name | Role           | Tasks Completed                     | % Contribution |
| ----------- | -------------- | ----------------------------------- | -------------- |
| Eldrex      | Lead Developer | Algorithm, v1.0.2 Features, Logic   | 10%            |
| Member 2    | UI Designer    | v1.0.2 Premium Theme, Layout        | 10%            |
| Member 3    | Documentation  | Paper writing & APA Citations       | 10%            |
| Member 4    | QA Tester      | CRUD & Stress Testing               | 10%            |
| Member 5    | Analyst        | Performance Data Validation         | 10%            |
| Member 6    | Integrator     | Code merging & Asset management     | 10%            |
| Member 7    | Researcher     | Algorithm efficiency analysis       | 10%            |
| Member 8    | Researcher     | User requirement gathering          | 10%            |
| Member 9    | Writer         | Editing & Final Formatting          | 10%            |
| Member 10   | Coordinator    | Task management & Scheduling        | 10%            |
