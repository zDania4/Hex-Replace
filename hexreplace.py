import os
import sys
import ctypes

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except Exception:
        return False

if not is_admin():
    print("Requesting administrative privileges...")
    ctypes.windll.shell32.ShellExecuteW(
        None, "runas", sys.executable, " ".join(sys.argv), None, 1
    )
    sys.exit()

# Function to convert hex strings to bytes
def hex_to_bytes(hex_str):
    try:
        return bytes.fromhex(hex_str)
    except ValueError:
        print("Invalid hex string. Please ensure it only contains valid hexadecimal characters.")
        exit(1)

# Main function
def main():
    # Ask for the input EXE file
    exe_file = input("Enter the path to the EXE file: ").strip().strip('\"')

    # Check if the file exists
    if not os.path.isfile(exe_file):
        print(f"File '{exe_file}' not found.")
        return

    # Create a backup of the file
    backup_file = exe_file + ".bak"
    try:
        with open(exe_file, "rb") as f:
            data = f.read()
        with open(backup_file, "wb") as f:
            f.write(data)
        print(f"Backup created: {backup_file}")
    except Exception as e:
        print(f"Error creating backup: {e}")
        return

    # Ask for the number of changes to be made
    try:
        changes_count = int(input("How many changes do you want to make? "))
        if changes_count <= 0:
            print("The number of changes must be greater than 0.")
            return
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return

    # Perform each change
    for i in range(changes_count):
        print(f"Change {i + 1}:")
        current_hex = input("Enter the current hex value to search for: ").strip()
        new_hex = input("Enter the new hex value to replace with: ").strip()

        current_bytes = hex_to_bytes(current_hex)
        new_bytes = hex_to_bytes(new_hex)

        # Ensure the replacement bytes match the size of the original
        if len(current_bytes) != len(new_bytes):
            print("Error: Current and new hex values must have the same length.")
            return

        # Replace in the data
        if current_bytes in data:
            data = data.replace(current_bytes, new_bytes)
            print(f"Replaced: {current_hex} -> {new_hex}")
        else:
            print(f"Hex value {current_hex} not found in the file.")

    # Save the updated file
    try:
        with open(exe_file, "wb") as f:
            f.write(data)
        print(f"Changes saved to: {exe_file}")
    except Exception as e:
        print(f"Error saving changes: {e}")

if __name__ == "__main__":
    main()