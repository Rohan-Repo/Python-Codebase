# Simple File Handling in Python with Error Handling

print("SIMPLE FILE HANDLING DEMO WITH ERROR HANDLING")

# 1. READ MODE - Read existing file
print("\n1. READ MODE")
try:
    with open('python_data_analysis_short.txt', 'r') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("Error: File not found! Please check the filename.")
except PermissionError:
    print("Error: Permission denied! You don't have access to read this file.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

# 2. WRITE MODE - Create new file (overwrites if exists)
print("\n2. WRITE MODE")
try:
    with open('output.txt', 'w') as file:
        file.write("This is a new file\n")
        file.write("Written using write mode\n")
    print("File 'output.txt' created!")
    
    # Read what we wrote
    with open('output.txt', 'r') as file:
        print(file.read())
except PermissionError:
    print("Error: Permission denied! Cannot write to this location.")
except IOError as e:
    print(f"Error: I/O error occurred - {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

# 3. APPEND MODE - Add to end of file
print("\n3. APPEND MODE")
try:
    with open('output.txt', 'a') as file:
        file.write("This line was appended\n")
        file.write("Append preserves existing content\n")
    print("Content appended!")
    
    # Read updated file
    with open('output.txt', 'r') as file:
        print(file.read())
except FileNotFoundError:
    print("Error: File not found! Cannot append to non-existent file.")
except PermissionError:
    print("Error: Permission denied! Cannot modify this file.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

# 4. Demonstrating error handling with non-existent file
print("\n4. ERROR HANDLING DEMO")
try:
    with open('nonexistent.txt', 'r') as file:
        content = file.read()
except FileNotFoundError:
    print("Caught FileNotFoundError: 'nonexistent.txt' does not exist!")

print("\nDemo completed!")
