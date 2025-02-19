import os
import time

# Print ASCII art
print("""
███╗   ██╗███████╗██████╗ ██╗   ██╗██╗      █████╗     ████████╗███████╗ ██████╗██╗  ██╗
████╗  ██║██╔════╝██╔══██╗██║   ██║██║     ██╔══██╗    ╚══██╔══╝██╔════╝██╔════╝██║  ██║
██╔██╗ ██║█████╗  ██████╔╝██║   ██║██║     ███████║       ██║   █████╗  ██║     ███████║
██║╚██╗██║██╔══╝  ██╔══██╗██║   ██║██║     ██╔══██║       ██║   ██╔══╝  ██║     ██╔══██║
██║ ╚████║███████╗██████╔╝╚██████╔╝███████╗██║  ██║       ██║   ███████╗╚██████╗██║  ██║
╚═╝  ╚═══╝╚══════╝╚═════╝  ╚═════╝ ╚══════╝╚═╝  ╚═╝       ╚═╝   ╚══════╝ ╚═════╝╚═╝  ╚═╝
""")

# Get the directory of the script
script_path = os.path.abspath(__file__)
script_dir = os.path.dirname(script_path)

# Check if it's inside a folder
if os.path.basename(script_dir) == "":
    print("Please put this file inside a folder.")
    input("Press Enter to exit...")
    exit()

# Create a text file inside the folder
file_path = os.path.join(script_dir, "output.txt")
with open(file_path, "w") as file:
    file.write("This is a generated text file.")

print(f"Text file created successfully: {file_path}")

while True:
    user_input = input("Enter 'y' to continue, 'n' to exit: ").lower()
    
    if user_input == 'y':
        print("Continuing program...")
    elif user_input == 'n':
        print("Exiting program...")
        break
    else:
        print("Invalid input. Please enter 'y' or 'n'.")

    time.sleep(1)
