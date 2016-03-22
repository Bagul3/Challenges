import sys


EXIT    = 'exit'
USAGE   = '''This is a recursion exercise script.

You will continuously be prompted for input to be used in calculations,
until you choose to exit.

To exit type: {exit}
'''.format(exit=EXIT)

def prompt(msg, expect=str, exit='exit'):
    """prompt(str[, type[, str]]) -> type

        msg:        message to prompt user
        expect:     type to expect                          
        exit:       input that would cause program exit;    default: 'exit'

    Prompts user for input until input of desired type or exits.
    Returns value converted to the `expect` type on success, else prompts again.
    """
    uinput = raw_input(msg)

    if uinput == exit:  sys.exit()
    try:                return expect(uinput)
    except:             return prompt(msg, expect, exit)

def power(base, n):
    """power(int, int) -> int

    Raises base to the power of n, returns result.
    """
    if n == 0: return 1
    return base * power(base, n-1)


if __name__ == '__main__':
    print USAGE
    while True:
        base    = prompt('Give me a base integer: ',                 expect=int)
        n       = prompt('Give me a power integer to raise it to: ', expect=int)

        print power(base, n)
