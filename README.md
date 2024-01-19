# OS-shell
 simple shell for Unix os. this shell should handle operations like for executing operations, managing the operations' history, directing inputs and outputs , and managing the connection between child and parent processes.

# Python Shell Program User Guide

This Python shell program is a simple command-line interface that allows you to execute system commands and manage command history.

## Features

1. **Executing Operations**: The shell can execute any command that you would normally run in a terminal.

2. **Managing History**: The shell keeps a history of the commands you've entered. You can navigate through this history using the up and down arrow keys.

3. **Directing Input/Output**: The shell supports input and output redirection. You can use the `>` symbol to redirect a command's output to a file and the `<` symbol to take a command's input from a file.

4. **Communicating Using Pipe**: The shell supports communication between functions using pipes. You can use the `|` symbol to use the output of one command as the input to another command.

5. **Functions History**: The shell manages a history file to store user-entered inputs. You can clear the command history by entering the `clear_history` command.

6. **File Management**: The shell supports file management. You can use the `>` symbol to direct a command's output to a file and the `<` symbol to direct a command's input from a file.

## Usage

1. Run the Python shell program by executing `python shell.py` in your terminal.

2. Enter a command at the prompt (`$ `). For example, you can enter `ls` to list the files and directories in the current directory.

3. Press the up and down arrow keys to navigate through the history of commands.

4. Enter `clear_history` to clear the command history.

5. Enter `exit` to exit the shell.

## Testing

You can test the Python shell program by entering various commands and checking the output. For example, you can enter `ls`, `pwd`, `echo hello > file.txt`, `cat < file.txt`, `ls | grep .py`, and `clear_history`.

Remember, this is a very basic shell and doesn't handle many features of a full-fledged shell. Also, the availability of these commands may depend on your operating system.

