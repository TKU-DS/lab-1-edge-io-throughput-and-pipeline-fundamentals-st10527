import time
import random
import csv
import os

# ==========================================
# Data Engineering - Lab 1: Edge I/O Throughput Test
# ==========================================
# Objective: Experience a common performance bottleneck on Edge devices: Disk I/O.
# Task: Add time.time() at the designated TODO markers to calculate and compare
#       the execution time of two different writing architectures.

DATA_SIZE = 50000  # Simulate 50,000 sensor records
FILE_NAME = "sensor_data.csv"

def generate_sensor_data(num_records):
    """Simulates streaming data from an edge sensor (e.g., temperature/humidity)."""
    print(f"[*] Generating {num_records} simulated sensor records...")
    data = []
    for _ in range(num_records):
        data.append([
            time.time(),                      # Timestamp
            round(random.uniform(20, 35), 2), # Temperature (Celsius)
            round(random.uniform(40, 90), 2)  # Humidity (%)
        ])
    return data

def write_data_line_by_line(data):
    """
    [Poor Architecture Demonstration] 
    Opens and closes the file for every single record. 
    Extremely I/O intensive and heavily penalized on Edge devices.
    """
    print("\n[*] Test 1: Line-by-Line Write...")
    
    # TODO 1: Add a variable 'start_time' below to record the starting time.
    # Hint: Use time.time()
    
    
    for row in data:
        # Opening the file in every iteration is an anti-pattern for edge systems.
        with open(FILE_NAME, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(row)
            
    # TODO 2: Add a variable 'end_time' below, and calculate the total duration (in seconds).
    # Hint: duration = end_time - start_time
    
    # print(f"    -> [Result] Line-by-line write duration: {duration:.4f} seconds")


def write_data_in_bulk(data):
    """
    [Good Architecture Demonstration] 
    Buffers data in memory and writes to disk in a single batch.
    """
    print("\n[*] Test 2: Bulk/Batch Write...")
    
    # TODO 3: Add a variable 'start_time' below to record the starting time.
    
    
    # Opens the file only once and dumps the entire array from memory to disk.
    with open(FILE_NAME, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data) 
        
    # TODO 4: Add a variable 'end_time' below, and calculate the total duration (in seconds).
    
    # print(f"    -> [Result] Bulk write duration: {duration:.4f} seconds")


if __name__ == "__main__":
    # Ensure a clean environment before testing
    if os.path.exists(FILE_NAME):
        os.remove(FILE_NAME)

    print("=== Edge Pipeline I/O Benchmark Started ===")
    
    # 1. Generate test data in memory
    sensor_data = generate_sensor_data(DATA_SIZE)
    
    # 2. Execute Test 1
    write_data_line_by_line(sensor_data)
    
    # Clean up the file to ensure fair conditions for Test 2
    if os.path.exists(FILE_NAME):
        os.remove(FILE_NAME)
        
    # 3. Execute Test 2
    write_data_in_bulk(sensor_data)
    
    print("\n===========================================")
    print("Experiment completed! Observe the difference in execution time between the two architectures.")
    print("After completing the TODOs, commit and push your code back to your GitHub Repository.")
