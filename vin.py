def int_to_string(angka):
    angka_dict = ['nol', 'satu', 'dua', 'tiga', 'empat', 'lima', 'enam', 'tujuh', 'delapan', 'sembilan']
    return ' '.join(angka_dict[int(digit)] for digit in str(angka))

# Contoh penggunaan
hasil = int_to_string(3124)
print(hasil)  # Output: 'tiga satu dua empat'
