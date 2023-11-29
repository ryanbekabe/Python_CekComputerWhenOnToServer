import requests, os, sys, socket
hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)
varhostname = f"H({hostname})"
varhostip = f"IP({ip_address})"
url = f"https://hanyajasa.com/?VHDUbuntu22_29112023_{varhostname} {varhostip}"

try:
    response = requests.get(url)
    # Periksa apakah permintaan berhasil (kode status 200)
    if response.status_code == 200:
        print("Berhasil mengakses halaman web.")
        #print(response.text)
    else:
        print(f"Gagal mengakses halaman web. Kode status: {response.status_code}")

except requests.RequestException as e:
    print(f"Terjadi kesalahan: {e}")
