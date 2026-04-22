# Simple File Handling in Python

print("SIMPLE FILE HANDLING DEMO")

# 1. READ MODE - Read existing file
print("\n1. READ MODE")
file = open('python-info.txt', 'r')
content = file.read()
print(content)
file.close()

# 2. WRITE MODE - Create new file (overwrites if exists)
print("\n2. WRITE MODE")
file = open('output.txt', 'w')
file.write("This is a new file\n")
file.write("Written using write mode\n")
file.close()
print("File 'output.txt' created!")

# Read what we wrote
file = open('output.txt', 'r')
print(file.read())
file.close()

# 3. APPEND MODE - Add to end of file
print("\n3. APPEND MODE")
file = open('output.txt', 'a')
file.write("This line was appended\n")
file.write("Append preserves existing content\n")
file.close()
print("Content appended!")

# Read updated file
file = open('output.txt', 'r')
print(file.read())
file.close()

print("Demo completed!")
