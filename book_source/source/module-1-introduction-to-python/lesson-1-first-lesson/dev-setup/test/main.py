import sys

import geopandas
import numpy
import pandas
import requests
import seaborn
import sklearn
import skimage

from my_file import foo

EXPECTED_MAJOR = 3
EXPECTED_MINOR = 8


def main():
    print('Main runs');
    foo();

    version = sys.version_info
    if version.major != EXPECTED_MAJOR or version.minor != EXPECTED_MINOR:
        print('⚠️  Warning! Detected Python version '
              f'{version.major}.{version.minor} but expected version '
              f'{EXPECTED_MAJOR}.{EXPECTED_MINOR}')


if __name__ == '__main__':
    main()
