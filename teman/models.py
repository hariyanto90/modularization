class Teman:
    def __init__(self, nama, sex):
        self.nama = nama
        self.sex = sex
        self.alamat = ''

    def __str__(self):
        return ('nama = %s, jenis kelamin = %s, alamat = %s' % (self.nama, self.sex, self.alamat))


daftar_teman = []


daftar_teman.append(Teman('joko', 'laki-laki'))
daftar_teman.append(Teman('prabowo', 'laki-laki'))
daftar_teman.append(Teman('mega', 'perempuan'))

sby = Teman('sby', 'laki-laki')
sby.alamat = ('ambon')
daftar_teman.append(sby)
# daftar_teman.append(Teman('sby', 'laki-laki'))
# daftar_teman.append('ani')
# daftar_teman.append('ene')
# daftar_teman.append('ono')
# daftar_teman.append('ina')



