from tkinter import*
from tkinter import messagebox
from tkinter import ttk

win = Tk()
win.title("ÖĞRENCİ TANIMA VE NOT HESAPLAMA SİSTEMİ")
win.geometry("1000x600")
win.resizable(FALSE, FALSE)

def karsila():
    s1 = str(entadi.get())
    s2 = str(entsoyadi.get())
    s3 = str(entnumara.get())
    lblkarsilama["text"] = str("Hoşgeldin ") + str(s1) + str(" ") + str(s2) + str(" ") + \
                           str("(") + str(s3) + str(")") + str("\n \n Not Ortalaması ve Başarı Durumu "
                                                               "Öğrenmek İçin Sınav Notlarını Aşağıdaki Kutucuklara "
                                                               "Yazabilirsin...")

    cbolum.current(0)
    entnumara.delete(0, "end")
    entsoyadi.delete(0, "end")
    entadi.delete(0, "end")


def ortalama():
    s1 = int(entvize.get())
    s2 = int(entfinal.get())
    s3 = int(s1*40/100) + int(s2*60/100)
    lblnotortalamasi["text"] = int(s3)


def basari():
    s1 = int(entvize.get())
    s2 = int(entfinal.get())
    s3 = int(s1*40/100) + int(s2*60/100)
    if s3>=60:
        lblbasaridurumu["text"] = str("Geçti")
    else:
        lblbasaridurumu["text"] = str("Kaldı")


lblbaslik = Label(win, text="ÖĞRENCİ TANIMA ve NOT HESAPLAMA SİSTEMİ", font="Verdna 16 bold",  fg="red")
lblbaslik.place(x=230, y=10)
lbladi = Label(win, text="Öğrencinin Adı: ", font="Verdana 12 bold")
lbladi.place(x=40, y=70)
lblsoyadi = Label(win, text="Öğrencinin Soyadı: ", font="Verdana 12 bold")
lblsoyadi.place(x=500, y=70)
lblnumara = Label(win, text="Öğrencinin Numarası: ", font="Verdana 12 bold")
lblnumara.place(x=40, y=120)
lblbolum = Label(win, text="Öğrencinin Bölümü: ", font="Verdana 12 bold")
lblbolum.place(x=500, y=120)

lblvize =Label(win, text="Vize Notu:", font="Verdana 12 bold")
lblvize.place(x=40, y=350)
lblfinal =Label(win, text="Final/Bütünleme Notu: ", font="Verdana 12 bold")
lblfinal.place(x=40, y=450)

lblkarsilama = Label(win, font="Verdana 12 bold")
lblkarsilama.place(x=50, y=240)

lblnotortalamasi = Label(win, font="Verdana 12 bold", fg="blue")
lblnotortalamasi.place(x=750, y=400)
lblbasaridurumu = Label(win, font="Verdana 12 bold", fg="blue")
lblbasaridurumu.place(x=740, y=500)

lblnot = Label(win, text="Not: Sınav Puanları Hesaplamasında Vize Notunun %40 ı"
                         "Final Notunun %60 ı alınarak hesaplanır.\n"
                         "Not Ortalamasının 60 Puanı Geçmesi Dahilinde Dersten Geçilir.", font="Verdana 12 bold")
lblnot.place(x=40, y=540)


entadi = Entry(win, font="Verdana 12 bold", fg="blue", width=22)
entadi.place(x=240, y=70)
entsoyadi = Entry(win, font="Verdana 12 bold", fg="blue", width=22)
entsoyadi.place(x=690, y=70)
entnumara = Entry(win, font="Verdana 12 bold", fg="blue", width=22)
entnumara.place(x=240, y=120)
entvize = Entry(win, font="Verdana 12 bold", fg="blue", width=22)
entvize.place(x=250, y=350)
entfinal = Entry(win, font="Verdana 12 bold", fg="blue", width=22)
entfinal.place(x=250, y=450)

cbolum = ttk.Combobox(win, font="Verdana 12 bold")
cbolum["values"] = ("Seçiniz...", "Bilgisayar Programcılığı", "Yönetim Bilişim Sistemleri", "Bilgisayar Mühendisliği")
cbolum.current(0)
cbolum.place(x=690, y=120)


btnkaydet = Button(win, text="Sisteme Giriş", font="Verdana 12 bold", fg="blue", command=karsila)
btnkaydet.place(x=430, y=190)
btnnotortalamasi = Button(win, text="Not Ortalaması", font="Verdana 12 bold", fg="blue", command=ortalama)
btnnotortalamasi.place(x=690, y=350)
btnbasaridurumu = Button(win, text="Başarı Durumu", font="Verdana 12 bold", fg="blue", command=basari)
btnbasaridurumu.place(x=700, y=450)

win.mainloop()