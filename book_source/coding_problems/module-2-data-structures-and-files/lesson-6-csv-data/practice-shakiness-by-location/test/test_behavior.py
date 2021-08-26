import unittest

import cse163_utils
import main


class Test(unittest.TestCase):
    def setUp(self):
        self._data = cse163_utils.parse("earthquakes.csv")

    def _test_helper(self, data, ans):
        val = main.shakiness_by_location(data)
        self.assertEquals(ans, val, f"Expected {ans}, but received {val}")

    def test_small_example(self):
        """
        #name(Test small example shown in spec)
        """
        data = [
            {
                "id": 1,
                "year": 2015,
                "month": 3,
                "day": 6,
                "latitude": 108.2,
                "longitude": 43.1,
                "name": "Seattle",
                "magnitude": 4,
            },
            {
                "id": 14,
                "year": 2015,
                "month": 4,
                "day": 6,
                "latitude": 45.7,
                "longitude": 107.4,
                "name": "Genovia",
                "magnitude": 6,
            },
            {
                "id": 6,
                "year": 2016,
                "month": 10,
                "day": 31,
                "latitude": 56.3,
                "longitude": 91.4,
                "name": "Seattle",
                "magnitude": 3.5,
            },
        ]
        expected = {"Seattle": 7.5, "Genovia": 6}
        self._test_helper(data, expected)

    def test_full_example(self):
        """
        #name(Test full earthquakes.csv dataset)
        """
        expected = {
            "California": 3638.4900000000084,
            "Burma": 22.200000000000003,
            "Nevada": 496.6400000000006,
            "Alaska": 3407.0000000000005,
            "Hawaii": 375.2099999999998,
            "Montana": 91.19000000000001,
            "Puerto Rico": 385.99999999999983,
            "Chile": 157.79999999999998,
            "Dominican Republic": 97.70000000000002,
            "British Virgin Islands": 230.09999999999994,
            "Indonesia": 298.60000000000014,
            "Washington": 176.2199999999999,
            "Southern East Pacific Rise": 15.799999999999999,
            "Argentina": 49.3,
            "Philippines": 85.19999999999999,
            "Canada": 99.96,
            "Papua New Guinea": 130.3,
            "Afghanistan": 43.6,
            "Oregon": 107.23000000000002,
            "South of Africa": 4.5,
            "Peru": 63.800000000000004,
            "Fiji": 75.0,
            "Japan": 192.60000000000002,
            "Oklahoma": 192.79999999999993,
            "Mexico": 111.45,
            "Kyrgyzstan": 39.8,
            "Tennessee": 36.24,
            "Tonga": 66.5,
            "Arkansas": 6.66,
            "South of the Fiji Islands": 77.00000000000001,
            "Utah": 71.59,
            "Georgia": 4.2,
            "U.S. Virgin Islands": 84.49999999999999,
            "Idaho": 27.930000000000003,
            "Wyoming": 46.29999999999999,
            "Iran": 13.299999999999999,
            "Syria": 4.4,
            "Russia": 122.60000000000001,
            "Tajikistan": 53.80000000000001,
            "Southwest Indian Ridge": 41.6,
            "Anguilla": 2.4,
            "Panama": 13.399999999999999,
            "Kansas": 47.489999999999995,
            "Northern Mariana Islands": 239.00000000000003,
            "Christmas Island": 5.0,
            "China": 63.900000000000006,
            "New Zealand": 88.40000000000002,
            "Vanuatu": 43.1,
            "Guatemala": 26.300000000000004,
            "Greece": 9.4,
            "Poland": 4.2,
            "Chagos Archipelago region": 4.4,
            "Italy": 64.3,
            "Virgin Islands region": 1.8,
            "New Jersey": 2.33,
            "Northern California": 2.45,
            "Southern Mid-Atlantic Ridge": 13.6,
            "South Sandwich Islands": 19.9,
            "South Georgia and the South Sandwich Islands": 99.7,
            "Northwest of Australia": 4.1,
            "South Indian Ocean": 26.900000000000002,
            "Solomon Islands": 45.5,
            "Mid-Indian Ridge": 4.9,
            "Portugal": 12.999999999999998,
            "Ascension Island region": 4.7,
            "Azerbaijan": 5.0,
            "India": 9.3,
            "Kiribati region": 4.6,
            "Martinique": 4.6,
            "Venezuela": 9.0,
            "Bolivia": 12.9,
            "Turkey": 8.0,
            "Vanuatu region": 4.5,
            "Missouri": 20.469999999999995,
            "Guam": 9.0,
            "Ohio": 1.98,
            "Nicaragua": 18.5,
            "East Timor": 4.5,
            "Northern Mid-Atlantic Ridge": 9.899999999999999,
            "Palau": 5.3,
            "Colorado": 19.4,
            "West Virginia": 2.31,
            "New Caledonia": 157.6,
            "Australia": 14.5,
            "Off the coast of Oregon": 7.199999999999999,
            "Virginia": 1.94,
            "Costa Rica": 17.7,
            "Ukraine": 4.8,
            "Colombia": 8.899999999999999,
            "East of the Kuril Islands": 4.7,
            "Cyprus": 4.1,
            "Pacific-Antarctic Ridge": 9.399999999999999,
            "Uzbekistan": 4.6,
            "Illinois": 7.289999999999999,
            "Central Mid-Atlantic Ridge": 4.3,
            "Western Indian-Antarctic Ridge": 4.5,
            "Ecuador": 8.5,
            "South of Panama": 4.6,
            "El Salvador": 9.399999999999999,
            "Western Xizang": 9.4,
            "Azores-Cape St. Vincent Ridge": 4.7,
            "North Carolina": 1.92,
            "North of Svalbard": 5.0,
            "Texas": 2.5,
            "Fiji region": 14.600000000000001,
            "Reykjanes Ridge": 4.5,
            "Arizona": 4.39,
            "Pakistan": 4.4,
            "Greenland Sea": 4.5,
            "New Hampshire": 1.5,
            "South Georgia Island region": 86.39999999999999,
            "New York": 1.48,
            "Central East Pacific Rise": 4.6,
            "North of Ascension Island": 9.5,
            "Pennsylvania": 1.37,
            "Japan region": 11.5,
            "Taiwan": 4.2,
            "Kuril Islands": 4.6,
        }
        self._test_helper(self._data, expected)

    def test_single_row(self):
        """
        #name(Test with subset of earthquakes.csv dataset)
        """
        self._test_helper(self._data[:1], {"California": 1.43})

    def test_empty_data(self):
        """
        #name(Test with dataset with no rows)
        """
        self._test_helper(self._data[:0], {})
