
def main():

    try:
        raise KeyError("Fake key error")
    except (KeyError, ZeroDivisionError) as e:
        print(e)
    else:
        print("No error")
    finally:
        print("Success")

main()