import os

print("===== File Counter =====")

folder_path = input("Enter folder path: ").strip()

print("Hello! You selected this folder:", folder_path)

try:
    files = os.listdir(folder_path)
except FileNotFoundError:
    print("Folder not found!")
    exit()

file_count = 0
folder_count = 0

file_number = 1

extensions = {}

for item in files:
    full_path = os.path.join(folder_path, item)

    if os.path.isfile(full_path):
        print(f"{file_number}. {item}")
        file_count += 1
        file_number += 1
        extension = os.path.splitext(item)[1]

        if extension in extensions:
                extensions[extension] += 1
        else:
                extensions[extension] = 1

    elif os.path.isdir(full_path):
        folder_count += 1

print("Total files:", file_count)
print("Total folders:", folder_count)
print("\nFile Types:")

for ext, count in extensions.items():
    print(f"{ext} : {count}")

with open("report.txt", "w") as report:
    report.write("===== File Counter Report =====\n")
    report.write(f"Total Files: {file_count}\n")
    report.write(f"Total Folders: {folder_count}\n\n")

    report.write("File Types:\n")

    for ext, count in extensions.items():
        report.write(f"{ext} : {count}\n")
print("\nReport saved as report.txt")