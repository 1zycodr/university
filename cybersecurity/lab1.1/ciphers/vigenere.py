class Vigenere:
    _alphabet = 'abcdefghijklmnopqrstuvwxyz'
    _n = 26

    @classmethod
    def decode(cls, value: str, key: str) -> str:
        result = ''
        key_len = len(key)
        no_alpha_count = 0

        for i, s in enumerate(value): 
            if s.isalpha():
                decoded_i = cls._alphabet.index(s.lower())
                decoded_i -= cls._alphabet.index(
                    key[(i - no_alpha_count) % key_len]
                )
                decoded_i %= cls._n
                
                assert decoded_i < 26 and decoded_i >= 0, decoded_i
                
                if s.isupper():
                    result += cls._alphabet[decoded_i].upper()
                else:
                    result += cls._alphabet[decoded_i]

            else:
                no_alpha_count += 1
                result += s
        
        return result

    @classmethod
    def encode(cls, value: str, key: str) -> str:
        result = ''
        key_len = len(key)
        no_alpha_count = 0

        for i, s in enumerate(value):
            if s.isalpha():
                encoded_i = cls._alphabet.index(s.lower()) 
                encoded_i += cls._alphabet.index(
                    key[(i - no_alpha_count) % key_len]
                )
                encoded_i %= cls._n
                
                assert encoded_i < 26, encoded_i 
                
                if s.isupper():
                    result += cls._alphabet[encoded_i].upper()
                else:
                    result += cls._alphabet[encoded_i]

            else:
                no_alpha_count += 1
                result += s

        return result


if __name__ == '__main__':
    tests = [
        'TESTING CAESAR CIPHERZZ',
        'SomEthing InTErestINg HaPPENs HERE',
        'WoW Is THERE CaeSAr CIPheR?!',
    ]
    key = 'abcde'
    
    for test in tests:
        encoded = Vigenere.encode(test, key)
        decoded = Vigenere.decode(encoded, key)
        print(test, encoded, decoded, sep=' -> ')
        assert decoded == test, i

