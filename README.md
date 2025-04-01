# Automatic-deadlock-detection-Tool
this is a python project...for detecting deadlock in a system log
Deadlocks in multi-threaded applications can cause systems to freeze and reduce performance. This Automated Deadlock Detection Tool helps identify and visualize deadlocks using a user-friendly GUI, making it easier for developers to debug concurrency issues




Module-Wise Breakdown
Module 1: Deadlock Detection Engine (Backend)

1. Detect potential deadlocks using process dependency graphs.
2. Identify circular wait conditions in resource allocation.
Module 1 Responsibilities:
• Parse process logs to extract resource allocation details.
• Construct a Resource Allocation Graph (RAG).
• Use Cycle Detection Algorithms to find deadlocks.
• Suggest deadlock resolution strategies.
Module 2: Visualization & Data Representation
1. Present detected deadlocks in an understandable manner.
2. Show a real-time graph-based visualization of process
dependencies.
Module 2 Responsibilities:
• Generate Directed Graphs to illustrate process dependencies.
• Display highlighted cycles in the graph for detected
deadlocks.
• Show real-time resource allocation and process states.
Module 3: User Interface (GUI)
1. Provide a simple and interactive UI for users to analyze
deadlocks.
2. Allow users to upload process logs or run live monitoring.
Module 3 Responsibilities:
• Upload system logs for manual analysis.
• Display live process dependency graphs.
• Provide resolution suggestions in an easy-to-read format.
• Allow filtering of deadlock occurrences based on severity.
