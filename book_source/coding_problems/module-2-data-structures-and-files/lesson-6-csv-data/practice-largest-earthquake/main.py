import cse163_utils


# Write your function here!


def main():
    data = cse163_utils.parse('/course/lecture-readings/earthquakes.csv')
    print(largest_magnitude(data))
    

if __name__ == '__main__':
    main()
