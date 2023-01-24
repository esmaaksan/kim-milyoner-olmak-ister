
from tkinter import *
from tkinter.ttk import Progressbar #ilerleme çubuğu etkinliğin veya görevin geçerli durumunu belirtir
import pyttsx3
from pygame import mixer #telefon jokerine müzik eklemek için

mixer.init()
mixer.music.load('kbc.mp3') #arka plan müziği eklendi
mixer.music.play(-1)

engine = pyttsx3.init()
voices = engine.getProperty('voices') #ses ayarları
engine.setProperty('voice', voices[0].id)

questions = ["Dünyanın en büyük ülkesi hangisidir?",
             "Artık yıl kaç gündür?",
             "Gagası ve ayakları en uzun olan kuş hangisidir ?",
             "Amerika Birleşik Devletleri'nin (ABD) ulusal para birimi nedir?",
             "Guido Van Rossum 1991 yılında  hangi dili tasarlamıştır?",
             " 9, 18, 27, _ 'den sonra hangi sayı gelmelidir?",
             "Hangisi tam olarak desteklenen ilk 64 bit işletim sistemidir ?",
             "Ormanların kralı olarak bilinen hayvan hangisidir?",
             "23:23 saat kaça denk geliyor ?",
             "En çok IPL maçını hangi takım kazandı?",
             "Güneş sistemimizdeki en büyük gezegen hangisidir?",
             "Dünyada kaç tane kıta vardır?",
             "Bir Millenium'da kaç yıl vardır?",
             " Ipad hangisi tarafından üretilmiştir?",
             "Microsoft'un kurucusu kimdir?"]

first_option = ["Hindistan", "354",
                "Balıkçılgiller", "Euro",
                "Javascript", "36",
                "Windows 7", "Fil", "11:23PM", "KKR",
                "Dünya", "8",
                "100 yıl", "Google", "Monty Ritz"]

second_option = ["ABD", "366",
                 "Papağan", "Peso ",
                 "Python", "34",
                 "Linux", "Aslan", "11.11PM", "CSK",
                 "Uranus", "5",
                 "50 yıl",
                 "Microsoft", "Danis Lio"]

third_option = ["Çin", "365",
                "Karga", "Dollar",
                "Java", "30",
                "Mac", "Kaplan", "7:23PM", "MI",
                "Mars", "7",
                "500 yıl",
                "Amazon", "Bill Gates"]

fourth_option = ["Rusya", "420",
                 "Güvercin", "Yen",
                 "C++", "37",
                 "Windows XP", "İnek", "9.11PM", "RCB",
                 "Jupiter",
                 "6",
                 "1000 yıl", "Apple",
                 "Jeff Bezos"]

correct_answers = ["Rusya", "366", "Balıkçılgiller", "Dollar", "Python", "36",
                   "Linux", "Aslan", "11:23PM", "MI", "Jupiter", "7", "1000 yıl", "Apple",
                   "Bill Gates"]


def select(event): #seçim yapma fonksiyonu
    mixer.music.set_volume(1)
    b = event.widget
    value = b['text']

    callButton.config(image='')
    progressbarA.place_forget()
    progressbarLabelA.place_forget() #seyirci joker kullandıktan sonra bir sonraki soruda pencerenin kapanması için

    progressbarB.place_forget()
    progressbarLabelB.place_forget()

    progressbarC.place_forget()
    progressbarLabelC.place_forget()

    progressbarD.place_forget()
    progressbarLabelD.place_forget()
    for i in range(15): # her soru için tekrarlansın diye döngü kullandık
        if value == correct_answers[i]:
            if value == third_option[14]:
                def playagain():
                    TelefonJButton.config(state=NORMAL, image=phoneImage)
                    YarıYarıyaButton.config(state=NORMAL, image=image50)# play againle başa dönüldüğünde jokerleri sıfırlar
                    SeyirciButton.config(state=NORMAL, image=audiencePole)
                    Moneylabel.config(image=Moneyimage)
                    SoruAlanı.delete(1.0, END) #önceki soruyu silmek için
                    SoruAlanı.insert(END, questions[0])#end sondakine ekler
                    optionButton1.config(text=first_option[0])
                    optionButton2.config(text=second_option[0])
                    optionButton3.config(text=third_option[0])
                    optionButton4.config(text=fourth_option[0])
                    root2.destroy()
                    mixer.music.load('kbc.mp3')
                    mixer.music.play(-1)

                def on_closing():
                    root2.destroy()
                    root.destroy()

                Moneylabel.config(image=image15)
                mixer.music.stop()
                mixer.music.load('Kbcwon.mp3')
                mixer.music.play()
                root2 = Toplevel()
                root2.overrideredirect(True) #başlık çubuğunu görmek için
                root2.grab_set() #imleç ile ilgili
                root2.config(bg='black')
                root2.geometry('500x400+140+30')
                root2.title('1 Milyon Dolar Kazandınız')
                centerimg = PhotoImage(file='center.png')
                imgLabel = Label(root2, image=centerimg, bd=0, )
                imgLabel.pack(pady=30)

                winlabel = Label(root2, text='KAZANDINIZ', font=('arial', 40, 'bold'), bg='black', fg='white')
                winlabel.pack()

                happyimage = PhotoImage(file='happy.png')
                happYLabel = Label(root2, image=happyimage, bg='black')
                happYLabel.place(x=400, y=280)

                happYLabel1 = Label(root2, image=happyimage, bg='black')
                happYLabel1.place(x=30, y=280)

                playagainButton = Button(root2, text='Tekrar Deneyiniz', font=('arial', 20, 'bold'), bg='black', fg='white',
                                         bd=0
                                         , activebackground='black', cursor='hand2', activeforeground='white',
                                         command=playagain)
                playagainButton.pack()

                closeButton = Button(root2, text='Kapatın', font=('arial', 20, 'bold'), bg='black', fg='white', bd=0
                                     , activebackground='black', cursor='hand2', activeforeground='white',
                                     command=on_closing)
                closeButton.pack()

                root2.protocol('WM_DELETE_WINDOW', on_closing) #
                root2.mainloop()
                break

            SoruAlanı.delete(1.0, END)
            SoruAlanı.insert(END, questions[i + 1])

            optionButton1.config(text=first_option[i + 1])
            optionButton2.config(text=second_option[i + 1])
            optionButton3.config(text=third_option[i + 1])
            optionButton4.config(text=fourth_option[i + 1])
            Moneylabel.config(image=images[i])

        if value not in correct_answers: #yanlış cevap verildiğinde bu kod bloğu çalışacak
            def tryagain():
                mixer.music.load('kbc.mp3')
                mixer.music.play(-1)
                TelefonJButton.config(state=NORMAL, image=phoneImage)
                YarıYarıyaButton.config(state=NORMAL, image=image50) #try againle başa dönüldüğünde jokerleri sıfırlar
                SeyirciButton.config(state=NORMAL, image=audiencePole)

                SoruAlanı.delete(1.0, END)
                SoruAlanı.insert(END, questions[0])
                optionButton1.config(text=first_option[0])
                optionButton2.config(text=second_option[0])
                optionButton3.config(text=third_option[0])
                optionButton4.config(text=fourth_option[0])
                Moneylabel.config(image=Moneyimage)
                root1.destroy()

            def on_closing():
                root1.destroy() #pencereyi kapatmak için kullanılır
                root.destroy() #oyunu kaybettiğimiz de oyun ekranının (ana pencerenin) kapanmasının sağlar

            mixer.music.stop()
            root1 = Toplevel()
            root1.overrideredirect(True)
            root1.grab_set()
            root1.config(bg='black')
            root1.geometry('500x400+140+30')
            root1.title('0 dolar kazandınız')
            img = PhotoImage(file='center.png')
            imgLabel = Label(root1, image=img, bd=0)
            imgLabel.pack(pady=30)
            loselabel = Label(root1, text='Kaybettiniz', font=('arial', 40, 'bold'), bg='black', fg='white')
            loselabel.pack()
            sadimage = PhotoImage(file='sad.png')
            sadlabel = Label(root1, image=sadimage, bg='black')
            sadlabel.place(x=400, y=280)
            sadlabel1 = Label(root1, image=sadimage, bg='black')
            sadlabel1.place(x=30, y=280)

            tryagainButton = Button(root1, text='Tekrar Deneyiniz', font=('arial', 20, 'bold'), bg='black', fg='white', bd=0
                                    , activebackground='black', cursor='hand2', activeforeground='white',
                                    command=tryagain)
            tryagainButton.pack()

            closeButton = Button(root1, text='Kapatın', font=('arial', 20, 'bold'), bg='black', fg='white', bd=0
                                 , activebackground='black', cursor='hand2', activeforeground='white',
                                 command=on_closing)
            closeButton.pack()

            root1.protocol('WM_DELETE_WINDOW', on_closing)

            root1.mainloop()

            break


def YarıYarıya():
    YarıYarıyaButton.config(image=image50x)
    YarıYarıyaButton.config(state=DISABLED) #butonun işlevselliğini yok ediyor

    if SoruAlanı.get(1.0, 'end-1c') == questions[0]: #ilk soru için 1 ve 3.şıkkı yok eder
        optionButton1.config(text='')
        optionButton3.config(text='')

    if SoruAlanı.get(1.0, 'end-1c') == questions[1]:
        optionButton4.config(text='')
        optionButton1.config(text='')

    if SoruAlanı.get(1.0, 'end-1c') == questions[2]:
        optionButton3.config(text='')
        optionButton4.config(text='')

    if SoruAlanı.get(1.0, 'end-1c') == questions[3]:
        optionButton2.config(text='')
        optionButton4.config(text='')

    if SoruAlanı.get(1.0, 'end-1c') == questions[4]:
        optionButton3.config(text='')
        optionButton4.config(text='')

    if SoruAlanı.get(1.0, 'end-1c') == questions[5]:
        optionButton2.config(text='')
        optionButton3.config(text='')

    if SoruAlanı.get(1.0, 'end-1c') == questions[6]:
        optionButton1.config(text='')
        optionButton3.config(text='')

    if SoruAlanı.get(1.0, 'end-1c') == questions[7]:
        optionButton3.config(text='')
        optionButton4.config(text='')

    if SoruAlanı.get(1.0, 'end-1c') == questions[8]:
        optionButton2.config(text='')
        optionButton4.config(text='')

    if SoruAlanı.get(1.0, 'end-1c') == questions[9]:
        optionButton1.config(text='')
        optionButton4.config(text='')

    if SoruAlanı.get(1.0, 'end-1c') == questions[10]:
        optionButton1.config(text='')
        optionButton3.config(text='')

    if SoruAlanı.get(1.0, 'end-1c') == questions[11]:
        optionButton1.config(text='')
        optionButton2.config(text='')

    if SoruAlanı.get(1.0, 'end-1c') == questions[12]:
        optionButton1.config(text='')
        optionButton2.config(text='')

    if SoruAlanı.get(1.0, 'end-1c') == questions[13]:
        optionButton2.config(text='')
        optionButton3.config(text='')

    if SoruAlanı.get(1.0, 'end-1c') == questions[14]:
        optionButton1.config(text='')
        optionButton4.config(text='')


def SeyirciJoker():
    SeyirciButton.config(image=audiencePolex)
    SeyirciButton.config(state=DISABLED) #seyirci butonun işlevselliğini yok ediyor

    progressbarA.place(x=580, y=190)
    progressbarLabelA.place(x=580, y=320)

    progressbarB.place(x=620, y=190)
    progressbarLabelB.place(x=620, y=320)

    progressbarC.place(x=660, y=190)
    progressbarLabelC.place(x=660, y=320)

    progressbarD.place(x=700, y=190)
    progressbarLabelD.place(x=700, y=320)

    if SoruAlanı.get(1.0, 'end-1c') == questions[0]: #doğru cevap en yüksek olacak şekilde çubuk yüksekliklerin ayarı
        progressbarA.config(value=30)

        progressbarB.config(value=60)

        progressbarC.config(value=40)

        progressbarD.config(value=90)

    if SoruAlanı.get(1.0, 'end-1c') == questions[1]:
        progressbarA.config(value=30)

        progressbarB.config(value=80)

        progressbarC.config(value=40)

        progressbarD.config(value=30)

    if SoruAlanı.get(1.0, 'end-1c') == questions[2]:
        progressbarA.config(value=80)

        progressbarB.config(value=60)

        progressbarC.config(value=50)

        progressbarD.config(value=70)

    if SoruAlanı.get(1.0, 'end-1c') == questions[3]:
        progressbarA.config(value=30)

        progressbarB.config(value=70)

        progressbarC.config(value=90)

        progressbarD.config(value=50)

    if SoruAlanı.get(1.0, 'end-1c') == questions[4]:
        progressbarA.config(value=30)

        progressbarB.config(value=80)

        progressbarC.config(value=40)

        progressbarD.config(value=30)

    if SoruAlanı.get(1.0, 'end-1c') == questions[5]:
        progressbarA.config(value=80)

        progressbarB.config(value=10)

        progressbarC.config(value=40)

        progressbarD.config(value=30)

    if SoruAlanı.get(1.0, 'end-1c') == questions[6]:
        progressbarA.config(value=30)

        progressbarB.config(value=80)

        progressbarC.config(value=20)

        progressbarD.config(value=40)

    if SoruAlanı.get(1.0, 'end-1c') == questions[7]:
        progressbarA.config(value=10)

        progressbarB.config(value=70)

        progressbarC.config(value=50)

        progressbarD.config(value=30)

    if SoruAlanı.get(1.0, 'end-1c') == questions[8]:
        progressbarA.config(value=90)

        progressbarB.config(value=80)

        progressbarC.config(value=70)

        progressbarD.config(value=20)

    if SoruAlanı.get(1.0, 'end-1c') == questions[9]:
        progressbarA.config(value=30)

        progressbarB.config(value=50)

        progressbarC.config(value=70)

        progressbarD.config(value=60)

    if SoruAlanı.get(1.0, 'end-1c') == questions[10]:
        progressbarA.config(value=40)

        progressbarB.config(value=20)

        progressbarC.config(value=50)

        progressbarD.config(value=70)

    if SoruAlanı.get(1.0, 'end-1c') == questions[11]:
        progressbarA.config(value=30)

        progressbarB.config(value=80)

        progressbarC.config(value=90)

        progressbarD.config(value=40)

    if SoruAlanı.get(1.0, 'end-1c') == questions[12]:
        progressbarA.config(value=20)

        progressbarB.config(value=60)

        progressbarC.config(value=50)

        progressbarD.config(value=80)

    if SoruAlanı.get(1.0, 'end-1c') == questions[13]:
        progressbarA.config(value=60)

        progressbarB.config(value=35)

        progressbarC.config(value=40)

        progressbarD.config(value=80)

    if SoruAlanı.get(1.0, 'end-1c') == questions[14]:
        progressbarA.config(value=60)

        progressbarB.config(value=65)

        progressbarC.config(value=90)

        progressbarD.config(value=80)


def TelefonJoker():
    mixer.music.stop()
    mixer.music.load('calling.mp3')
    mixer.music.play() # müziği telefon jokeri kullanıldığın da oynatmak için

    TelefonJButton.config(image=phoneImageX, state=DISABLED)#telefon jokerinin işlevselliğini yok eder
    callButton.config(image=callimage)


def phoneclick():
    mixer.music.load('kbc.mp3')
    mixer.music.play(-1)
    mixer.music.set_volume(0)
    for i in range(15): #bu fonksiyon telefon jokerine tıklandığın da doğru cevabı söylüyor
        if SoruAlanı.get(1.0, 'end-1c') == questions[i]:
            engine.say(f'Bekir Hocam Cevabımız {correct_answers[i]}')
            engine.runAndWait()


root = Tk()#Tk kütüphanesinden root ana objesini oluşturuyoruz
root.geometry('1270x652+0+0') #dikdörtgen oluşturduk
root.resizable(0, 0)
root.title('Kim Milyoner Olmak İster')#başlık atama
root.config(bg='black') #arka plan rengini siyah yaptık

leftFrame = Frame(root, bg='black', padx=90) #root içinde bir alan oluşturduk pad x ile soldan boşluk verdik
leftFrame.grid(row=0, column=0)#ızgara yapısı uyguladık yukarıdan ve aşağıdan 0 ızgara oluşturduk

rightFrame = Frame(root, bg='black', padx=50, pady=25)
rightFrame.grid(row=0, column=1)

topFrame = Frame(leftFrame, bg='black', pady=15)#left frame içinde bir yapı oluşturduk burası joker alanı için
topFrame.grid(row=0, column=0)

middleFrame = Frame(leftFrame, bg='black', pady=15)#left frame içinde bir yapı oluşturduk
middleFrame.grid(row=1, column=0)

bottomFrame = Frame(leftFrame, bg='black')#left frame içinde yapı oluşturduk
bottomFrame.grid(row=2, column=0)

centreImage = PhotoImage(file='center.png')
logoLabel = Label(middleFrame, image=centreImage, bd=0, width=300, height=200, bg='black')
logoLabel.grid(row=0, column=0)

image50 = PhotoImage(file='50-50.png')
image50x = PhotoImage(file='50-50-X.png')

YarıYarıyaButton = Button(topFrame, image=image50, bd=0, bg='black', cursor='hand2', activebackground='black', width=180,
                      height=80, command=YarıYarıya)
YarıYarıyaButton.grid(row=0, column=0)

audiencePole = PhotoImage(file='audiencePole.png')
audiencePolex = PhotoImage(file='audiencePoleX.png')
SeyirciButton = Button(topFrame, image=audiencePole, bd=0, bg='black', cursor='hand2', activebackground='black',
                            width=180, height=80, command=SeyirciJoker)
SeyirciButton.grid(row=0, column=1)

phoneImage = PhotoImage(file='phoneAFriend.png')
phoneImageX = PhotoImage(file='phoneAFriendX.png')
TelefonJButton = Button(topFrame, image=phoneImage, bd=0, bg='black', cursor='hand2', activebackground='black', width=180,
                     height=80, command=TelefonJoker)
TelefonJButton.grid(row=0, column=2)

callimage = PhotoImage(file='phone.png')
callButton = Button(root, bg='black', bd=0, activebackground='black', cursor='hand2', command=phoneclick)
callButton.place(x=70, y=260)

Moneyimage = PhotoImage(file='Picture0.png')
image1 = PhotoImage(file='Picture1.png')
image2 = PhotoImage(file='Picture2.png')
image3 = PhotoImage(file='Picture3.png')
image4 = PhotoImage(file='Picture4.png')
image5 = PhotoImage(file='Picture5.png')
image6 = PhotoImage(file='Picture6.png')
image7 = PhotoImage(file='Picture7.png')
image8 = PhotoImage(file='Picture8.png')
image9 = PhotoImage(file='Picture9.png')
image10 = PhotoImage(file='Picture10.png')
image11 = PhotoImage(file='Picture11.png')
image12 = PhotoImage(file='Picture12.png')
image13 = PhotoImage(file='Picture13.png')
image14 = PhotoImage(file='Picture14.png')
image15 = PhotoImage(file='Picture15.png')

images = [image1, image2, image3, image4, image5, image6, image7, image8, image9, image10, image11, image12, image13
    , image14, image15]

Moneylabel = Label(rightFrame, image=Moneyimage, bg='black', bd=0)
Moneylabel.grid(row=0, column=0)

layoutimage = PhotoImage(file='lay.png')
layoutlabel = Label(bottomFrame, image=layoutimage, bg='black', bd=0)
layoutlabel.grid(row=0, column=0)


SoruAlanı = Text(bottomFrame, font=('arial', 18, 'bold'), bg='black', fg='white', width=34, height=2,
                        wrap='word',bd=0)
SoruAlanı.place(x=70,y=10)

SoruAlanı.insert(END, questions[0])




labelA = Label(bottomFrame, font=('arial', 16, 'bold'), text='A:', bg='black', fg='white')
labelA.place(x=60,y=110)

optionButton1 = Button(bottomFrame, text=first_option[0], font=('arial', 18, 'bold'), bg='black', fg='white',
                              cursor='hand2',bd=0,activebackground='black',activeforeground='white')
optionButton1.place(x=100,y=100)

labelB = Label(bottomFrame, font=('arial', 16, 'bold'), text='B:', bg='black', fg='white')
labelB.place(x=330,y=110)

optionButton2 = Button(bottomFrame, text=second_option[0], font=('arial', 18, 'bold'), bg='black', fg='white',
                              cursor='hand2',bd=0,activebackground='black',activeforeground='white')
optionButton2.place(x=370,y=100)

labelC = Label(bottomFrame, font=('arial', 16, 'bold'), text='C:', bg='black', fg='white')
labelC.place(x=60,y=190)

optionButton3 = Button(bottomFrame, text=third_option[0], font=('arial', 18, 'bold'), bg='black', fg='white',
                             cursor='hand2',bd=0,activebackground='black',activeforeground='white')
optionButton3.place(x=100,y=180)

labelD = Label(bottomFrame, font=('arial', 16, 'bold'), text='D:', bg='black', fg='white')
labelD.place(x=330,y=190)

optionButton4 = Button(bottomFrame, text=fourth_option[0], font=('arial', 18, 'bold'), bg='black', fg='white',
                             cursor='hand2',bd=0,activebackground='black',activeforeground='white')
optionButton4.place(x=370,y=180)

progressbarA = Progressbar(root, orient=VERTICAL, mode='determinate', length=120)

progressbarLabelA = Label(root, text='A', font=('arial', 20, 'bold'), bg='black', fg='white')

progressbarB = Progressbar(root, orient=VERTICAL, mode='determinate', length=120)

progressbarLabelB = Label(root, text='B', font=('arial', 20, 'bold'), bg='black', fg='white')

progressbarC = Progressbar(root, orient=VERTICAL, mode='determinate', length=120)

progressbarLabelC = Label(root, text='C', font=('arial', 20, 'bold'), bg='black', fg='white')

progressbarD = Progressbar(root, orient=VERTICAL, mode='determinate', length=120)

progressbarLabelD = Label(root, text='D', font=('arial', 20, 'bold'), bg='black', fg='white')

optionButton1.bind('<Button-1>', select)
optionButton2.bind('<Button-1>', select)
optionButton3.bind('<Button-1>', select)
optionButton4.bind('<Button-1>', select)

root.mainloop()