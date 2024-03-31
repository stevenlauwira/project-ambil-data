import requests

# Fungsi untuk login ke situs
def login(Email, Kata_Sandi):
    login_url = 'https://dataonline.bmkg.go.id/home'
    session = requests.Session()
    login_data = {
        'Email': Email,
        'Kata Sandi': Kata_Sandi
    }
    response = session.post(login_url, data=login_data)
    if response.status_code == 200:
        print('Login berhasil!')
        return session
    else:
        print('Login gagal!')
        return None

# Fungsi untuk mendapatkan data yang diinginkan setelah login
def get_data(session):
    base_url = 'https://dataonline.bmkg.go.id/home'
    response = session.get(base_url)
    if response.status_code == 200:
        # Lakukan sesuatu dengan data yang diperoleh
        # Misalnya, olah data atau simpan ke dalam file
        print('Data berhasil diperoleh!')
    else:
        print('Gagal mendapatkan data.')

# Contoh penggunaan:
Email = input('Masukkan email: ')
Kata_Sandi = input('Masukkan Katas andi: ')

# Login
session = login(Email, Kata_Sandi)
if session:
    # Jika login berhasil, dapatkan data yang diinginkan
    get_data(session)
else:
    print('Terjadi kesalahan saat login.')
