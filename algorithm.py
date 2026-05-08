def binary_search(data, target_id):
    low = 0
    high = len(data) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_id = data[mid].get("id")
        
        if mid_id == target_id:
            return data[mid]
        elif mid_id < target_id:
            low = mid + 1
        else:
            high = mid - 1

    return None

def universal_search(data, query):
    if not query:
        return data
        
    query = str(query).lower()
    
    def matches(book):
        searchable_content = (
            f"{book.get('id')} "
            f"{book.get('title', '')} "
            f"{book.get('author', '')} "
            f"{book.get('location', '')} "
            f"{book.get('shelf', '')}"
        ).lower()
        return query in searchable_content

    return [book for book in data if matches(book)]
