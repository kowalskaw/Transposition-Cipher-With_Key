import numpy as np
from encrypt_transpos_cipher import EncryptTranspositionCipher
import math


class DecryptTranspositionCipher(EncryptTranspositionCipher):
    pass

    def __init__(self, word, input):
        self.word = word
        # klucz -> lista liczb
        self.key = super().generate_key(word)
        # input -> wejściowy tekst zaszyfrowany
        self.input = input
        # matrix ->
        self.matrix = np.full((len(self.key), len(self.key)), " ")
        # przestawiony tekst jawny
        self.decrypted = ""

    def check_blocks_and_decrypt(self):
        max_len = \
            float(len(self.key) * len(self.key)) / 2.0 \
            + float(len(self.key)) / 2.0
        max_len = int(max_len)
        print("Maksymalna długosć bloku: " + str(max_len))

        self.input = self.input.replace(" ", "")

        current_char_num = 0

        # jesli tekst zaszyfrowany nie miesci sie w jednej macierzy
        if len(self.input) > max_len:
            num_blocks = math.ceil(float(len(self.input)) / float(max_len))
            print("numblocks:", num_blocks)
            for i in range(num_blocks):
                temp_input = ""
                # pętla która wypełni temp_input odpowiednim fragmentem
                # zaszyfrowanego tekstu
                for j in range(max_len):
                    # print(self.input[current_char_num])

                    if current_char_num >= len(self.input):
                        temp_input += "x"
                        current_char_num += 1
                    else:
                        temp_input += self.input[current_char_num]
                        current_char_num += 1
                self.decrypt_input_in_matrix(temp_input)
                print(self.matrix)
                self.decrypted += self.read_decrypted_string_from_matrix()
                temp_input = ""
        else:
            self.decrypt_input_in_matrix(self.input)
            self.decrypted += self.read_decrypted_string_from_matrix()

    def decrypt_input_in_matrix(self, input):
        # deszyfrowanie
        order = 0
        cursor = 0
        on_the_right = []  # liczby z klucza na prawo,
        # czyli te, które trzeba wpisać
        for y in range(0, len(self.key)):
            for x in range(0, len(self.key)):
                if self.key[x] == order:
                    for n in range(x, len(self.key)):
                        on_the_right.append(self.key[n])
                        print(on_the_right)
                    on_the_right.sort()
                    for n in range(0, len(on_the_right)):
                        self.matrix[on_the_right[n]][x] = input[cursor]
                        cursor += 1
                    on_the_right.clear()
                    order += 1

        print(self.matrix)

    def read_decrypted_string_from_matrix(self):
        decrypted_string = ""
        order = 0

        for row in self.matrix:
            for cell in row:
                decrypted_string += cell
                # if self.key[x] == order:
                #     for cell in range(len(self.key)):
                #         decrypted_string += self.matrix[cell][x]
                #     order += 1

        return decrypted_string.replace(" ", "")

    def print_attributes(self):
        print(self.word)
        print(self.key)
        print(self.input)
        print(self.matrix)
        print(self.decrypted)

    def get_word(self):
        return self.word

    def get_key(self):
        return self.key

    def get_input(self):
        return self.input

    def get_matrix(self):
        return self.matrix

    def get_decrypted(self):
        return self.decrypted


word = "kurwa"
input = "rwajoazrictjnoernociaeloiinnwcedgoatsiwomsawcjztrairjnooneaiceilaorndwincooosmitweszwaacgorrojinjneaaeitwlrinodcnsoacoiwieaswzoargtcomajjannerertiiwooncandslceioowigsotaxxixxmxxxaxrwajoazrictjnoernociaeloiinnwcedgoatsiwomsawcjztrairjnooneaiceilaorndwincooosmitweszwaacgorrojinjneaaeitwlrinodcnsoacoiwieaswzoargtcomajjannerertiiwooncandslceioowigsotaxxixxmxxxax"
decrypt = DecryptTranspositionCipher(word, input)
decrypt.check_blocks_and_decrypt()
decrypt.print_attributes()
