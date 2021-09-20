from ciphers import Caesar, Vigenere
from tools import typewriter


def test_caesar(tests):
    typewriter('- Testing Caesar cipher...')
    typewriter('Enter maximum key (< 26): ', end='')
    keys_max = int(input())

    for test in tests:
        for i in range(1, keys_max + 1):
            encoded = Caesar.encode(test, i) 
            decoded = Caesar.decode(encoded, i)
            typewriter(' -> '.join([test + f' (key:{i})', encoded, decoded]))
            assert decoded == test, f'test: "{test}", key: {i}'
    
    typewriter('- Success!')
    
    
def test_vigenere(tests):
    typewriter('\n- Testing Vigenere cipher...')
    typewriter('Enter key (only letters): ', end='')
    key = input()

    for test in tests:
        encoded = Vigenere.encode(test, key)
        decoded = Vigenere.decode(encoded, key)
        typewriter(' -> '.join([test, encoded, decoded]))
        assert decoded == test, f'test: "{test}"'
    
    typewriter('- Success!')


def main():
    tests = [
        'TESTING CAESAR CIPHER ZZZ',
        'SomEthing InTErestINg HaPPENs HERE',
        'WoW Is THERE CaeSAr CIPheR?!',
    ]
    
    test_caesar(tests)
    test_vigenere(tests)


if __name__ == '__main__':
    main()

