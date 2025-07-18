#!/usr/bin/env python3
# encoding=utf-8
# file_name=zll.py

import os
from pathlib import Path
from typing import List, Tuple

from appdirs import user_data_dir
from zbig import zprint
from zbig.zfile import zcsv

APP_NAME = "zll"
APP_AUTHOR = "bigzhu"
CONFIG_FILE_NAME = "hosts.csv"
config_file_path = Path(user_data_dir(APP_NAME, APP_AUTHOR)) / CONFIG_FILE_NAME
print(config_file_path)


# 确保文件建立
def create_config_file() -> None:
    """Create the SSH configuration file if it doesn't exist."""
    if config_file_path.exists():
        return
    config_file_path.parent.mkdir(parents=True, exist_ok=True)
    config_file_path.write_text("User,Host,Port,Description\n")
    print(f"Create file: {config_file_path}")


def read_connections() -> Tuple[List[str], List[List[str]]]:
    """Read SSH connections from configuration file.

    Returns:
        Tuple containing header row and connection data rows
    """
    header, rows = zcsv.read_csv(str(config_file_path))
    print(f"Using SSH connection info file: {config_file_path}")
    return header, rows


# 添加 number 和打印
def display_connections_table(
    header: List[str], connection_data: List[List[str]]
) -> None:
    """Display SSH connections in a formatted table with row numbers.

    Args:
        header: Column headers for the table
        connection_data: List of connection rows
    """
    numbered_header = ["Number"] + header
    numbered_rows = [[i] + row for i, row in enumerate(connection_data)]
    zprint.table([numbered_header] + numbered_rows, "    ")


def connect_to_host(connection_info: List[str]) -> None:
    """Connect to SSH server with given connection info.

    Args:
        connection_info: List containing [user, hostname, port, description]
    """
    try:
        user, hostname, port, *_ = connection_info + [
            "22"
        ]  # Default port to 22 if not provided
        if not user or not hostname:
            raise ValueError("Username and hostname are required")

        print(f"SSH connecting to {hostname} ......")
        result = os.system(f"export TERM=xterm;ssh -p {port} {user}@{hostname}")
        if result != 0:
            print(f"SSH connection failed with exit code {result}")
    except (ValueError, IndexError) as e:
        print(f"Error in SSH connection: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")


def add_connection() -> None:
    """Add a new SSH connection configuration."""
    try:
        username = input("Input username: ").strip()
        hostname = input("Input ip or hostname: ").strip()
        if not username or not hostname:
            raise ValueError("Username and hostname are required")

        port_input = input("Input port (default 22): ").strip() or "22"
        try:
            port_number = int(port_input)
            if not (1 <= port_number <= 65535):
                raise ValueError("Port must be between 1 and 65535")
            port = str(port_number)
        except ValueError:
            print("Invalid port number, using default port 22")
            port = "22"

        description = input("Input comment: ").strip()
        zcsv.write_csv_append(
            str(config_file_path), [username, hostname, port, description]
        )
        print("Added successfully!")
    except KeyboardInterrupt:
        print("\nOperation cancelled.")
        return
    except Exception as e:
        print(f"Error adding new host: {e}")
        return

    main()


def delete_connection(index_string: str) -> None:
    """Delete an SSH connection configuration by index.

    Args:
        index_string: String representation of the connection index to delete
    """
    try:
        delete_index = int(index_string)
        if delete_index < 0:
            raise ValueError("Index cannot be negative")
        zcsv.write_csv_delete(str(config_file_path), delete_index)
        print("Delete successfully!")
    except ValueError as e:
        print(f"Invalid number for deletion: {e}")
    except Exception as e:
        print(f"Error deleting host: {e}")

    main()


def interactive_menu(header: List[str], connection_data: List[List[str]]) -> None:
    """Display interactive menu for SSH connection management.

    Args:
        header: Column headers for the connection table
        connection_data: List of SSH connection data rows
    """
    while True:
        display_connections_table(header, connection_data)
        user_input = (
            input("Input number, IP, or hostname (q to quit, a to add, d to delete): ")
            .strip()
            .lower()
        )

        if user_input == "q":
            return
        if user_input == "a":
            return add_connection()
        if user_input == "d":
            delete_index_input = input("Input number to delete: ")
            return delete_connection(delete_index_input)
        if not user_input:
            continue

        try:
            selected_index = int(user_input)
            if 0 <= selected_index < len(connection_data):
                return connect_to_host(connection_data[selected_index])
        except ValueError:
            # If user_input is not an integer, continue with string comparison
            pass

        matching_connections = [
            row
            for row in connection_data
            if user_input in str(row[1]) or user_input in str(row[3])
        ]

        if not matching_connections:
            print("Can't find any matching connections.")
        elif len(matching_connections) == 1:
            return connect_to_host(matching_connections[0])
        else:
            print(
                f"Found {len(matching_connections)} matches for '{user_input}', please select again!"
            )
            connection_data = matching_connections


def main() -> None:
    """Main entry point for the SSH connection manager."""
    create_config_file()
    header, connection_data = read_connections()
    interactive_menu(header, connection_data)


if __name__ == "__main__":
    main()
