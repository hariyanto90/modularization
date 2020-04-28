from models import daftar_buku

def run_view():
    print('daftar buku')
    print('------------')

    for dn in daftar_buku:
        print(dn)