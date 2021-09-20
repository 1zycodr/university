from time import sleep
import sys


def typewriter(string, end='\n'):
    """
        smoothly printing string 
        :param line: line which we have to print 
        :return:     None
    """
    string += end
    for letter in string:
        print(letter, end='')
        sys.stdout.flush()
        sleep(0.004)

