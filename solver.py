#!/usr/bin/python3

import sys, string, re

# split a word into an array of characters
def split(word):
    return [char for char in word]

def manual():
    print("PEMAKAIAN: ")
    print("./solver.py <huruf-huruf dalam katla> <huruf-huruf tidak dalam katla> <penempatan huruf>")
    print("<huruf-huruf dalam katla> adalah huruf-huruf yang kamu ketahui ada pada katla; tuliskan tanpa spasi. contoh: ab")
    print("<huruf-huruf tidak dalam katla> adalah huruf-huruf yang kamu ketahui tidak ada pada katla; tuliskan tanpa spasi. contoh: sd")
    print("<penempatan huruf> adalah penempatan tata letak huruf-huruf yang kita ketahui saat ini dituliskan, dan yang tidak diketahui ditandai dengan underscore. contoh: aba__")
    print("")
    print("CATATAN: ")
    print("jika kamu tidak memiliki informasi yang cukup untuk mengisi salah satu argumen di atas, dapat di isi argument dengan tanda tanya \"?\"")

def errorout():
    print("Terjadi ERROR: ")
    print("Penempatan huruf harus tepat 5 karakter, dan hanya terdiri dari huruf dan underscore\n")

# validate args
if len(sys.argv) != 4 or len(sys.argv) == 2:
    manual()
    exit()

dictionary = open("words.txt", "r")
words = dictionary.readlines()
print("Telah mengambil " + str(len(words)) + " kata dari kamus.\n")
dictionary.close()

# this will be the array with the possible answers
solutions = []

# remove new lines from words in array, put them into solutions array
for word in words:
   solutions.append(word.strip())

# check sys.argv[1] and sys.argv[2]
allowed = set(string.ascii_lowercase + '?')
if not set(sys.argv[1] + sys.argv[2]) <= allowed:
   print("Argumen pertama dan kedua harus berupa huruf kecil, atau menggunakan tanda tanya tunggal (?) sebagai pengganti") 

# remove words without the necessary chars
if sys.argv[1] != '?':
    solutions = [x for x in solutions if all(y in x for y in sys.argv[1])]

# remove words with characters that we know aren't in the solution
if sys.argv[2] != '?':
    solutions = [x for x in solutions if all(y not in x for y in sys.argv[2])]

regex = sys.argv[3]
if regex == '?':
    regex = "_____"
allowed = set(string.ascii_lowercase + '_')
if not set(regex) <= allowed:
    errorout()
    manual()
    exit()
if len(regex) != 5:
    errorout()
    manual()
    exit()
    
regex = regex.replace("_", ".")

# match based on regex
regex_pattern = "^" + regex + "$"
pattern = re.compile(regex_pattern)

for word in solutions:
    if pattern.match(word):
        print(word)