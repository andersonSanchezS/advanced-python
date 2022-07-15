# Error Handling

while True:
    try:
        age = int(input("How old are you? "))
        print(age)
    except ValueError:
        print("Invalid input")
    except Exception as e:
        print(e)
    else:
        print("thank you")
        break
