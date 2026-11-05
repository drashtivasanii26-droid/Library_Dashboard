
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


class LibraryDashboard:

    def __init__(self):
        self.df = None

        # Save files in the same folder as this Python file
        self.base_path = os.path.dirname(os.path.abspath(__file__))
        self.chart_folder = os.path.join(
            self.base_path, "Library_Charts"
        )

    # 1. Load Dataset
    def load_data(self, file_path):

        file_path = file_path.strip().strip('"').strip("'")

        if not file_path:
            print("\nPlease enter CSV file path.")
            return

        if not os.path.isfile(file_path):
            print("\nError: CSV file not found!")
            print("Please check your file path.")
            self.df = None
            return

        if not file_path.lower().endswith(".csv"):
            print("\nError: Please select a CSV file.")
            self.df = None
            return

        try:
            df = pd.read_csv(file_path)

            required_columns = [
                "Transaction ID",
                "Date",
                "User ID",
                "Book Title",
                "Book Genre",
                "User Type",
                "Borrowing Time",
                "Borrowing Duration (Days)"
            ]

            missing_columns = [
                col for col in required_columns
                if col not in df.columns
            ]

            if missing_columns:
                print("\nMissing columns:", missing_columns)
                self.df = None
                return

            df = df.drop_duplicates()
            df = df.dropna(subset=required_columns)

            df["Date"] = pd.to_datetime(
                df["Date"], errors="coerce"
            )

            df["Borrowing Duration (Days)"] = pd.to_numeric(
                df["Borrowing Duration (Days)"],
                errors="coerce"
            )

            df = df.dropna(subset=[
                "Date",
                "Borrowing Duration (Days)"
            ])

            if df.empty:
                print("\nError: CSV file has no valid records.")
                self.df = None
                return

            self.df = df

            print("\nDataset loaded successfully!")
            print("Total Records Loaded:", len(self.df))

        except Exception as e:
            self.df = None
            print("\nError loading dataset:", e)

    # Check Dataset
    def check_data(self):

        if self.df is None or self.df.empty:
            print("\nPlease load your CSV dataset first.")
            return False

        return True

    # 2. Calculate Statistics
    def calculate_statistics(self):

        if not self.check_data():
            return

        duration = self.df["Borrowing Duration (Days)"]

        print("\n========== STATISTICS ==========")
        print("Total Transactions:", len(self.df))
        print("Average Borrowing Duration:", np.mean(duration))
        print("Maximum Borrowing Duration:", np.max(duration))
        print("Minimum Borrowing Duration:", np.min(duration))
        print("Standard Deviation:", np.std(duration))

    # 3. Filter Transactions
    def filter_transactions(self):

        if not self.check_data():
            return

        print("\nAvailable Genres:")
        print(self.df["Book Genre"].unique())

        genre = input("\nEnter Book Genre: ").strip()

        if not genre:
            print("\nPlease enter a genre.")
            return

        result = self.df[
            self.df["Book Genre"].astype(str).str.contains(
                genre, case=False, na=False
            )
        ]

        if result.empty:
            print("\nNo transactions found for:", genre)

        else:
            print("\nFiltered Transactions:")
            print(result.to_string(index=False))
            print("\nTotal Records Found:", len(result))

    # 4. Generate Report
    def generate_report(self):

        if not self.check_data():
            return

        report = self.df.groupby("Book Genre").agg(
            Total_Transactions=("Transaction ID", "count"),
            Average_Duration=("Borrowing Duration (Days)", "mean")
        )

        report_path = os.path.join(
            self.base_path, "library_report.csv"
        )

        report.to_csv(report_path)

        print("\nReport generated successfully!")
        print("File Name: library_report.csv")
        print(report)

    # 5. Data Analysis
    def data_analysis(self):

        if not self.check_data():
            return

        print("\n========== DATA ANALYSIS ==========")

        print("\nDataset Information:")
        self.df.info()

        print("\nDataset Description:")
        print(self.df.describe(include="all"))

        print("\nGenre Wise Transactions:")
        print(self.df.groupby("Book Genre").size())

        print("\nUser Type Analysis:")
        print(self.df.groupby("User Type").size())

        print("\nMost Borrowed Books:")
        print(self.df["Book Title"].value_counts().head(5))

        print("\nMonthly Borrowing:")
        monthly = self.df.groupby(
            self.df["Date"].dt.to_period("M")
        ).size()

        print(monthly)

    # 6. Data Visualization
    def data_visualization(self):

        if not self.check_data():
            return

        os.makedirs(self.chart_folder, exist_ok=True)

        print("\nGenerating Charts...")

        # 1. Top 5 Books Bar Chart
        top_books = self.df["Book Title"].value_counts().head(5)

        plt.figure(figsize=(9, 5))
        ax = top_books.plot(kind="bar")

        ax.set_title("Top 5 Most Borrowed Books")
        ax.set_xlabel("Book Title (X-Axis)")
        ax.set_ylabel("Number of Borrowings (Y-Axis)")
        ax.legend(["Borrowing Count"], loc="upper right")

        ax.text(
            0.98, 0.02,
            "X: Book Title\nY: Borrowing Count",
            transform=ax.transAxes,
            fontsize=8,
            ha="right",
            va="bottom",
            bbox=dict(boxstyle="round", facecolor="white", alpha=0.8)
        )

        plt.xticks(rotation=30, ha="right")
        plt.tight_layout()

        plt.savefig(
            os.path.join(self.chart_folder, "Top_5_Books.png"),
            dpi=300,
            bbox_inches="tight"
        )
        plt.show()
        plt.close()

        # 2. Monthly Borrowing Line Graph
        monthly = self.df.groupby(
            self.df["Date"].dt.to_period("M")
        ).size()

        plt.figure(figsize=(9, 5))
        ax = monthly.plot(kind="line", marker="o")

        ax.set_title("Monthly Borrowing Trend")
        ax.set_xlabel("Month (X-Axis)")
        ax.set_ylabel("Number of Borrowings (Y-Axis)")
        ax.legend(["Monthly Borrowing"], loc="upper right")

        ax.text(
            0.98, 0.02,
            "X: Month\nY: Total Borrowings",
            transform=ax.transAxes,
            fontsize=8,
            ha="right",
            va="bottom",
            bbox=dict(boxstyle="round", facecolor="white", alpha=0.8)
        )

        plt.xticks(rotation=45)
        plt.tight_layout()

        plt.savefig(
            os.path.join(self.chart_folder, "Monthly_Borrowing.png"),
            dpi=300,
            bbox_inches="tight"
        )
        plt.show()
        plt.close()

        # 3. Genre Pie Chart
        genre_count = self.df["Book Genre"].value_counts()

        plt.figure(figsize=(7, 7))
        ax = genre_count.plot(
            kind="pie",
            autopct="%1.1f%%",
            startangle=90
        )

        ax.set_title("Book Genre Distribution")
        ax.set_ylabel("")

        plt.tight_layout()

        plt.savefig(
            os.path.join(self.chart_folder, "Genre_Distribution.png"),
            dpi=300,
            bbox_inches="tight"
        )
        plt.show()
        plt.close()

        # 4. Borrowing Activity Heatmap
        heatmap_data = self.df.copy()

        heatmap_data["Day"] = heatmap_data["Date"].dt.day_name()

        heatmap_data["Hour"] = pd.to_datetime(
            "2000-01-01 " + heatmap_data["Borrowing Time"].astype(str),
            errors="coerce"
        ).dt.hour

        heatmap_data = heatmap_data.dropna(subset=["Hour"])

        day_order = [
            "Monday", "Tuesday", "Wednesday",
            "Thursday", "Friday", "Saturday", "Sunday"
        ]

        if not heatmap_data.empty:

            pivot_data = heatmap_data.pivot_table(
                index="Day",
                columns="Hour",
                values="Transaction ID",
                aggfunc="count",
                fill_value=0
            )

            pivot_data = pivot_data.reindex(
                [d for d in day_order if d in pivot_data.index]
            )

            plt.figure(figsize=(10, 5))

            ax = sns.heatmap(
                pivot_data,
                annot=True,
                cmap="YlGnBu",
                fmt="g"
            )

            ax.set_title("Borrowing Activity Day/Time Heatmap")
            ax.set_xlabel("Hour (X-Axis)")
            ax.set_ylabel("Day (Y-Axis)")

        else:
            plt.figure(figsize=(10, 5))
            plt.text(
                0.5, 0.5,
                "No Valid Borrowing Time Data",
                ha="center",
                va="center"
            )
            plt.title("Borrowing Activity Day/Time Heatmap")
            plt.xlabel("Hour (X-Axis)")
            plt.ylabel("Day (Y-Axis)")

        plt.tight_layout()

        plt.savefig(
            os.path.join(self.chart_folder, "Borrowing_Heatmap.png"),
            dpi=300,
            bbox_inches="tight"
        )
        plt.show()
        plt.close()

        # Final Success Message
        print("All Charts Generated Successfully!")

    # 7. Show Dataset
    def show_dataset(self):

        if not self.check_data():
            return

        print("\n========== LIBRARY DATASET ==========")
        print(self.df.to_string(index=False))
        print("\nTotal Records:", len(self.df))

    # 8. Main Menu
    def run(self):

        while True:

            print("\n========== E-LIBRARY MENU ==========")
            print("1. Load Dataset")
            print("2. Calculate Statistics")
            print("3. Filter Transactions")
            print("4. Generate Report")
            print("5. Data Analysis")
            print("6. Data Visualization")
            print("7. Show Dataset")
            print("8. Exit")

            choice = input("\nEnter your choice: ").strip()

            if choice == "1":

                path = input(
                    "\nEnter CSV file path: "
                ).strip().strip('"').strip("'")

                self.load_data(path)

            elif choice == "2":
                self.calculate_statistics()

            elif choice == "3":
                self.filter_transactions()

            elif choice == "4":
                self.generate_report()

            elif choice == "5":
                self.data_analysis()

            elif choice == "6":
                self.data_visualization()

            elif choice == "7":
                self.show_dataset()

            elif choice == "8":
                print("\nThank you for using E-Library Management System!")
                break

            else:
                print("\nInvalid choice! Please enter 1 to 8.")


# Main Program
if __name__ == "__main__":

    obj = LibraryDashboard()
    obj.run()
