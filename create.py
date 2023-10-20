from PIL import Image, ImageDraw, ImageFont
# from datetime import date
import json

# font size list
size=[25,32,16,40]

# Open file data.json
f=open("data.json")
data=json.load(f)

# open template
tmp=Image.open("src/Template.png")

# open second image for pas photo
pas_photo=Image.open(data["pas_photo"])

# Font list
font=["font/Arrial.ttf", "font/Sign.ttf","font/Ocr.ttf"]
# Font for provinsi
fprov=ImageFont.truetype(font[0], size[0])
# Font for NIK
fnik=ImageFont.truetype(font[2],size[1])
# Font for data
fdata=ImageFont.truetype(font[0],size[2])
# Font for signature
fsign=ImageFont.truetype(font[1],size[3])

# Create condition if photo size not same 432
if pas_photo.size[0] != 432:
	croped = pas_photo.crop((0,0,432,450))
	csize = croped.resize((round(pas_photo.size[0]*0.4), round(pas_photo.size[1]*0.4)))
	tmp.paste(csize, (520,140))
else:
	csize = pas_photo.resize((round(pas_photo.size[0]*0.4), round(pas_photo.size[1]*0.4)))
	tmp.paste(csize, (520,140))

# sign
s = data["nama"].split()
sign=s[0]
print("[XXX]GENERATE FAKE E-KTP SUCCESS")
print(data)

# Draw in Image
write=ImageDraw.Draw(tmp)
write.text((380,45), f"PROVINSI {data['provinsi'].upper()}", fill=("black"), font=fprov, anchor="ms")
write.text((380,70), f"KOTA {data['kota'].upper()}", fill=("black"), font=fprov, anchor="ms")
write.text((170,105), data["nik"], fill=("black"), font=fnik, anchor="lt")
write.text((190,145), data["nama"].upper(), fill=("black"), font=fdata, anchor="lt")
write.text((190,168), data["ttl"].upper(), fill=("black"), font=fdata, anchor="lt")
write.text((190,191), data["jenis_kelamin"].upper(), fill=("black"), font=fdata, anchor="lt")
write.text((463,190), data["golongan_darah"].upper(),fill=("black"), font=fdata, anchor="lt")
write.text((190,212), data["alamat"].upper(), fill=("black"), font=fdata, anchor="lt")
write.text((190,234), data["rt/rw"].upper(), fill=("black"), font=fdata, anchor="lt")
write.text((190,257), data["kel/desa"].upper(), fill=("black"), font=fdata, anchor="lt")
write.text((190,279), data["kecamatan"].upper(), fill=("black"), font=fdata, anchor="lt")
write.text((190,300), data["agama"].upper(), fill=("black"), font=fdata, anchor="lt")
write.text((190,323), data["status"].upper(), fill=("black"), font=fdata, anchor="lt")
write.text((190,346), data["pekerjaan"].upper(), fill=("black"), font=fdata, anchor="lt")
write.text((190,369), data["kewarganegaraan"].upper(), fill=("black"), font=fdata, anchor="lt")
write.text((190,390), data["masa_berlaku"].upper(), fill=("black"), font=fdata, anchor="lt")
write.text((553,340), f"KOTA {data['kota'].upper()}", fill=("black"), font=fdata, anchor="lt")
write.text((570,360), data["terbuat"], fill=("black"), font=fdata, anchor="lt")
write.text((540,395), sign, fill=("black"), font=fsign, anchor="lt")
tmp.save("src/result.png", quality=95)
