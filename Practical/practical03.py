file = open("sample.txt", "w")

file.write("Welcome to TechFix Solutions!\n")
file.write("This file was created using Python.\n")
file.write("We are learning file handling.\n")

file.close()

print("✅ File 'sample.txt' has been created and text has been written successfully.")

file = open("message.txt", "w")

file.write("Hello! Welcome to Python file handling.\n")
file.write("This text is written into the file named 'message.txt'.")

file.close()

print("✅ File 'message.txt' has been created and text has been written successfully.")