import numpy as np
import math


class EncryptTranspositionCipher():
    def __init__(self, word, input):
        self.word = word
        # klucz -> lista liczb
        self.key = self.generate_key(word)
        # input -> wejściowy tekst jawny
        self.input = input
        # matrix -> pusta macierz wypełniona spacjami
        self.matrix = np.full((len(self.key), len(self.key)), " ")
        # zaszyfrowany tekst -> pusty strig
        self.encrypted = ""

    def generate_key(self, word):
        i = 0
        order = 0
        alphabet = 'abcdefghijklmnopqrstuwxyz'
        key = [None] * len(word)

        while (i < len(alphabet)):
            # jesli litera wystapi chociaz raz to
            if word.count(alphabet[i]) != 0:
                # zwraca ile razy wystapila litera
                number_of_occurences = word.count(alphabet[i])
                start = 0  # indeks od ktorego ma szukac (find)
                # in range wykona sie tyle razy, ile wystapila litera
                for n in range(0, number_of_occurences):
                    # znajduje indeks pierwszego wystapienia litery,
                    # od indeksu start
                    indx = word.find(alphabet[i], start)
                    key[indx] = order  # w kluczu, pod indeksem pierwszego
                    # wystapienia litery, zapisujemy kolejnosc
                    order += 1  # zmieniamy kolejnosc
                    # (jesli pod a bylo 1, to pod kolejna litera bedzie 2)
                    start = indx + 1  # jesli bylo wiecej wystapien,
                    # to zmieniamy start, zeby szukalo kolejnego indeksu poza znalezionym
            i += 1

        return key

    # def load_word_from_file(self, directory):

    def check_blocks_and_encrypt(self):
        max_len = \
            float(len(self.key) * len(self.key)) / 2.0 \
            + float(len(self.key)) / 2.0
        max_len = int(max_len)
        print("Maksymalna długosć bloku: " + str(max_len))

        self.input = self.input.replace(" ", "")

        current_char_num = 0

        # jesli tekst jawny nie miesci sie w jednej macierzy
        if len(self.input) > max_len:
            num_blocks = math.ceil(float(len(self.input)) / float(max_len))
            print("numblocks:", num_blocks)
            for i in range(num_blocks):
                # tutaj jest przechowywany aktualnie przetwarzany
                # fragment tekstu wejściowego
                temp_input = ""
                # pętla która wypełni temp_input odpowiednim fragmentem
                # tekstu lub X-ami jeśli tekst jest za krótki
                for j in range(max_len):
                    if current_char_num >= len(self.input):
                        temp_input += "x"
                        current_char_num += 1
                    else:
                        # print(self.input[current_char_num])
                        temp_input += self.input[current_char_num]
                        current_char_num += 1
                self.encrypt_input_in_matrix(temp_input)
                print(self.matrix)
                self.encrypted += self.read_encrypted_string_from_matrix()
                temp_input = ""
        else:
            self.encrypt_input_in_matrix(self.input)
            self.encrypted += self.read_encrypted_string_from_matrix()

    def encrypt_input_in_matrix(self, input):
        # usuwanie spacji
        # input = self.input.replace(" ", "")

        # szyfrowanie
        order = 0
        cursor = 0

        for y in range(0, len(self.key)):
            for x in range(0, len(self.key)):
                # uzupełnianie jeśli kursor jest większy
                # od input, żeby dopelnic string
                if cursor >= len(input):
                    self.matrix[y][x] = "x"
                # uzupełnianie tekstem wejsciowym
                else:
                    self.matrix[y][x] = input[cursor]
                    cursor += 1
                # zmiana kolumny
                if self.key[x] == order:
                    order += 1
                    break

        # return matrix

    def read_encrypted_string_from_matrix(self):
        encrypted_string = ""
        order = 0

        for y in range(0, len(self.key)):
            for x in range(0, len(self.key)):
                if self.key[x] == order:
                    for cell in range(len(self.key)):
                        encrypted_string += self.matrix[cell][x]
                    order += 1

        return encrypted_string.replace(" ", "")

    def print_attributes(self):
        print(self.word)
        print(self.key)
        print(self.input)
        print(self.matrix)
        print(self.encrypted)

    def get_word(self):
        return self.word

    def get_key(self):
        return self.key

    def get_input(self):
        return self.input

    def get_matrix(self):
        return self.matrix

    def get_encrypted(self):
        return self.encrypted

# word = "ikonostas"
# input = "wczoraj trojanie nie wrocili na noc do swego miasta"
# encrypt = EncryptTranspositionCipher(word, input)
# encrypt.check_blocks_and_encrypt()
# encrypt.print_attributes()
