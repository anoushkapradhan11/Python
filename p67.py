try:
    with (open("file1.txt")as f1,
        open("file.txt")as f2,
        open ("file3.txt")as f3):
        print(f1.read())
        print(f2.read())
        print(f3.read())
except Exception as e:
    print(e)
else:
    print("Code Sucessfully ran")
