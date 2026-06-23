import time

minutes = int(input("Enter study time (minutes): "))

seconds = minutes * 60

while seconds > 0:
    mins = seconds // 60
    secs = seconds % 60

    print(f"\rTime left: {mins:02}:{secs:02}", end="")

    time.sleep(1)
    seconds -= 1

print("\nTime's up! Study session completed.")