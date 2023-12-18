
import datetime
import subprocess

def schedule_shutdown():
    # Get current date and time
    current_time = datetime.datetime.now()

    # Define off-work hours
    start_time = current_time.replace(hour=21, minute=0, second=0)
    end_time = current_time.replace(hour=7, minute=0, second=0)

    # Check if current time is within off-work hours
    if current_time >= start_time or current_time <= end_time:
        # Schedule server shutdown
        subprocess.run(["sudo", "shutdown", "-h", "+1"])  # Shutdown in 1 minute

# Run the shutdown scheduling function
schedule_shutdown()