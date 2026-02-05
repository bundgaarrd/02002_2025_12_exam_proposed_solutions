# Opgave 6: (Navigation Tracking)
def navigation_tracking(instructions):
    visited = [] 
    visited_indices = [] # list to keep track of visited indices

    # Maybe this task could be solved with a dictionary instead
    searching = True
    index = 0
    while searching:  # Searching until done (risk of infinity loop)      

        # If index is out of bound
        if ((index + instructions[index]) >= len(instructions)):
            visited.append(instructions[index])
            visited_indices.append(index)

            difference_index = (len(instructions) - index) - 1
            new_instruction = instructions[index] - difference_index

            index = new_instruction - 1
        else:
            visited.append(instructions[index])
            visited_indices.append(index)

            index += instructions[index]

        if (index in visited_indices):
            searching = False
    
    return visited