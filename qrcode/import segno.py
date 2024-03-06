import segno
from PIL import Image, ImageDraw, ImageFont

# Membuat kode QR menggunakan segno
qr = segno.make('Hello, World!')

# Konversi ke gambar PIL
qr_image = qr.to_pil()

# Membuat objek ImageDraw
draw = ImageDraw.Draw(qr_image)

# Mengatur font dan teks yang akan ditambahkan
font = ImageFont.load_default()  # Atau gunakan font kustom jika diperlukan
text = "Additional Text"

# Menentukan posisi teks di bawah kode QR
text_width, text_height = draw.textsize(text, font)
text_position = ((qr_image.width - text_width) // 2, qr_image.height)

# Menambahkan teks ke gambar
draw.text(text_position, text, font=font, fill='black')

# Menyimpan gambar hasil
qr_image.save('output.png')
