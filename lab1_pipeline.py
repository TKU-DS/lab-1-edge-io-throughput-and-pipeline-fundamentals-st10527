import time
import random
import csv
import os

# ==========================================
# Data Engineering - Lab 1: Edge I/O Throughput Test (SOLUTION)
# ==========================================

DATA_SIZE = 50000  # Simulate 50,000 sensor records
FILE_NAME = "sensor_data.csv"

def generate_sensor_data(num_records):
    """Simulates streaming data from an edge sensor."""
    print(f"[*] Generating {num_records} simulated sensor records...")
    data = []
    for _ in range(num_records):
        data.append([
            time.time(),                      
            round(random.uniform(20, 35), 2), 
            round(random.uniform(40, 90), 2)  
        ])
    return data

def write_data_line_by_line(data):
    """[Poor Architecture] Opens and closes the file for every single record."""
    print("\n[*] Test 1: Line-by-Line Write...")
    
    # TODO 1: Record start time
    start_time = time.time()  # <--- 解答在這
    
    for row in data:
        with open(FILE_NAME, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(row)
            
    # TODO 2: Record end time and calculate duration
    end_time = time.time()    # <--- 解答在這
    duration = end_time - start_time
    
    print(f"    -> [Result] Line-by-line write duration: {duration:.4f} seconds")


def write_data_in_bulk(data):
    """[Good Architecture] Buffers data in memory and writes to disk in a single batch."""
    print("\n[*] Test 2: Bulk/Batch Write...")
    
    # TODO 3: Record start time
    start_time = time.time()  # <--- 解答在這
    
    with open(FILE_NAME, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data) 
        
    # TODO 4: Record end time and calculate duration
    end_time = time.time()    # <--- 解答在這
    duration = end_time - start_time
    
    print(f"    -> [Result] Bulk write duration: {duration:.4f} seconds")


if __name__ == "__main__":
    if os.path.exists(FILE_NAME):
        os.remove(FILE_NAME)

    print("=== Edge Pipeline I/O Benchmark Started ===")
    
    # 1. Generate test data
    sensor_data = generate_sensor_data(DATA_SIZE)
    
    # 2. Execute Test 1
    write_data_line_by_line(sensor_data)
    
    # Clean up
    if os.path.exists(FILE_NAME):
        os.remove(FILE_NAME)
        
    # 3. Execute Test 2
    write_data_in_bulk(sensor_data)
    
    print("\n===========================================")
    print("Experiment completed!")
