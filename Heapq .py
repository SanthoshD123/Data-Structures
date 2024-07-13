import heapq

# Create an empty priority queue (heap)
priority_queue = []

# Function to add an item with a priority
def add_task(priority, task):
    heapq.heappush(priority_queue, (priority, task))

# Function to pop the highest priority task
def pop_task():
    return heapq.heappop(priority_queue)

# Add some tasks with priorities
add_task(2, "write code")
add_task(1, "write tests")
add_task(3, "debug code")

# Pop tasks by priority
print(pop_task())  # Output: (1, "write tests")
print(pop_task())  # Output: (2, "write code")
print(pop_task())  # Output: (3, "debug code")
