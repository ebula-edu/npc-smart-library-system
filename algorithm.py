def binary_search(data, target_id):
    """
    Perform binary search on a list of dictionaries sorted by 'id'.
    Returns the dictionary if found, else None.
    """
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

def merge_sort(data, key, reverse=False):
    """
    Perform Merge Sort (O(n log n)) on a list of dictionaries.
    """
    if len(data) <= 1:
        return data
    
    mid = len(data) // 2
    left = merge_sort(data[:mid], key, reverse)
    right = merge_sort(data[mid:], key, reverse)
    
    return _merge(left, right, key, reverse)

def _merge(left, right, key, reverse):
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        val_l = left[i].get(key)
        val_r = right[j].get(key)
        
        if isinstance(val_l, str): val_l = val_l.lower()
        if isinstance(val_r, str): val_r = val_r.lower()
        
        if not reverse:
            if val_l <= val_r:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        else:
            if val_l >= val_r:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
                
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def universal_search(data, query):
    """
    Filter data based on query matching ID, Title, or Author.
    Returns a filtered list of books.
    """
    if not query:
        return data
        
    query = str(query).lower()
    filtered_books = []
    
    for book in data:
        if (query in str(book.get("id")).lower() or 
            query in str(book.get("title", "")).lower() or 
            query in str(book.get("author", "")).lower()):
            filtered_books.append(book)
            
    return filtered_books
