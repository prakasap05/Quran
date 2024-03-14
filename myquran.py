from alquran_id import AlQuran as Quran
import os,sys

def alquran(id_surat, id_ayat):
    quran = Quran()
    nama_surat = quran.Surat(id_surat)
    ar_ayt = quran.ArNumber(id_ayat)
    ayat = quran.Ayat(id_surat, id_ayat)
    jml_ayat = quran.JumlahAyat(id_surat)
    terjemahan = quran.Terjemahan(id_surat, id_ayat)
    tafsir = quran.Tafsir(id_surat, id_ayat)
    return nama_surat[0], nama_surat[1], ayat, jml_ayat, terjemahan, tafsir, ar_ayt

os.system('clear') #change cls or clear
print(f"""
######################################
Al-Quran Indonesia | Libary alquran_id
      Developed by Prakasa Putra
######################################

""")
kas_surah = input('Masukkan nomor surah: ')
kas_ayat = input('Masukkan nomor ayat nya: ')

quran = alquran(kas_surah, kas_ayat)
print('---------------------------------------------------')
print(f"""
Nama Surat      = {quran[0]} / {quran[1]}
Jumlah Ayat     = {quran[3]}
Ayat		= [{quran[6]}]

{quran[2]}

Terjemahan	= {quran[4]}
Tafsir		= {quran[5]}
""")
