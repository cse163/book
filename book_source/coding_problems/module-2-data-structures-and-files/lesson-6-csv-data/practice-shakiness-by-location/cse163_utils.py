import pandas as pd


def parse(file_name):
    """
    Reads the CSV with the given file_name and returns it as a list of
    dictionaries. The list will have a dictionary for each row, and each
    dictionary will have a key for each column.
    """
    df = pd.read_csv(file_name)
    return df.to_dict('records')
