"""
Explanation:

* Binary search is an algorithm; its input is a sorted list of elements. 
* If an element you’re looking for is in that list, binary search returns the position where it’s located. 
* Otherwise, binary search returns null.

-- If you are guessing the number 64, one way to find that would to check for every number starting 1 until
   you reach 64.
   -- Another way to approach this problem would be to Start with 50. 
   -- 50 is much smaller than 64 then you are free to eliminate every number before that. 
   -- Next guess: 75. Now eliminate everything on the right. 

Big O Notation: 
    -- Think of log_10 100 as asking: 'What power do I need to raise 10 to in order to get 100?'
    -- Since 10² = 10 × 10 = 100, we know that log_10 100 = 2.
    -- In the context of Big 0, log always means log_2
-- For simple search: In a list of 128, worst case, we'd have to search all the 128 numbers.
-- For Binary search: We'll have to check log n elements in the worst case. Log 128 == 7 i.e. 2^7 == 128

"""

from typing import List, Optional, TypeVar
T = TypeVar('T', int, float, str)

class BinarySearch:
    @staticmethod
    def search_iterative(list_of_items: List[int], item: int) -> Optional[int]:
        """Search for an item in a sorted list using iteration.
        
        Args:
            1. list_of_items: A sorted list of integers
            2. item: The integer to find
            
        Returns:
            3. Optional[int]: Index of item if found, None otherwise
        """
        low = 0                           # First index of the list
        high = len(list_of_items) - 1     # Last index of the list      

        while low <= high:
            mid = (low + high) // 2       # If there were 11 items then low == 0, high == 10. mid would be 5.
            guess = list_of_items[mid]
            
            if guess == item:
                return mid
            if guess > item:              # If we are guessing 8
                high = mid - 1
            else:
                low = mid + 1

        return None

    @staticmethod
    def search_recursive(list_of_items: List[int], low: int, high: int, item: int) -> Optional[int]:
        """Search for an item in a sorted list using recursion.
        
        Args:
            1. list_of_items: A sorted list of integers
            2. low: Lower bound index
            3. high: Upper bound index
            4. item: The integer to find
            
        Returns:
            5. Optional[int]: Index of item if found, None otherwise
        """
        if high >= low:
            mid = (high + low) // 2
            guess = list_of_items[mid]

            if guess == item:
                return mid
            elif guess > item:
                return BinarySearch.search_recursive(list_of_items, low, mid - 1, item)
            else:
                return BinarySearch.search_recursive(list_of_items, mid + 1, high, item)
        else:
            return None


def example_usage():
    """Demonstrate how to use the BinarySearch class."""
    # Create a sample sorted list
    sample_list = [1, 3, 5, 7, 9]
    
    print("Binary Search Examples:")
    print("-" * 20)
    
    # Example 1: Finding an existing element using iterative search
    target = 3
    result = BinarySearch.search_iterative(sample_list, target)
    print(f"Looking for {target} iteratively:")
    print(f"Found at index: {result}")  # Should print 1
    
    # Example 2: Looking for a non-existent element
    target = -1
    result = BinarySearch.search_iterative(sample_list, target)
    print(f"\nLooking for {target} iteratively:")
    print(f"Result: {result}")  # Should print None
    
    # Example 3: Using recursive search
    target = 7
    high = len(sample_list) - 1
    result = BinarySearch.search_recursive(sample_list, 0, high, target)
    print(f"\nLooking for {target} recursively:")
    print(f"Found at index: {result}")  # Should print 3


if __name__ == "__main__":
    example_usage()

# %%
list_of_items = [1,2,3,4,5,6,7]

booze = len(list_of_items)
high = len(list_of_items) - 1

print(booze)
print(high)
# %%
