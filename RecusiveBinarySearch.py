def RBS(lst, target, left=0, right=None):
    if right is None:  # Initialize right boundary on first call
        right = len(lst) - 1
    
    if left > right:  # Base case: target not found
        return None

    midpoint = (left + right) // 2  # Calculate the midpoint

    if lst[midpoint] == target:  # Target found
        return midpoint
    elif lst[midpoint] < target:  # Search in the right half
        return RBS(lst, target, midpoint + 1, right)
    else:  # Search in the left half
        return RBS(lst, target, left, midpoint - 1)

def validate(result):
    if result is not None:
        print("The Target index is:", result)
    else:
        print("The Target was not found.")

# Example usage
result = RBS([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3)
validate(result)
