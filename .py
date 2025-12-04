import os
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
from datetime import datetime

# ============================================
# Task 1: Data Ingestion & Validation
# ============================================

def load_all_data(data_dir):
    files = list(Path(data_dir).glob("*.csv"))
    combined = []

    for file in files:
        try:
            df = pd.read_csv(file, parse_dates=["timestamp"], on_bad_lines="skip")
        except Exception as e:
            print(f"Error in {file}: {e}")
            continue

        # Add missing metadata
        name = file.stem.split("_")[0]
        df["building"] = df.get("building", name)
        df["month"] = df.get("month", file.stem.split("_")[1] if "_" in file.stem else "Unknown")

        combined.append(df)

    if combined:
        return pd.concat(combined, ignore_index=True)
    return pd.DataFrame()

# ============================================
# Task 2: Aggregations
# ============================================

def calculate_daily_totals(df):
    df = df.set_index("timestamp")
    return df.resample("D")["kwh"].sum()

def calculate_weekly_aggregates(df):
    df = df.set_index("timestamp")
    return df.resample("W")["kwh"].sum()

def building_wise_summary(df):
    summary = df.groupby("building")["kwh"].agg(["mean", "min", "max", "sum"])
    summary.rename(columns={"sum": "total"}, inplace=True)
    return summary

# ============================================
# Task 3: Object-Oriented Modeling
# ============================================

class MeterReading:
    def __init__(self, timestamp, kwh):
        self.timestamp = timestamp
        self.kwh = kwh

class Building:
    def __init__(self, name):
        self.name = name
        self.meter_readings = []

    def add_reading(self, reading):
        self.meter_readings.append(reading)

    def calculate_total_consumption(self):
        return sum(r.kwh for r in self.meter_readings)

    def generate_report(self):
        values = [r.kwh for r in self.meter_readings]
        return {
            "building": self.name,
            "total": sum(values),
            "min": min(values),
            "max": max(values),
            "mean": sum(values) / len(values),
        }

# ============================================
# Task 4: Dashboard Visualization
# ============================================

def generate_dashboard(df, output="dashboard.png"):
    daily = calculate_daily_totals(df)
    weekly = calculate_weekly_aggregates(df)

    plt.figure(figsize=(12, 15))

    # 1. Daily Trend Line
    plt.subplot(3, 1, 1)
    for b in df["building"].unique():
        subset = df[df["building"] == b].set_index("timestamp").resample("D")["kwh"].sum()
        plt.plot(subset.index, subset.values, label=b)
    plt.title("Daily Energy Consumption Trend")
    plt.xlabel("Date")
    plt.ylabel("kWh")
    plt.legend()
    plt.grid()

    # 2. Weekly Bar Chart
    plt.subplot(3, 1, 2)
    weekly_df = df.groupby("building").resample("W", on="timestamp")["kwh"].sum().groupby("building").mean()
    plt.bar(weekly_df.index, weekly_df.values)
    plt.title("Average Weekly Usage per Building")
    plt.ylabel("kWh")
    plt.grid(axis='y')

    # 3. Scatter Plot for Peak Hours
    plt.subplot(3, 1, 3)
    df["hour"] = df["timestamp"].dt.hour
    for b in df["building"].unique():
        subset = df[df["building"] == b]
        plt.scatter(subset["hour"], subset["kwh"], label=b, s=10)
    plt.title("Peak-Hour Consumption Scatter Plot")
    plt.xlabel("Hour of Day")
    plt.ylabel("kWh")
    plt.legend()
    plt.grid()

    plt.tight_layout()
    plt.savefig(output)
    plt.close()

# ============================================
# Task 5: File Exports
# ============================================

def export_files(df):
    df.to_csv("cleaned_energy_data.csv", index=False)

    summary = building_wise_summary(df)
    summary.to_csv("building_summary.csv")

    total = df["kwh"].sum()
    highest = summary["total"].idxmax()
    peak_hour = df.groupby(df["timestamp"].dt.hour)["kwh"].sum().idxmax()

    with open("summary.txt", "w") as f:
        f.write("Campus Energy-Use Dashboard — Executive Summary\n\n")
        f.write(f"Total campus consumption: {total} kWh\n")
        f.write(f"Highest consuming building: {highest}\n")
        f.write(f"Peak load time: {peak_hour}:00 hrs\n")

# ============================================
# Main Runner
# ============================================

def main():
    df = load_all_data("data")
    if df.empty:
        print("No valid CSV files found")
        return

    generate_dashboard(df)
    export_files(df)
    print("All tasks completed successfully!")

if __name__ == "__main__":
    main()
