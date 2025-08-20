# file_read_write_with_error_handling.py

def read_and_modify_file():
    input_file = input("Enter the filename to read: ")

    try:
        # Try reading the file
        with open(input_file, "r") as f:
            content = f.read()

        # Modify content (example: uppercase)
        modified_content = content.upper()

        # Ask for output filename
        output_file = input("Enter the new filename to save modified content: ")

        with open(output_file, "w") as f:
            f.write(modified_content)

        print(f"\n✅ Modified content written successfully to '{output_file}'")

    except FileNotFoundError:
        print(f"❌ Error: The file '{input_file}' does not exist.")
    except PermissionError:
        print(f"❌ Error: You don’t have permission to read '{input_file}'.")
    except Exception as e:
        print(f"⚠️ An unexpected error occurred: {e}")


# Run the program
read_and_modify_file()
