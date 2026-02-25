# Lab 1: Edge I/O Throughput & Pipeline Fundamentals

## 📌 Objective
Welcome to the first lab of Data Engineering. In edge computing environments, hardware resources (CPU, RAM, Disk I/O) are strictly limited. 

This lab aims to physically demonstrate the performance penalty of poor architectural choices. You will benchmark two different data writing strategies (Line-by-Line vs. Bulk Write) to understand why I/O operations are often the most critical bottleneck in an edge data pipeline.

## 🛠️ Environment Setup
We will use **GitHub Codespaces** to simulate a constrained edge device (2-core CPU, limited RAM).
1. Click the green `<> Code` button at the top right of this repository.
2. Select the **Codespaces** tab.
3. Click **Create codespace on main** (or open your existing codespace).
4. Wait for the cloud VS Code environment to initialize.

## 🚀 Instructions
1. Open the `lab1_pipeline.py` file in your Codespace.
2. Read the comments carefully to understand the simulated sensor data generation.
3. Locate the `TODO 1` to `TODO 4` markers.
4. Import the `time` module (already done for you) and use `time.time()` to measure the execution duration of both writing methods.
5. Run the script in the terminal:

    ```bash
    python lab1_pipeline.py
    ```

6. Observe the terminal output. You should see a massive delta (time difference) between Test 1 and Test 2.

## 🧠 Reflection Questions (Think as an Architect)

*While you don't need to submit a formal report for this week, consider the following architectural trade-offs:*

1. **The OS Level**: Why is opening and closing a file (Line-by-Line) orders of magnitude slower than a Bulk Write? What is the operating system doing behind the scenes?
2. **The Edge Constraint**: If Bulk Write is so much faster, why don't we just buffer a whole day's worth of sensor data in RAM before writing to the disk? What happens to the data in RAM if the edge device (e.g., a drone or IoT sensor) loses power unexpectedly?

## ✅ Submission Guidelines

To complete this lab:

1. Ensure your `lab1_pipeline.py` runs successfully and prints the correct durations.
2. Commit your changes:

    ```bash
    git add lab1_pipeline.py
    git commit -m "Complete Lab 1 I/O benchmark"
    ```

3. Push the code back to your GitHub repository:

    ```bash
    git push origin main
    ```

*Note: Do NOT commit the generated `sensor_data.csv` file. Our `.gitignore` should handle this automatically.*
