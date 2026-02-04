try:
    with open("test12.txt", "r") as f:
        f.write("asdasdasd")
except (FileNotFoundError, ValueError) as e:
        print("General exception occurred!")

'''
'r': Read (default). Error if file doesn't exist.
'w': Write. Creates new or overwrites existing.
'a': Append. Adds to the end of the file.
'b': Binary mode (for images/PDFs).
'''