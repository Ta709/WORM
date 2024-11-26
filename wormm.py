import os
import shutil

# Define the base directory and the number of directories to replicate to
base_dir = './worm_test/'
num_replicates = 5

# File to log keystrokes
keylog_file = os.path.join(base_dir, "keylog.txt")

def on_key_event_simulated(key):
    """Simulate key logging by capturing user input."""
    with open(keylog_file, 'a') as log_file:
        log_file.write(f"{key}\n")

def start_keylogger_simulated():
    """Simulate keylogging by capturing user input from console."""
    print("Keylogger is running. Type 'exit' to stop.")
    while True:
        key = input("Press any key: ")  # Simulate key press by capturing input
        if key.lower() == "exit":
            break
        on_key_event_simulated(key)

def replicate():
    """Replicates the script into subdirectories."""
    # Ensure the base directory exists
    if not os.path.exists(base_dir):
        os.makedirs(base_dir)

    # Get the path of the current script
    script_name = os.path.basename(__file__)

    # Replicate the script to `num_replicates` directories
    for i in range(1, num_replicates + 1):
        # Define a new sub-directory name
        new_dir = os.path.join(base_dir, f'replica_{i}')

        # Check if the new directory exists; if not, create it
        if not os.path.exists(new_dir):
            os.makedirs(new_dir)

        # Define the path to replicate the script to
        new_copy_path = os.path.join(new_dir, script_name)

        # If the script hasn't already been copied to the new directory, copy it
        if not os.path.exists(new_copy_path):
            shutil.copy2(__file__, new_copy_path)
            print(f"Replicated script to {new_copy_path}")
        else:
            print(f"Script already exists in {new_copy_path}")

def main():
    print("This is a safe educational example of how a worm might replicate.")
    print("Press Ctrl+C to stop the script.")
    replicate()

    # Start the simulated keylogger
    start_keylogger_simulated()

if __name__ == '__main__':
    main()
