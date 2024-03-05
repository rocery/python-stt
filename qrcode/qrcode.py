# STRUKTUR FOLDER
# <folder>
# |-- qrcode.py
# |-- data.csv
# |-- /hasil
# |    -- qrcode.png

from segno import helpers
import csv
import os

# Load data, ganti nama <data.csv> sesuai data yang ada. Gunakan file csv'
data = "data.csv"
# Folder tempat simpan hasil generate qrcode, ganti folder jika diinginkan
forder_save = "test"
# scaleSize gigunakan untuk memperbesar resolusi hasil generate
scaleSize = 10
# Ganti ukuran sisi garis qrcode jika akan digunakan pada background gelap
borderSize = 1

# Cek folder, jika tidak ada buat baru
if not os.path.exists(forder_save):
    os.makedirs(forder_save)

# Buka File CSV
with open(data, "r") as fp:
    reader = csv.DictReader(fp)
    line_count = 1
    line_error = 0
    for row in reader:
        if row["nama"] == "":
            print(f"{line_count}. Nama kosong, mohon periksa data.")
            line_error += 1
        elif row["qrcode"] == "":
            print(f"{line_count}. Qrcode kosong, mohon periksa data.")
            line_error += 1
        else:
            qrcode = helpers.make_mecard(name=f"{row['nama']}",
                                         url=f"{row['qrcode']}",
                                         )
            # to_artistic to add pic, .save use default settings
            qrcode.save(
                # background = "back.jpg",
				# target = 
                f"{forder_save}/{row['nama']}.png",
				scale = scaleSize,
				border = borderSize,
                light = (255, 255, 255),
			)
            print(f"{line_count}. Pembuatan QrCode data pegawai: {row['nama']} berhasil!")
        line_count += 1
    print(f"Data terbaca {line_count - 1}")
    print(f"Data diproses {line_count - 1 - line_error}")
    print(f"Data error {line_error}")
    print(f"Data disimpan di folder '{forder_save}'")
