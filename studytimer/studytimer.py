import time

minutes = int(input("Enter study time (minutes): "))

seconds = minutes * 60
total_seconds = seconds

# Warning points (75%, 50%, 25% time remaining)
warnings = {
    total_seconds * 3 // 4: "⚠️ 75% of your time is still left!",
    total_seconds // 2: "⚠️ Half of your study time is left!",
    total_seconds // 4: "⚠️ Only 25% of your study time is left!"
}

while seconds > 0:
    mins = seconds // 60
    secs = seconds % 60

    print(f"\rTime left: {mins:02}:{secs:02}", end="")

    if seconds in warnings:
        print(f"\n{warnings[seconds]}")

    time.sleep(1)
    seconds -= 1

print("\n🎉 Time's up! Study session completed.")