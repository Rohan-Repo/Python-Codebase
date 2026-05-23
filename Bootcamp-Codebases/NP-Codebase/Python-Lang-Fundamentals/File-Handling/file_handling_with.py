# Simple File Handling in Python

print("SIMPLE FILE HANDLING DEMO")

# 1. READ MODE - Read existing file
print("\n1. READ MODE")
with open('python-info.txt', 'r') as file:
    content = file.read()
    print( 'File Mode: ', file.mode )
    print(content)
# File automatically closed here

# 2. WRITE MODE - Create new file (overwrites if exists)
print("\n2. WRITE MODE")
with open('output.txt', 'w') as file:
    print( 'File Mode: ', file.mode )
    file.write("This is a new file\n")
    file.write("Written using write mode\n")
print("File 'output.txt' created!")

# Read what we wrote
with open('output.txt', 'r') as file:
    print(file.read())

# 3. APPEND MODE - Add to end of file
print("\n3. APPEND MODE")
with open('output.txt', 'a') as file:
    print( 'File Mode: ', file.mode )
    file.write("This line was appended\n")
    file.write("Append preserves existing content\n")
print("Content appended!")

# Read updated file
with open('output.txt', 'r') as file:
    print(file.read())

print("Demo completed!")
