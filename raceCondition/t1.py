import threading

# Shared variable
counter = 0

# Function that increments the counter
def increment():
    global counter
    for _ in range(100000):
        counter += 1  # Not thread-safe

# Create two threads that will modify the counter
thread1 = threading.Thread(target=increment)
thread2 = threading.Thread(target=increment)

# Start both threads
thread1.start()
thread2.start()

# Wait for both threads to complete
thread1.join()
thread2.join()

# Print the final value of counter
print(f"Final counter value: {counter}")

