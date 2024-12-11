# file = open("my_file.txt")
# content = file.read()
# print(content)
# file.close()

# with open("my_file.txt") as file:
#     contents = file.read()
#     print(contents)

# with open("my_file.txt", mode="w") as file: // Write Mode
#     file.write("New text.")

# with open("my_file.txt", mode="a") as file: // Append Mode
#     file.write("\n2nd line text.")

# with open("new_file.txt", mode="w") as file: #//  If in write mode, creates file if file does not exist
#     file.write("1st line")

# score = open("my_file.txt", "r").read()
# print(score)

with open("D:\_Projects\sample_data.txt", "r") as file: # Absolute file path
    print(file.read())

with open("./Day 24/my_file.txt", "r") as file: # Relative file path (This assumes that Python Self-Learning folder is working directory)
    print(file.read())

with open("../../another_sample.txt", "r") as file:
    print(file.read())