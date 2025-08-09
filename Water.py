#Container with most water
def max_area(height):
    # Initialize two pointers at the ends of the array
    left = 0
    right = len(height) - 1
    max_water = 0
    
    # Loop until the two pointers meet
    while left < right:
        # Calculate the current area
        width = right - left
        min_height = min(height[left], height[right])
        current_area = width * min_height
        
        # Update max_water if current_area is greater
        max_water = max(max_water, current_area)
        
        # Move the pointer at the smaller height inward
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    
    return max_water
heights = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(max_area(heights))
