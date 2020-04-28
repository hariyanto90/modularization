class Buku:
    def __init__(self, judul):
        self.judul = judul

    def __str__(self):
         return ('Judul Buku adalah = %s' % self.judul)



daftar_buku = []
daftar_buku.append(Buku('sejarah nasional'))
daftar_buku.append(Buku('habbit'))
daftar_buku.append(Buku('balada sejuta jiwa'))
daftar_buku.append(Buku('doraemon'))
