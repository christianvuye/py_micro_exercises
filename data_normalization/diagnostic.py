print(f"The value of __name__ is: {__name__}")

if __name__ == "__main__":
    print("This file was run directly!")
else:
    print("This file was imported by another program!")