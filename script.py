def recover(cipher_hex, raw_key, sbox):
    # 1. Transform the key using the S-Box
    transformed_key = "".join(sbox.get(c, c) for c in raw_key)
    
    # 2. XOR Decrypt
    cipher_bytes = bytes.fromhex(cipher_hex)
    return "".join(chr(b ^ ord(transformed_key[i % len(transformed_key)])) 
                   for i, b in enumerate(cipher_bytes))


#note that if the results look gibberish, check the symmetry of your primes.
