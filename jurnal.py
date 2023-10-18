# -*- coding: utf-8 -*-
"""jurnal.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/17SvwKPQPk1Wk5zxyPndsVqWYCDP2Cs_o
"""

import streamlit as st
st.title("KRIPTOGRAFI")
def vigenere_encrypt(plain_text, key):
    encrypted_text = ""
    key_length = len(key)
    for i in range(len(plain_text)):
        char = chr((ord(plain_text[i]) + 1) % 256)
        key_char = key[i % key_length]
        encrypted_char = chr((ord(char) + ord(key_char)) % 256)
        encrypted_text += encrypted_char
    return encrypted_text

def vigenere_decrypt(cipher_text, key):
    decrypted_text = ""
    key_length = len(key)
    for i in range(len(cipher_text)):
        char = cipher_text[i]
        key_char = key[i % key_length]
        decrypted_char = chr((ord(char) - ord(key_char) - 1) % 256)
        decrypted_text += decrypted_char
    return decrypted_text

def calculate_ber(original_text, decrypted_text):
    if len(original_text) != len(decrypted_text):
        raise ValueError("Panjang teks asli dan teks terdekripsi harus sama")

    num_errors = sum(1 for a, b in zip(original_text, decrypted_text) if a != b)
    ber = num_errors / len(original_text)
    return ber

def calculate_cer(original_text, decrypted_text):
    if len(original_text) != len(decrypted_text):
        raise ValueError("Panjang teks asli dan teks terdekripsi harus sama")

    num_errors = sum(1 for a, b in zip(original_text, decrypted_text) if a != b)
    cer = num_errors / len(original_text)
    return cer

def calculate_avalanche_effect(original_text, key):
    encrypted_text = vigenere_encrypt(original_text, key)
    total_changes = 0

    for i in range(len(original_text)):
        modified_text = list(original_text)
        modified_text[i] = chr((ord(modified_text[i]) + 1) % 256)
        modified_text = ''.join(modified_text)
        modified_encrypted_text = vigenere_encrypt(modified_text, key)

        differences = sum(1 for j in range(len(encrypted_text)) if encrypted_text[j] != modified_encrypted_text[j])
        total_changes += differences

    avalanche_effect = (total_changes / (len(original_text) * 256)) * 100  # Hitung dalam persentase
    return avalanche_effect



# Contoh penggunaan
original_text = st.text_input("Enter the message: ")  # Teks asli
key = st.text_input("Enter the Key: ")  # Kunci Vigenere
cipher_text = vigenere_encrypt(original_text, key)  # Enkripsi teks asli
decrypted_text = vigenere_decrypt(cipher_text, key)  # Dekripsi teks terenkripsi


ber_str = str(int(ber * 10000))
cer_str = str(int(cer * 10000))
avalanche_effect_str = str(int(round(avalanche_effect)))

st.write(f'Teks Asli: {original_text}')
st.write(f'Teks Terenkripsi: {cipher_text}')
st.write(f'Teks Terdekripsi: {decrypted_text}')
st.write(f'Bit Error Rate (BER): {ber_str}')
st.write(f'Character Error Rate (CER): {cer_str}')
st.write(f'Avalanche Effect: {avalanche_effect_str}')
       

