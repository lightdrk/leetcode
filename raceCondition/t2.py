import multiprocessing

# Shared variable (use a Manager to share state between processes)
def increment(counter):
    for _ in range(100000):
        counter.value += 1  # Not thread-safe in multiprocessing

if __name__ == "__main__":
    # Create a manager for shared state
    with multiprocessing.Manager() as manager:
        # Shared counter
        counter = manager.Value('i', 0)
        
        # Create two processes
        process1 = multiprocessing.Process(target=increment, args=(counter,))
        process2 = multiprocessing.Process(target=increment, args=(counter,))
        
        # Start both processes
        process1.start()
        process2.start()
        
        # Wait for both processes to finish
        process1.join()
        process2.join()
        
        # Print the final counter value
        print(f"Final counter value: {counter.value}")

