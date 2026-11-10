# Daily Routine

routine = {
    "Waking up": 30,
    "Morning exercise": 45,
    "Getting ready": 30,
    "Breakfast": 30,
    "Studying": 120,
    "Playing": 60,
    "Lunch": 30,
    "Watching TV": 60,
    "Homework": 120,
    "Dinner": 30,
    "Sleeping": 480
}

print("MY DAILY ROUTINE")
print("-------------------------")

for activity, minutes in routine.items():
    print(activity, "-", minutes, "minutes")

print("\nWEEKLY TIME SPENT")
print("-------------------------")

for activity, minutes in routine.items():
    weekly_time = minutes * 7

    hours = weekly_time // 60
    remaining_minutes = weekly_time % 60

    print(activity, "=", hours, "hours",
          remaining_minutes, "minutes per week")