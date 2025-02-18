print("""
███╗   ██╗███████╗██████╗ ██╗   ██╗██╗      █████╗     ████████╗███████╗ ██████╗██╗  ██╗
████╗  ██║██╔════╝██╔══██╗██║   ██║██║     ██╔══██╗    ╚══██╔══╝██╔════╝██╔════╝██║  ██║
██╔██╗ ██║█████╗  ██████╔╝██║   ██║██║     ███████║       ██║   █████╗  ██║     ███████║
██║╚██╗██║██╔══╝  ██╔══██╗██║   ██║██║     ██╔══██║       ██║   ██╔══╝  ██║     ██╔══██║
██║ ╚████║███████╗██████╔╝╚██████╔╝███████╗██║  ██║       ██║   ███████╗╚██████╗██║  ██║
╚═╝  ╚═══╝╚══════╝╚═════╝  ╚═════╝ ╚══════╝╚═╝  ╚═╝       ╚═╝   ╚══════╝ ╚═════╝╚═╝  ╚═╝
""")

while True:
    close_program = input("Do you want to close this program? y/n: ").lower()


    if close_program == 'y':
        print("Closing program...")
        break
    elif close_program == 'n':
        print("Program will keep running.")
    else:
        print("Invalid input. Please enter 'y' to close or 'n' to keep running the program.")

    import time
    time.sleep(1)
    
