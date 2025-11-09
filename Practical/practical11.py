try:
    file = open("example.txt", "r")
    content = file.read()
    print("File content:\n", content)
except FileNotFoundError:
    print("Error: File 'example.txt' does not exist.")
finally:
    print("Closing file (if opened).")
    try:
        file.close()
    except NameError:
        pass