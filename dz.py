path = r"C:\Users\Admin\Desktop\dz.txt"

with open(path, "w", encoding="utf-8") as file1:
    file1.write("name: Vlad\n")
    file1.write("surname: Babinsky\n")
    file1.write("age: 15\n")
    file1.write("Study in: It-Step\n")

with open(path, "r", encoding="utf-8") as file1:
    content = file1.read()
    print(content)