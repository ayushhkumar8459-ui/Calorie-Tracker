# Name: [Ayush]
# Date: [7-10-2025]
# Project: Calorie Tracker

print("Welcome to the Calorie Tracker!")
print("You can log your meals and track your total calories for the day.\n")

# Step 1: Ask how many meals
meal_count = int(input("How many meals did you have today? "))

# Step 2: Create empty lists to store data
meals = []
calories = []

# Step 3: Get meal names and calories
for i in range(meal_count):
    meal_name = input(f"Enter meal {i+1} name: ")
    calorie_amount = float(input(f"Enter calories for {meal_name}: "))
    meals.append(meal_name)
    calories.append(calorie_amount)

# Step 4: Calculate total and average calories
total_calories = sum(calories)
average_calories = total_calories / meal_count

# Step 5: Ask for daily calorie limit
daily_limit = float(input("\nEnter your daily calorie limit: "))

# Step 6: Compare and print message
if total_calories > daily_limit:
    print("\n⚠️ You have exceeded your daily calorie limit!")
else:
    print("\n✅ You are within your daily calorie limit. Great job!")

# Step 7: Display summary neatly
print("\nHere is your calorie summary:\n")
print("Meal Name\tCalories")
print("--------------------------------")

for i in range(meal_count):
    print(f"{meals[i]}\t\t{calories[i]}")

print("--------------------------------")
print(f"Total:\t\t{total_calories}")
print(f"Average:\t{average_calories:.2f}")

# Step 8 (Bonus): Save to file
save = input("\nDo you want to save this report to a file? (yes/no): ").lower()

if save == "yes":
    from datetime import datetime
    filename = f"calorie_log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    with open(filename, "w") as f:
        f.write("Daily Calorie Tracker Report\n")
        f.write("--------------------------------\n")
        for i in range(meal_count):
            f.write(f"{meals[i]}\t{calories[i]}\n")
        f.write("--------------------------------\n")
        f.write(f"Total: {total_calories}\n")
        f.write(f"Average: {average_calories:.2f}\n")
        if total_calories > daily_limit:
            f.write("Status: Exceeded daily limit\n")
        else:
            f.write("Status: Within daily limit\n")
    print(f"\nReport saved as {filename}")
else:
    print("\nReport not saved. Goodbye!")
