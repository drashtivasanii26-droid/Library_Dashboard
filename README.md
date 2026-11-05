# E-Library Management System

* **Author:** Drashti Vasani

## Project Overview

The **E-Library Management System** is a menu-driven Python application
for analyzing library borrowing transactions. It uses Pandas and NumPy
to load, clean, filter, and analyze library data, and Matplotlib and
Seaborn to create visual reports.

The program is implemented using a `LibraryDashboard` class.

## Features

1.  **Load Dataset** -- Load a CSV file, validate the required columns,
    remove duplicate rows, and remove records with missing or invalid
    required data.
2.  **Calculate Statistics** -- Display the total number of transactions
    and the average, maximum, minimum, and standard deviation of
    borrowing duration.
3.  **Filter Transactions** -- Search transactions by book genre
    (case-insensitive partial match).
4.  **Generate Report** -- Create a genre-wise report containing
    transaction counts and average borrowing duration.
5.  **Data Analysis** -- Display dataset information, descriptive
    statistics, genre-wise transactions, user-type analysis, the five
    most borrowed books, and monthly borrowing totals.
6.  **Data Visualization** -- Generate four charts: top five books,
    monthly borrowing trend, book genre distribution, and borrowing
    activity by day and hour.
7.  **Show Dataset** -- Display all loaded records and the total record
    count.
8.  **Exit** -- Close the application.

## Technologies Used

-   Python
-   Pandas
-   NumPy
-   Matplotlib
-   Seaborn

## Required Libraries

Install the required Python packages:

``` bash
pip install pandas numpy matplotlib seaborn
```

## CSV Dataset Format

The program expects a CSV file containing these exact column names:

  Column                        Description
  ----------------------------- -------------------------------------
  `Transaction ID`              Unique transaction identifier
  `Date`                        Date of the borrowing transaction
  `User ID`                     Library user identifier
  `Book Title`                  Title of the borrowed book
  `Book Genre`                  Genre/category of the book
  `User Type`                   Type/category of the user
  `Borrowing Time`              Time at which the book was borrowed
  `Borrowing Duration (Days)`   Borrowing duration in days

The CSV must contain all eight columns. The program converts `Date` to a
date value and `Borrowing Duration (Days)` to a numeric value. Rows with
missing required values or invalid dates/durations are removed.
Duplicate rows are also removed during loading.

## How to Run

1.  Save the Python program as `library_dashboard.py` (or another `.py`
    filename).
2.  Keep the library transaction CSV file in a known folder.
3.  Open a terminal or command prompt in the project folder.
4.  Run the program:

``` bash
python library_dashboard.py
```

5.  Choose an option from the menu.
6.  When prompted, enter the path to the CSV file.

## Main Menu

``` text
========== E-LIBRARY MENU ==========
1. Load Dataset
2. Calculate Statistics
3. Filter Transactions
4. Generate Report
5. Data Analysis
6. Data Visualization
7. Show Dataset
8. Exit

Enter your choice:
```

## Sample Output

The following is an example of the program's interaction. The displayed
record counts and calculated values depend on the CSV dataset used.

``` text
========== E-LIBRARY MENU ==========
1. Load Dataset
2. Calculate Statistics
3. Filter Transactions
4. Generate Report
5. Data Analysis
6. Data Visualization
7. Show Dataset
8. Exit

Enter your choice: 1

Enter CSV file path: library_data.csv

Dataset loaded successfully!
Total Records Loaded: [number of valid records]

========== E-LIBRARY MENU ==========
1. Load Dataset
2. Calculate Statistics
3. Filter Transactions
4. Generate Report
5. Data Analysis
6. Data Visualization
7. Show Dataset
8. Exit

Enter your choice: 2

========== STATISTICS ==========
Total Transactions: [total transactions]
Average Borrowing Duration: [average duration]
Maximum Borrowing Duration: [maximum duration]
Minimum Borrowing Duration: [minimum duration]
Standard Deviation: [standard deviation]

Enter your choice: 3

Available Genres:
[available book genres]

Enter Book Genre: Fiction

Filtered Transactions:
[matching transaction records]

Total Records Found: [number of matching records]

Enter your choice: 4

Report generated successfully!
File Name: library_report.csv
[genre-wise transaction count and average duration report]

Enter your choice: 5

========== DATA ANALYSIS ==========

Dataset Information:
[columns, non-null counts, and data types]

Dataset Description:
[descriptive statistics]

Genre Wise Transactions:
[transaction count for each genre]

User Type Analysis:
[transaction count for each user type]

Most Borrowed Books:
[top five book titles and their borrowing counts]

Monthly Borrowing:
[monthly transaction totals]

Enter your choice: 6

Generating Charts...
[Top 5 Most Borrowed Books chart displayed]
[Monthly Borrowing Trend chart displayed]
[Book Genre Distribution chart displayed]
[Borrowing Activity Day/Time Heatmap displayed]
All Charts Generated Successfully!

Enter your choice: 7

========== LIBRARY DATASET ==========
[all loaded transaction records]
Total Records: [number of records]

Enter your choice: 8

Thank you for using E-Library Management System!
```

## Generated Reports and Charts

### CSV Report

When **Generate Report** is selected, the program creates:

``` text
library_report.csv
```

The report groups transactions by `Book Genre` and contains:

-   `Total_Transactions` -- number of transactions in each genre.
-   `Average_Duration` -- average borrowing duration for each genre.

The report is saved in the same folder as the Python file.

### Visualizations

When **Data Visualization** is selected, the program creates the
`Library_Charts` folder (if it does not already exist) and saves these
charts:

  -----------------------------------------------------------------------
  Chart file                          Visualization
  ----------------------------------- -----------------------------------
  `Top_5_Books.png`                   Bar chart of the five most borrowed
                                      books

  `Monthly_Borrowing.png`             Line graph showing monthly
                                      borrowing totals

  `Genre_Distribution.png`            Pie chart showing the distribution
                                      of book genres

  `Borrowing_Heatmap.png`             Heatmap showing borrowing activity
                                      by day and hour
  -----------------------------------------------------------------------

All chart images are saved at 300 DPI in the `Library_Charts` folder,
located alongside the Python file. The charts are also displayed when
generated.

## Project Structure

``` text
E-Library-Management-System/
│
├── library_dashboard.py
├── library_data.csv
├── library_report.csv
├── Library_Charts/
│   ├── Top_5_Books.png
│   ├── Monthly_Borrowing.png
│   ├── Genre_Distribution.png
│   └── Borrowing_Heatmap.png
└── README.md
```

*The Python file and input CSV names above are examples. The report and
chart files are generated by the program.*

## Error Handling

The application checks for common input and dataset problems:

-   Empty CSV file path.
-   CSV file not found.
-   A file that does not have the `.csv` extension.
-   Missing required columns.
-   No valid records remaining after cleaning.
-   Attempts to use analysis options before loading a dataset.
-   Invalid menu choices.

## Conclusion

The E-Library Management System provides a simple way to examine library
borrowing activity. It combines data loading and cleaning, transaction
filtering, statistical calculations, genre-wise reporting, dataset
analysis, and visualizations in one interactive Python application.
