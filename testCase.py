# from selenium import webdriver

# driver = webdriver.Chrome()
# driver.maximize_window()

# driver.get("https://dataonline.bmkg.go.id/home")

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# URL login
login_url = "https://dataonline.bmkg.go.id/home"

# Menjalankan driver Microsoft Edge
driver = webdriver.Edge()
# executable_path="C:\Users\steve\Desktop\project mengambil data\msedge.exe"
driver.maximize_window()
# Mengakses URL login
driver.get(login_url)

# Menunggu halaman login dimuat
sleep(5)

# Mengisi alamat email
email_field = driver.find_element(By.ID, "Email")
email_field.send_keys("your_email@domain.com")

# Mengisi kata sandi
password_field = driver.find_element(By.ID, "Kata Sandi")
password_field.send_keys("your_password")

# Menekan tombol login
login_button = driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary")
login_button.click()

# user_input = input("Tekan 'q' untuk menutup browser: ")
# if user_input.lower() == 'q':
#     driver.quit()