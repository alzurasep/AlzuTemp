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


# Komutlar
def PrefetchSil():
    for file in PrefetchFiles:
        try:
            dosyaYolu = pathlib.Path(f"{Prefetch}\\{file}")
            dosyaYolu.unlink()
        except PermissionError:
            pass 
        except FileNotFoundError:
            pass


def LocalTempSil():
    for file in LocalTempFiles:
        try:
            dosyaYolu = pathlib.Path(f"{LocalTemp}\\{file}")
            dosyaYolu.unlink()
        except PermissionError:
            pass 
        except FileNotFoundError:
            pass
        

def TempSil():
    for file in TempFiles:
        try:
            dosyaYolu = pathlib.Path(f"{Temp}\\{file}")
            dosyaYolu.unlink()
        except PermissionError:
            pass 
        except FileNotFoundError:
            pass

def HepsiniSil():
    TempSil()
    PrefetchSil()
    LocalTempSil()

if __name__ == "__main__":
    HepsiniSil()