import numpy as np


# Write your function here!


def main():
    values = np.arange(12).reshape((3, 4))
    print(values)
    result = collapse(values)
    print(result)


if __name__ == '__main__':
    main()
