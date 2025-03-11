def int_to_string(angka):
    angka_dict = ['nol', 'satu', 'dua', 'tiga', 'empat', 'lima', 'enam', 'tujuh', 'delapan', 'sembilan']
    hasil = ""
    for digit in str(angka):
        hasil += angka_dict[int(digit)] + " "
    return hasil.strip()  # Menghapus spasi di akhir

# Contoh penggunaan
print(int_to_string(3124))  # Output: 'tiga satu dua empat' 
