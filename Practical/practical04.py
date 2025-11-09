file = open("message.txt", "r")

content = file.read()

print("=== File Contents ===")
print(content)

file.close()