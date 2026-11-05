# 📚 E-Library Management System
---

### 👩‍💻 Author

**Drashti Vasani**

---

## 📌 Project Overview

The **E-Library Management System** is a menu-driven Python application designed to analyze library borrowing transactions.

This project uses **Pandas and NumPy** for data processing, cleaning, filtering, and statistical analysis. It also uses **Matplotlib and Seaborn** to generate meaningful charts and visual reports.

The entire application is developed using an object-oriented approach with a `LibraryDashboard` class.

### 🎯 Project Objectives

- Manage and analyze library borrowing records.
- Calculate important statistical information.
- Filter transactions based on book genres.
- Generate genre-wise reports.
- Analyze user and book borrowing patterns.
- Create attractive data visualizations.

---

## ✨ Key Features

| No. | Feature | Description |
|---|---|---|
| 1 | 📂 Load Dataset | Load and validate CSV datasets. |
| 2 | 📊 Calculate Statistics | Calculate average, maximum, minimum and standard deviation. |
| 3 | 🔍 Filter Transactions | Search transactions by book genre. |
| 4 | 📑 Generate Report | Generate genre-wise borrowing reports. |
| 5 | 📈 Data Analysis | Perform detailed dataset analysis. |
| 6 | 📉 Data Visualization | Generate four different charts. |
| 7 | 📋 Show Dataset | Display all library transaction records. |
| 8 | 🚪 Exit | Close the application. |

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| 🐍 Python | Core programming language |
| 🐼 Pandas | Data manipulation and analysis |
| 🔢 NumPy | Numerical calculations |
| 📊 Matplotlib | Data visualization |
| 🎨 Seaborn | Statistical visualization |

---

## 📦 Required Libraries

Install the following libraries before running the project.

```bash
pip install pandas numpy matplotlib seaborn
```

---

## 📁 Project Structure

```text
E-Library-Management-System/
│
├── 📄 library_dashboard.py
│
├── 📊 library_transactions.csv
│
├── 📑 library_report.csv
│
├── 📂 Library_Charts/
│   ├── Top_5_Books.png
│   ├── Monthly_Borrowing.png
│   ├── Genre_Distribution.png
│   └── Borrowing_Heatmap.png
│
└── 📘 README.md
```

---

## 📋 CSV Dataset Format

The application uses a CSV dataset containing library borrowing transactions.

### Required Dataset Columns

| Column Name | Description |
|---|---|
| Transaction ID | Unique transaction identifier |
| Date | Borrowing transaction date |
| User ID | Library user identification |
| Book Title | Name of the borrowed book |
| Book Genre | Category of the book |
| User Type | Student, Faculty or Public |
| Borrowing Time | Time of borrowing |
| Borrowing Duration (Days) | Total borrowing duration |
| Due Date | Expected book return date |
| Return Date | Actual book return date |

**Data Cleaning Operations:**

- Remove duplicate records.
- Handle missing values.
- Validate required columns.
- Convert date and numeric columns into appropriate data types.
- Remove invalid records.

---

## 🚀 How to Run the Project

Follow these simple steps:

**Step 1:** Download or clone the project.

**Step 2:** Install the required libraries.

```bash
pip install pandas numpy matplotlib seaborn
```

**Step 3:** Open the project folder in VS Code, Jupyter Notebook or any Python IDE.

**Step 4:** Run the Python file.

```bash
python library_dashboard.py
```

**Step 5:** Select an option from the main menu.

**Step 6:** Enter the CSV dataset path when requested.

---

## 🖥️ Main Menu

```text
=================================================
           📚 E-LIBRARY MANAGEMENT SYSTEM
=================================================

1. Load Dataset
2. Calculate Statistics
3. Filter Transactions
4. Generate Report
5. Data Analysis
6. Data Visualization
7. Show Dataset
8. Exit

=================================================

Enter your choice:
```

---

## 📊 Sample Output

### 1️⃣ Load Dataset

```text
Enter your choice: 1

Enter CSV file path: library_transactions.csv

Dataset loaded successfully!

Total Records Loaded: 80
```

### 2️⃣ Calculate Statistics

```text
========== STATISTICS ==========

Total Transactions: 80

Average Borrowing Duration: 13.6125

Maximum Borrowing Duration: 28

Minimum Borrowing Duration: 1

Standard Deviation: 7.459044426064239
```

### 3️⃣ Filter Transactions

```text
Enter your choice: 3

Available Genres:

['Biography', 'Fiction', 'Technology',
 'Science', 'History', 'Mystery']

Enter Book Genre: science

Filtered Transactions:

Transaction ID       Book Title             Book Genre
T0009                Human Biology          Science
T0012                The Universe Explained Science
T0014                Physics Made Easy      Science
T0024                The Universe Explained Science

Total Records Found: 14
```

### 4️⃣ Generate Report

```text
Enter your choice: 4

Report generated successfully!

File Name: library_report.csv

             Total_Transactions  Average_Duration

Biography              9             14.111111
Fiction               17             12.529412
History               12             13.083333
Mystery               10             18.100000
Science               14             11.571429
Technology            18             13.833333
```

### 5️⃣ Data Analysis

```text
========== DATA ANALYSIS ==========

Dataset Information:
80 Entries
10 Columns

Genre Wise Transactions:

Biography      9
Fiction       17
History       12
Mystery       10
Science       14
Technology    18

User Type Analysis:

Faculty       30
Public        26
Student       24

Most Borrowed Books:

The Silent River           11
Artificial Intelligence     8
Python Programming          8
The Universe Explained      7
Modern India                 6

Monthly Borrowing:

2026-01      7
2026-02      9
2026-03      4
2026-04      8
2026-05     11
2026-06      8
2026-07     10
2026-08      9
2026-09      4
2026-10     10
```

### 6️⃣ Data Visualization

```text
Enter your choice: 6

Generating Charts...

All Charts Generated Successfully!
```

### 7️⃣ Show Dataset

```text
Enter your choice: 7

========== LIBRARY DATASET ==========

Transaction ID    Date         User ID
T0001             2026-01-13   U008
T0002             2026-10-07   U002
T0003             2026-04-30   U018
T0004             2026-10-07   U019
T0005             2026-08-05   U007

...

Total Records: 80
```

### 8️⃣ Exit

```text
Enter your choice: 8

Thank you for using E-Library Management System!
```

---

## 📈 Data Visualization

The project generates four different charts to understand library borrowing activities.

### 📊 1. Top 5 Most Borrowed Books

Displays the five most frequently borrowed books using a bar chart.

### 📅 2. Monthly Borrowing Trend

Displays monthly borrowing activities using a line chart.

### 🥧 3. Book Genre Distribution

Shows the distribution of different book genres using a pie chart.

### 🔥 4. Borrowing Activity Heatmap

Displays borrowing activity based on days and hours using a heatmap.

### Generated Chart Files

| Chart Name | Description |
|---|---|
| `Top_5_Books.png` | Top five borrowed books |
| `Monthly_Borrowing.png` | Monthly borrowing trend |
| `Genre_Distribution.png` | Genre-wise distribution |
| `Borrowing_Heatmap.png` | Day and hour borrowing activity |

**Output Folder:** `Library_Charts/`

All charts are saved in PNG format at **300 DPI** and are also displayed when generated.

---

## 📑 Generated Reports

When the user selects the **Generate Report** option, the application creates:

`library_report.csv`

The report contains:

- `Total_Transactions` – Total borrowing transactions for each genre.
- `Average_Duration` – Average borrowing duration for each genre.

The generated report is saved in the same folder as the Python file.

---

## ⚠️ Error Handling

The application handles common errors such as:

- Empty CSV file path.
- CSV file not found.
- Invalid file extension.
- Missing required columns.
- Empty dataset after data cleaning.
- Selecting analysis options before loading the dataset.
- Invalid menu choices.

---

## 🎓 Learning Outcomes

Through this project, the following concepts are implemented:

- Python Object-Oriented Programming (OOP).
- Pandas DataFrame operations.
- NumPy numerical calculations.
- Data Cleaning and Preprocessing.
- Descriptive Statistics.
- Data Filtering and Grouping.
- CSV File Handling.
- Data Visualization using Matplotlib and Seaborn.

---

## 🏁 Conclusion

The **E-Library Management System** is a useful Python-based data analysis project that simplifies the process of analyzing library borrowing transactions.

It combines dataset management, data cleaning, statistical calculations, transaction filtering, report generation, and data visualization into one interactive application.

This project demonstrates the practical application of Python libraries for real-world data analysis and visualization.

---


                                            ⭐ Thank You ⭐
