# Kütüphaneleri Yüklüyoruz
import pathlib
import tkinter as GUI
from tkinter import ttk as GUIW
import os


# Gereksiz Klasörleri Buluyoruz
LocalTemp = os.environ[ 'TEMP' ]
Prefetch = os.path.join( os.environ.get ( 'SystemRoot', 'C:\\Windows' ), 'Prefetch' )
Temp = os.path.join( os.environ.get ( 'SystemRoot', 'C:\\Windows' ), 'Temp' )

# Dosyaları Alıyoruz
LocalTempFiles = os.listdir(LocalTemp)
PrefetchFiles = os.listdir(Prefetch)
TempFiles = os.listdir(Temp)

# Toplam Dosya Sayısı
LocalCount = len( LocalTempFiles )
PrefetchCount = len( PrefetchFiles )
TempCount = len( TempFiles )
ToplamDosya = LocalCount + PrefetchCount + TempCount



# Arayüzü Oluşturuyoruz 
AlzuW = GUI.Tk()
AlzuW.minsize( 600, 200 )
AlzuW.maxsize( 600, 200 )
AlzuW.resizable( False, False )

AlzuW.title( "AlzuTemp" )

# Labelları Oluşturuyoruz
Toplam = GUIW.Label( AlzuW, text = f"{ToplamDosya} Dosya Bulundu" )
Toplam.pack()

PrefetchDeleted = GUI.StringVar() 
PrefetchDeleted.set(f"{PrefetchCount} Dosya 'Prefetch' içinde bulundu")
PrefetchSayisiLabel = GUIW.Label( AlzuW, text = f"{PrefetchCount} Dosya 'Prefetch' içinde bulundu", textvariable = PrefetchDeleted )
PrefetchSayisiLabel.pack()

LocalTempDeleted = GUI.StringVar()
LocalTempDeleted.set(f"{LocalCount} Dosya '%Temp%' içinde bulundu")
LocalTempSayisiLabel = GUIW.Label( AlzuW, textvariable = LocalTempDeleted )
LocalTempSayisiLabel.pack()

TempDeleted = GUI.StringVar()
TempDeleted.set(f"{TempCount} Dosya 'Temp' içinde bulundu")
TempSayisiLabel = GUIW.Label( AlzuW, text = f"{TempCount} Dosya 'Temp' içinde bulundu", textvariable = TempDeleted )
TempSayisiLabel.pack()


# Komutlar
def PrefetchSil():
    for file in PrefetchFiles:
        try:
            dosyaYolu = pathlib.Path(f"{Prefetch}\\{file}")
            dosyaYolu.unlink()
            PrefetchDeleted.set(f"{PrefetchCount} Dosya 'Prefetch' içinde bulundu")
        except PermissionError:
            pass 
        except FileNotFoundError:
            pass


def LocalTempSil():
    for file in LocalTempFiles:
        try:
            dosyaYolu = pathlib.Path(f"{LocalTemp}\\{file}")
            dosyaYolu.unlink()
            LocalTempDeleted.set(f"{LocalCount} Dosya '%Temp%' içinde bulundu")
        except PermissionError:
            pass 
        except FileNotFoundError:
            pass
        

def TempSil():
    for file in TempFiles:
        try:
            dosyaYolu = pathlib.Path(f"{Temp}\\{file}")
            dosyaYolu.unlink()
            TempDeleted.set(f"{TempCount} Dosya 'Temp' içinde bulundu")
        except PermissionError:
            pass 
        except FileNotFoundError:
            pass

def HepsiniSil():
    TempSil()
    PrefetchSil()
    LocalTempSil()

# Prefetch için Buton
PrefetchButton = GUIW.Button( AlzuW, text = "Prefetch'i Sil", width = 250, command = PrefetchSil )
PrefetchButton.pack()

# %Temp% için Buton
LocalTempButton = GUIW.Button( AlzuW, text = "%Temp%'i Sil", width = 250, command = LocalTempSil  )
LocalTempButton.pack()

# Temp için Buton
TempButton = GUIW.Button( AlzuW, text = "Temp'i Sil", width = 250, command = TempSil  )
TempButton.pack()

# Hepsi için Buton
HepsiniSil = GUIW.Button( AlzuW, text = "Hepsini Sil", width = 250, command = HepsiniSil  )
HepsiniSil.pack()

# Uygulama Başlıyor
if __name__ == "__main__":
    AlzuW.mainloop()