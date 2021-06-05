with open("example.txt","a+") as files:
    print(f"initial location: {files.tell()}")
data=files.read()
if not data:
    print("read nothing")
else:
    print(files.read())