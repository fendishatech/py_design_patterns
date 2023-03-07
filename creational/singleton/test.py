from my_singleton import MySingleton, MySingletonTwo


def test_with_new():
    instanceOne = MySingleton()
    print(f"Initial Value : {instanceOne.name}")

    instanceOne.name = "Changed at Instance One"
    print(f"Changed Value : {instanceOne.name}")

    instanceTwo = MySingleton()
    print(f"Value at second instance: {instanceOne.name}")


def test_with_new_two():
    instanceOne = MySingletonTwo()
    print(f"Initial Value : {instanceOne.name}")

    instanceOne.name = "Changed at Instance One"
    print(f"Changed Value : {instanceOne.name}")

    instanceTwo = MySingleton()
    print(f"Value at second instance: {instanceOne.name}")


def main():
    # test_with_new()
    test_with_new_two()


if __name__ == "__main__":
    main()
