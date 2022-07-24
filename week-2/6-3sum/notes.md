I guarantee that I will not be able to solve this if I never faced this question before LOL 

Steps: 

1. Sort the array 
2. For each element in the array, use two pointers approach 
   1. Start from start_pointer = current_index+1, last_pointer = len(array)
   2. if `cur_element + array[start_pointer] + array[last_pointer] == 0`, append the result
   3. If < 0, increase start_pointer += 1
   4. if > 0, decrease last_pointer -= 1
   5. stop when start_pointer == last_pointer

