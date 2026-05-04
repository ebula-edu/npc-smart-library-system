import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from algorithm import binary_search, merge_sort

def test_binary_search():
    data = [
        {"id": 10, "title": "A"},
        {"id": 20, "title": "B"},
        {"id": 30, "title": "C"},
        {"id": 40, "title": "D"}
    ]
    
    print("Testing Binary Search...")
    assert binary_search(data, 20)["title"] == "B"
    assert binary_search(data, 25) is None
    assert binary_search(data, 10)["title"] == "A"
    assert binary_search(data, 40)["title"] == "D"
    print("Binary Search: PASSED")

def test_merge_sort():
    data = [
        {"id": 3, "title": "Zebra", "author": "C"},
        {"id": 1, "title": "Apple", "author": "A"},
        {"id": 2, "title": "Banana", "author": "B"}
    ]
    
    print("\nTesting Merge Sort...")
    

    sorted_id = merge_sort(data, "id")
    assert sorted_id[0]["id"] == 1
    assert sorted_id[2]["id"] == 3
    print("Sort by ID: PASSED")

    sorted_title = merge_sort(data, "title")
    assert sorted_title[0]["title"] == "Apple"
    assert sorted_title[2]["title"] == "Zebra"
    print("Sort by Title: PASSED")

    sorted_author = merge_sort(data, "author", reverse=True)
    assert sorted_author[0]["author"] == "C"
    assert sorted_author[2]["author"] == "A"
    print("Sort by Author (Desc): PASSED")

if __name__ == "__main__":
    test_binary_search()
    test_merge_sort()
    print("\nAll tests passed!")
