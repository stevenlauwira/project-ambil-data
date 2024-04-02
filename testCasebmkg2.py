import requests
import pandas as pd


def get_bmkg_data(jenis_stasiun, parameter, provinsi, kabupaten, nama_stasiun, start_date, end_date):
    url = "https://dataonline.bmkg.go.id/data_iklim"
    
    params = {
        "jenis": jenis_stasiun,
        "parameter": parameter,
        "provinsi": provinsi,
        "kabupaten": kabupaten,
        "stasiun": nama_stasiun,
        "tanggal_awal": start_date,
        "tanggal_akhir": end_date
    }
    
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print("Failed to retrieve data. Status code:", response.status_code)
        return None

jenis_stasiun = "upt"
parameter = "semuanya"
provinsi = "maluku utara"
kabupaten = "kab. kepulauan sula"
nama_stasiun = "stasiun meteorologi emalamo"
start_date = "1990-01-01"
end_date = "1999-12-31"

data = get_bmkg_data(jenis_stasiun, parameter, provinsi, kabupaten, nama_stasiun, start_date, end_date)

if data:
    df = pd.DataFrame(data)
    print(df)
else:
    print("No data retrieved.")
