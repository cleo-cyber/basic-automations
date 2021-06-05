with open("example.txt","a+") as files:
    print(f"initial location: {files.tell()}")

    data=files.read()

    if not data:
        print("read nothing")
    else:
        print(files.read())
    files.seek(0,0)
    print("New location{}".format(files.tell()))
    data=files.read()
    if not data:
        print("read nothing")
    else:
        print(data)
    print("location after read{}".format(files.tell()))
