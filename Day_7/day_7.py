# file = open("loream.txt", "r")
# content = file.read()
# file.close()

# with open("loream.txt", "r") as file_read:
#   print(file_read.readable())
  # entire = file_read.read()
  # first_line = file_read.readline()
  # entire but list = file_read.readlines()
  
# with open("output.txt", "w") as file_write:
  # print(file_write.writable())
  # file_write.write("PUMUB\n")
  # file_write.writelines(["PUMUB\n", "FC\n", "IT"])

# with open("output.txt", "a") as file_append:
#   file_append.write("\nCS")
#   file_append.writelines(["\nFirst Year", "\nSection a"])

# import os

# path_url = os.path.join("Day_7", "output.txt")

# if os.path.exists(path_url):
#   print("File Exists")
#   os.remove(path_url)
# else:
#   print("File Not Found")


# from pathlib import Path

# path_url = Path("Day_7") / "loream.txt"

# if path_url.exists:
#   print("Exists")

# path_url.write_text("Hello")

# print(path_url.read_text())

import csv

# with open("data.csv", "r") as csv_file:
#   # reader = csv.reader(csv_file)
#   reader = csv.DictReader(csv_file)
#   for row in reader:
#     print(row["Name"])


# data_list = [
#     ["Name", "Age", "City"],
#     ["Alice", 30, "New York"],
#     ["Bob", 25, "Los Angeles"]
# ]

# with open("output_list.csv", "w", newline="") as wirte_csv_list:
#   writer = csv.writer(wirte_csv_list)
#   writer.writerows(data_list)

# data_csv = [
#     {"Name": "Alice", "Age": 30, "City": "New York"},
#     {"Name": "Bob", "Age": 25, "City": "Los Angeles"}
# ]

# with open("output_dict.csv", "w", newline="") as wirte_csv_dict:
#   fieldnames = ["Name", "Age", "City"]
  
#   writer = csv.DictWriter(wirte_csv_dict, fieldnames=fieldnames)
#   writer.writeheader()
#   writer.writerows(data_csv)

import json

# with open("test.json", "r") as json_read:
#   data = json.load(json_read)
#   print(data["name"])

# data = {
#     "name": "Alice",
#     "age": 30,
#     "city": "New York"
# }

# with open("output.json", "w") as f:
#     json.dump(data, f, indent=4) 

json_string = '{"name": "Alice", "age": 30}'
print(json_string, type(json_string))

data = json.loads(json_string)
print(data, type(data))

output = json.dumps(data)
print(output, type(output))