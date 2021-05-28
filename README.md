# Upass
An encrypted and secure command line password manager tool.

## Upcomming Features -
- In Memory Decryption
- Graphical User Interface
- Support for Windows
- Suggestion of Randomly Ganerated Passwords
- Copy the passwords to the clipboard.
- Reminder to replace weak passwords using suggested one.

### About -
It is a secure password manager tool built using python3 that uses SQLite3
databases to store your passwords locally. The local database is encrypted 
using AES256-CBC encryption algorithm available in pyAesCrypt library.

## Dependencies
    - To add these dependencies, Run the commands given below -
        Type command: $pip install pyaescrypt

## Install Instructions 
    - Install the above dependencies using pip
    - Clone this repository,
        Type command : $git clone https://github.com/utgupta27/Upass.git
    - Now goto the source code directory i.e, >>Upass, 
        Type command: $cd Upass
    - To run the program, 
        Type command: $python3 main.py