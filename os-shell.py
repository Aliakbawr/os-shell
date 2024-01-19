# OS project
# Students: MehrAzin Marzouq, AliAkbar Ahrari
# (!) Only run this program on a Unix-based OS

import os
import subprocess
import readline

# File to store command history
HISTORY_FILE = 'history.txt'


def execute_command(command):
    command = command.split()

    # Check for 'clear_history' command
    if command[0] == 'clear_history':
        readline.clear_history()  # Clear the command history
        if os.path.exists(HISTORY_FILE):
            os.remove(HISTORY_FILE)  # Delete the history file
        print("Command history cleared.")
        return

    if command[0] == 'help':
        print_help()
        return

    try:
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = process.communicate()

        if process.returncode != 0:
            print(f"Error: {error.decode().strip()}")
        else:
            print(output.decode().strip())

    except FileNotFoundError:
        print(f"Command not found: {command[0]}")


def print_help():
    commands = {
        'ls': 'List directory contents',
        'pwd': 'Print the name of the current working directory',
        'cd': 'Change the shell working directory',
        'touch': 'Change file timestamps',
        'mkdir': 'Make directories',
        'cat': 'Concatenate and print files',
        'grep': 'Print lines matching a pattern',
        'uname': 'Print system information',
        'df': 'Report file system disk space usage',
        'free': 'Display amount of free and used memory in the system',
        'top': 'Display Linux processes',
        'ping': 'Send ICMP ECHO_REQUEST to network hosts',
        'netstat': 'Print network connections, routing tables, interface statistics',
        'ifconfig': 'Configure a network interface',
        'ps': 'Report a snapshot of the current processes',
        'kill': 'Send a signal to a process',
        'bg': 'Put jobs in the background',
        'fg': 'Put jobs in the foreground',
        'clear_history': 'Clear the command history',
    }

    for command, description in commands.items():
        print(f"{command}: {description}")


def shell_loop():
    # Load history from file
    if os.path.exists(HISTORY_FILE):
        readline.read_history_file(HISTORY_FILE)

    while True:
        command = input("$ ")

        if command.lower() == "exit":
            break
        else:
            readline.add_history(command)  # Add command to history
            execute_command(command)

    # Save history to file
    readline.write_history_file(HISTORY_FILE)


if __name__ == "__main__":
    shell_loop()
