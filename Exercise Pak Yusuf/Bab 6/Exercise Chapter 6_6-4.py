glossary = {
    'string': 'Rangkaian karakter.',
    'comment': 'Catatan di program yang diabaikan oleh interpreter Python.',
    'list': 'Kumpulan item dalam urutan tertentu.',
    'loop': 'Memproses kumpulan item satu per satu.',
    'tuple': 'Kumpulan item berurutan yang isinya tidak bisa diubah.',
    'variable': 'Nama yang dipakai untuk menyimpan sebuah nilai.',
    'index': 'Nomor posisi sebuah item di dalam list, dimulai dari 0.',
    'slice': 'Potongan dari sebuah list, misalnya cubes[:3].',
    'method': 'Fungsi yang melekat pada sebuah objek, misalnya title().',
    'boolean': 'Nilai yang hanya bisa True atau False.',
}

for word, meaning in glossary.items():
    print(f"\n{word.title()}: {meaning}")