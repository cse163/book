HEADER = '-' * 20

def error_message(expected, received, msg=''):
    expected = f"'{expected}'" if type(expected) is str else expected
    received = f"'{received}'" if type(received) is str else received
    if msg:
        msg += '\n\n'
        
    return f'\n\n{HEADER}\n{msg}Expected:\n{expected}\n\nReceived:\n{received}\n{HEADER}\n'
