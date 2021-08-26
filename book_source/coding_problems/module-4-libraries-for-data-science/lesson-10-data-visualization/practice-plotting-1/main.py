import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

sns.set()


def main():
    # Read iris.csv file using pandas library
    df = pd.read_csv('iris.csv')

    # TODO: Plot petal_width vs petal_length

    # TODO: Change the axis labels and title of the graph

    # Save the plot to a file
    # For this problem, we need an extra parameter for a better layout.
    plt.savefig('plot.png', bbox_inches='tight')


if __name__ == '__main__':
    main()
