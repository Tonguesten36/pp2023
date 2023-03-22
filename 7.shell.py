import subprocess

subprocess.call(['echo', '---Welcome to The Shell---'])

while True:
    # User's input
    command = input(">>> ")

    # Terminate the shell
    if command == "exit":
        exit()

    # Run command with shell=True (although I'm not sure if this is safe)
    subprocess.run(command, shell=True)

