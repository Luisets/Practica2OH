import group06.EA as ea


def f(array):
    return sum(array)
    pass


def main():
    bounds = [(1, 5)] * 5
    name = ea.EA(f, bounds, 10)
    name.run(10)
    pass


if __name__ == "__main__":
    pass
