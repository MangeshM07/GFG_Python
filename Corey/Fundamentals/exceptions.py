
try:
    f = open("test.txt")
    if f.name == "test.txt":
        raise Exception
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print(e)
else:
    print("File present")
    print(f.read())
finally:
    print("Executing finally block")