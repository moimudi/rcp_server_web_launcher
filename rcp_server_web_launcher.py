#!/usr/bin/env python3
# launch_browser/rcp_server_web_launcher.py
# RPC Server Web Browser Launcher, start from windows or linux

# --- Notes ---
# Copy this file and run it in a separate terminal before launching the Navidec platform code.
# Ensure that Python 3 is installed on your operating system.
# If you're using Windows, you can simply download the compiled file "rpcserver.exe" and run it without the need to install Python.
# Ensure that you have Google Chrome installed on Windows or Firefox installed on Linux.

# command to run...
# python3  rcp_server_web_launcher.py

import os
import tempfile
import platform
import subprocess
from xmlrpc.server import SimpleXMLRPCServer

# Assign IP address and port number to variables
ip_address = "0.0.0.0"
port = 8100

# Function to change the color of text
def change_color(text, color):
    # Define color codes
    colors = {
        'red': '\033[31m',
        'green': '\033[32m',
        'yellow': '\033[33m',
        'blue': '\033[34m',
        'magenta': '\033[35m',
        'cyan': '\033[36m',
        'white': '\033[37m',
        'reset': '\033[0m'
    }

    # Check if the operating system is Windows
    if os.name == 'nt':
        os.system('')

    # Print the colored text
    return f'{colors[color]}{text}{colors["reset"]}'

def display_message(message, color):
    print(change_color(message, color))

def print_title(title, color):
    bar = '+' + '-' * (len(title) + 2) + '+'
    print(change_color(bar, color))
    print('| ' + change_color(title, color) + ' |')
    print(change_color(bar, color))

def launch_browser(urls):

    os_name = platform.system()
    print(change_color(f"Currrent OS is {os_name}", 'cyan'))

    try:
        if os_name == "Windows":
            # Create a new temporary directory for the user data
            user_data_dir = tempfile.mkdtemp()

            # Define the command
            command = ["cmd", "/c", "start", "chrome", "--user-data-dir=" + user_data_dir] + urls
            subprocess.Popen(command, shell=True)

        elif os_name == "Linux":
            # For Linux, use the 'firefox' command
            command = ["firefox"] + urls
            subprocess.Popen(command, shell=True)
        else:
            print(change_color(f"Unsupported operating system: {os_name}", 'red'))
            return False
    except Exception as e:
        print(change_color(f"An error occurred: {e}", 'red'))
        return False

    return True

def is_alive():
    return "RPC Server is alive"

def start_server(ip_address, port):
    # Use the variables in the SimpleXMLRPCServer function
    server = SimpleXMLRPCServer((ip_address, port))

    print_title('RPC Server Web Browser Launcher', 'yellow')

    # Display the message in red
    display_message("Ensure Chrome on Windows or Firefox on Linux, and this RPC Server not blocked by firewall.", 'red')

    print(change_color(f"Listening on port {port}...", 'green'))

    server.register_function(launch_browser, "launch_browser")

    server.register_function(is_alive, "is_alive")

    server.serve_forever()

# Call the function with your IP address and port
start_server(ip_address, port)



