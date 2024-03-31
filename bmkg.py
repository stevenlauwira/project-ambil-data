import requests
import pandas as pd
from bs4 import BeautifulSoup
from datetime import datetime, timedelta

# Fungsi untuk login ke situs
def login(Email, Kata_Sandi):
    login_url = 'https://dataonline.bmkg.gosteven.id/home'
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

def get_available_parameters():
    base_url = "https://dataonline.bmkg.go.id/data_iklim"
    response = requests.get(base_url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        parameter_select = soup.find("select", {"id": "parameter"})
        parameters = [option["value"] for option in parameter_select.find_all("option")]
        return parameters
    else:
        return []

def download_data(provinsi, jenis_stasiun, no_stasiun, parameters, kabupaten, start_date, end_date):
    base_url = "https://dataonline.bmkg.go.id/data_iklim"
    for parameter in parameters:
        current_date = start_date
        while current_date <= end_date:
            year_month = current_date.strftime("%Y%m")
            last_day_of_month = current_date.replace(day=1) + timedelta(days=32)
            last_day_of_month = last_day_of_month - timedelta(days=last_day_of_month.day)
            
            if current_date < last_day_of_month:
                next_month_first_day = current_date.replace(day=1) + timedelta(days=32)
                next_month_first_day = next_month_first_day - timedelta(days=next_month_first_day.day)
                delta = next_month_first_day - current_date
            else:
                delta = last_day_of_month - current_date

            params = {
                "tipe": "monthly",
                "start_year": year_month,
                "end_year": year_month,
                "prov": provinsi,
                "jenis_stasiun": jenis_stasiun,
                "no_stasiun": no_stasiun,
                "parameter": parameter,
                "kabupaten": kabupaten,
                "action": "download"
            }
            response = requests.get(base_url, params=params)
            if response.status_code == 200:
                df = pd.read_csv(response.text, sep=";")
                file_name = f"{provinsi}_{jenis_stasiun}_{no_stasiun}_{parameter}_{kabupaten}_{year_month}.xlsx"
                df.to_excel(file_name, index=False)
                print(f"Data untuk parameter {parameter} pada bulan {year_month} berhasil diunduh dan disimpan dalam format Excel.")
            else:
                print(f"Gagal mengunduh data untuk parameter {parameter} pada bulan {year_month}.")
            current_date = current_date + delta

# Mendapatkan daftar parameter yang tersedia dari BMKG
available_parameters = get_available_parameters()

if available_parameters:
    print("Parameter yang tersedia:")
    for parameter in available_parameters:
        print(parameter)
    
    # Meminta masukan dari pengguna untuk tanggal awal, tanggal akhir, jenis stasiun, dan nomor stasiun
    start_date_input = input("Masukkan tanggal awal (format: DD-MM-YYYY): ")
    end_date_input = input("Masukkan tanggal akhir (format: DD-MM-YYYY): ")
    jenis_stasiun = input("Masukkan jenis stasiun: ")
    no_stasiun = input("Masukkan nomor stasiun: ")
    provinsi = input("masukan nama provinsi: ")
    kabupaten = input("masukan nama kabupaten: ")

    # Melakukan parsing tanggal awal dan akhir
    start_date = datetime.strptime(start_date_input, "%d-%m-%Y")
    end_date = datetime.strptime(end_date_input, "%d-%m-%Y")

    # Contoh penggunaan:
    parameters = available_parameters  # Memilih semua parameter yang tersedia

    download_data(provinsi, jenis_stasiun, no_stasiun, parameters, kabupaten, start_date, end_date)
else:
    print("Gagal mendapatkan daftar parameter yang tersedia dari BMKG.")
