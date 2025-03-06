# ZeusSec1337-DDoS-Tools v1.0

ZeusSec1337-DDoS-Tools adalah alat untuk melakukan simulasi serangan DDoS menggunakan berbagai metode seperti **ICMP Flood**, **SYN Flood**, **UDP Flood**, dan **HTTP GET Flood**. Tool ini dibuat untuk keperluan edukasi dan pengujian keamanan jaringan.

> **⚠ DISCLAIMER:** Tool ini hanya untuk **pendidikan** dan **pengujian pribadi**. Penyalahgunaan alat ini dapat melanggar hukum. Gunakan dengan tanggung jawab!

---

## 🔥 Fitur

- **ICMP Flood (Ping Flood)** ➝ Mengirim paket ICMP ke target.
- **SYN Flood** ➝ Membanjiri target dengan paket SYN untuk membuat server overload.
- **UDP Flood** ➝ Mengirimkan banyak paket UDP ke port acak.
- **HTTP GET Flood** ➝ Membanjiri target dengan permintaan HTTP GET.

---

## 📌 Instalasi

### **1. Instalasi di Termux**

```bash
pkg update && pkg upgrade -y
pkg install python git -y
git clone https://github.com/sidabutar1337/ZeusSec1337-DDoS-Tools.git
cd ZeusSec1337-DDoS-Tools
pip install -r requirements.txt
python ZEUSS-DDOS.py
```

### **2. Instalasi di Linux (Debian/Ubuntu)**

```bash
sudo apt update && sudo apt upgrade -y
sudo apt install python3 python3-pip git -y
git clone https://github.com/sidabutar1337/ZeusSec1337-DDoS-Tools.git
cd ZeusSec1337-DDoS-Tools
pip3 install -r requirements.txt
python3 ZEUSS-DDOS.py
```

---

## 🎯 Cara Penggunaan

1. Jalankan script dengan:
   ```bash
   python ZEUSS-DDOS.py
   ```
2. Pilih metode serangan yang diinginkan.
3. Masukkan **target IP/Host** dan jumlah serangan.
4. Tunggu hingga proses selesai.

---

## ☕ Dukung Developer
Jika kamu ingin mendukung pengembangan tools ini, bisa berdonasi melalui link berikut:

[![Saweria](https://img.shields.io/badge/Donate-Saweria-orange)](https://saweria.co/zeussec1337)

[Donasi via Saweria](https://saweria.co/zeussec1337)

