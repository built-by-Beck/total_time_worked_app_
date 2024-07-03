## The Creator = built_by_Beck
## wrote this code to help with paperwork at Topre America where I used to work
## takes user input for start time and end time then returns total minutes worked 
## Simple command-line program


from datetime import datetime

def my_function():
    start_time = input("Enter start time (in 24-hour format, e.g., 0900): ")
    end_time = input("Enter end time (in 24-hour format, e.g., 1430): ")

    # Convert input times to datetime objects
    start_time_dt = datetime.strptime(start_time, "%H%M")
    end_time_dt = datetime.strptime(end_time, "%H%M")

    # Calculate time difference
    time_difference = end_time_dt - start_time_dt

    # Calculate total minutes worked
    total_minutes = time_difference.total_seconds() / 60

    print(f"Total time worked was {int(total_minutes)} minutes.")

# Loop to run the function repeatedly
while True:
    my_function()
    continue_prompt = input("Do you want to calculate another time period? (yes/no): ")
    if continue_prompt.lower() != 'yes':
        break

print("Exiting program.")
