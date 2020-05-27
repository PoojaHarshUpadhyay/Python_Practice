with open("bear.txt", "r") as  file1:
    brea_content = file1.read()
    
with open("first.txt", "w") as file2:
    file2.write(brea_content[:90])
