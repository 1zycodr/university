class Caesar:
    _alphabet = 'abcdefghijklmnopqrstuvwxyz'
    _n = 26

    @classmethod
    def decode(cls, value: str, key: int) -> str:
        result = ''

        for i, s in enumerate(value): 
            if s.isalpha():
                decoded_i = cls._alphabet.index(s.lower()) - key
                decoded_i %= cls._n

                if s.isupper():
                    result += cls._alphabet[decoded_i].upper()
                else:
                    result += cls._alphabet[decoded_i]

            else:
                result += s
        
        return result

    @classmethod
    def encode(cls, value: str, key: int) -> str:
        result = ''
        
        for i, s in enumerate(value):
            if s.isalpha():
                encoded_i = cls._alphabet.index(s.lower()) + key
                encoded_i %= cls._n
                
                if s.isupper():
                    result += cls._alphabet[encoded_i].upper()
                else:
                    result += cls._alphabet[encoded_i]

            else:
                result += s

        return result


if __name__ == '__main__':
    tests = [
        'TESTING CAESAR CIPHER',
        'SomEthing InTErestINg HaPPENs HERE',
        'WoW Is THERE CaeSAr CIPheR?!',
    ]
    
    for test in tests:
        for i in range(1, 26):
            encoded = Caesar.encode(test, i)
            decoded = Caesar.decode(encoded, i)
            print(test, encoded, decoded, sep=' -> ')
            assert decoded == test, i

