def encode(text, key):
    # print("1. call cipher()")
    cipher = make_cipher(key)
    # print(f"    1.4 cipher is {''.join(cipher)}")

    ciphertext_chars = []
    print(f"2. encrypt message")
    for char in text:
        print(
            # f"    i is {char}, cipher.index(i) is {cipher.index(char)} and chr(65 + {cipher.index(char)}) is {chr(65 + cipher.index(char))}"
        )
        ciphered_char = chr(65 + cipher.index(char))
        ciphertext_chars.append(ciphered_char)

    # print(f"3. encrypted message is {''.join(ciphertext_chars)}")
    return "".join(ciphertext_chars)


def decode(encrypted, key):
    cipher = make_cipher(key)
    answer = "theswiftfoxjumpedoverthelazydog"
    index = 0
    print(f"1. generate cipher: {''.join(cipher)}")
    plaintext_chars = []

    print("2. decrypt each letter:")
    for char in encrypted:
        print(
            f"    * '{char}' should decrypt to '{answer[index]}' with index {cipher.index(answer[index])}"
        )
        print(
            f"    * actual value is '{cipher[65 - ord(char)]}' with an index of {65 - ord(char)} \n"
        )
        # corrected: could use abs(), * 1 or switch ord(char) with 65
        plain_char = cipher[ord(char) - 65]
        plaintext_chars.append(plain_char)
        index += 1

    return "".join(plaintext_chars)


def make_cipher(key):
    # chr() takes integer argument and return the string representing a character at that code point.
    # alphabet = [f"{i}: {chr(i + 98)}" for i in range(1, 26)]

    # corrected:
    alphabet = [chr(i + 97) for i in range(0, 26)]
    # print(f"    1.2 create alphabet: {alphabet}")
    cipher_with_duplicates = list(key) + alphabet
    # print(f"    1.3 combine {list(key)} with alphabet: {cipher_with_duplicates}")

    cipher = []
    for i in range(0, len(cipher_with_duplicates)):
        if cipher_with_duplicates[i] not in cipher_with_duplicates[:i]:
            cipher.append(cipher_with_duplicates[i])
    return cipher


# When you run this file, these next lines will show you the expected
# and actual outputs of the functions above.
# print(
#     f"""
# Running: encode("theswiftfoxjumpedoverthelazydog", "secretkey")
# Expected: EMBAXNKEKSYOVQTBJSWBDEMBPHZGJSL
# Actual: {encode('theswiftfoxjumpedoverthelazydog', 'secretkey')}
# """
# )

print(
    f"""
Running: decode("EMBAXNKEKSYOVQTBJSWBDEMBPHZGJSL", "secretkey")
Expected: theswiftfoxjumpedoverthelazydog
Actual: {decode('EMBAXNKEKSYOVQTBJSWBDEMBPHZGJSL', 'secretkey')}
"""
)
