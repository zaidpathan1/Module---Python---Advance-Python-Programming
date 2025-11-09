file = open("info.txt", "r")

data = file.read(10)

print(f"Data read: {data}")

position = file.tell()
print(f"Current cursor position: {position}")

# Close the file
file.close()