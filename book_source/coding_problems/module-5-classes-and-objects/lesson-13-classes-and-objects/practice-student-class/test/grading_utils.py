HEADER = '-' * 20

def error_message(expected, received):
    expected = f"'{expected}'" if type(expected) is str else expected
    received = f"'{received}'" if type(received) is str else received
    return f'\n\n{HEADER}\nExpected:\n{expected}\n\nReceived:\n{received}\n{HEADER}\n'


def assert_equals(unittest, expected, received):
    unittest.assertEquals(expected, received, error_message(expected, received))
