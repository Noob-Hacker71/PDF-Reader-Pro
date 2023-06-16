import os
try:
    import pyttsx3
except:
    os.system('pip install pyttsx3')
try:
    import pdfplumber
except:
    os.system('pip install pdfplumber')
try:
    from googletrans import Translator
except:
    os.system('pip3 install googletrans==3.1.0a0')
try:
    from tkinter import *
    from tkinter import ttk
except:
    # print("Please install Tkinter Module for GUI access.")
    exit()
try:
    from PIL import ImageTk
except:
    exit()

class MainProcess:

    pageList = []
    currentPage = 0 

    def __init__(self, root):
        self.root  = root
        self.root.title("PDF Reader Pro")
        self.root.geometry("440x250+400+500")
        self.root.configure(bg='black')
        self.root.overrideredirect(True)

        # Create the widgets
        self.pdf_file_label = Label(root, text="PDF File Path:", bg='green', fg='white',font=('arial', 10, 'bold'))
        self.pdf_file_entry = Entry(root, width=34, bg='green', fg='white', font=( 'arial',12, 'bold'))
        self.pdf_file_entry.focus_set()

        self.page_number_label = Label(root, text="Page Number:",bg='green', fg='white', font=('arial', 10, 'bold'))
        self.page_number_entry = Entry(root , width=34, bg='green', fg='white', font=( 'arial',12, 'bold'))

        self.target_language_label = Label(root, text="Target Lang  :",bg='green', fg='white', font=('arial', 10, 'bold'))
        self.target_language_entry = Entry(root,  width=34, bg='green', fg='white', font=( 'arial',12, 'bold'))

        self.v = IntVar()
        # self.radioBtn = Radiobutton(root, 
        #             text="Play English Audio",
        #             padx = 20,
        #             bg='black',
        #             fg='green',
        #             font=( 'arial',10, 'bold'),
        #             variable=self.v, 
        #             value=1).place(x=150, y=140)
        


         
        self.radioBtn = Checkbutton(self.root, 
                    variable = self.v,
                    onvalue = 1,
                    offvalue = 0,
                    text="Play English Audio",
                    padx = 20,
                    bg='black',
                    fg='green',
                    font=( 'arial',10, 'bold')
                    ).place(x=150, y=140)
        

        self.play_button = Button(root, text="Translate & Play", command=self.play ,width=51, bg='green', foreground='white', font=( 'arial',10, 'bold'))
        self.exitBTN = Button(root, text="Exit Programe !", command=self.exit ,width=51, bg='red', foreground='black', font=( 'arial',10, 'bold'))




        # Layout the widgets
        self.pdf_file_label.place(x=10, y=10)
        self.pdf_file_entry.place(x=120, y=10)


        self.page_number_label.place(x=10, y=50)
        self.page_number_entry.place(x=120, y=50)

        self.target_language_label.place(x=10, y=100)
        self.target_language_entry.place(x=120, y=100)

        self.play_button.place(x=11, y=180)
        self.exitBTN.place(x=11, y=210)
    


    def play(self):

        try:
            self.read.destroy()
        except:
            pass
        
        # Get the user input
        self.pdf_file = self.pdf_file_entry.get()
        self.page_number = self.page_number_entry.get()
        self.target_language = self.target_language_entry.get()

        try:
            if len(self.pageList) == 0:
                with pdfplumber.open(self.pdf_file) as self.pdf:
                    for page in self.pdf.pages:
                        self.pageList.append(page)
                    # print(f"Your File Contains {len(self.pageList)} Pages.")
            else:
                pass
        except Exception as e:
            exit()
            # print(e)
        

        if self.v.get() == 0:
            self.currentPage = int(self.page_number)
            self.read = Tk()
            self.read.title("PDF Reader Pro By Noob-Community")
            self.read.geometry("1050x1050+500+50")
            self.read.configure(bg='black')
            # print(self.v.get())
            #Btn 
            self.preBtn = Button(self.read, text="Read Previus Page", command=self.preButton , width=40, bg='cyan', foreground='black', font=( 'arial',10, 'bold')).place(x=20, y= 10)
            # self.nxtBtn1 = Button(self.read, text="Home Page", command=self.play , width=40).place(x=380,y=10)
            self.nxtBtn = Button(self.read, text="Read Next Page", command=self.nextButton , width=40, bg='cyan', foreground='black', font=( 'arial',10, 'bold')).place(x=705,y=10)

        elif self.v.get() == 1:
            self.currentPage = int(self.page_number)
            self.audio = Tk()
            self.audio.title("PDF Reader Pro By Noob-Community")
            self.audio.geometry("350x230+600+500") 
            self.audio.configure(bg='black')
            self.pageLbl = Label(self.audio,  text=(f"Totol Page : {len(self.pageList)}"),justify='center', bg='black',fg='green', width=35, height=5, font=('times new roman', 12)).place(x=13,y=40)
            # self.getAudPage = Entry(self.audio, width=30,  ).place(x=90,y=155)
            self.playAudioBtn = Button(self.audio, text="Play Previus Page", command=self.playEngAudioPre , width=15 , bg='cyan', foreground='black', font=( 'arial',10, 'bold')).place(x=40,y=155)
            self.playAudioBtn1 = Button(self.audio, text="Play Next Page", command=self.playEngAudioNext , width=15  , bg='cyan', foreground='black', font=( 'arial',10, 'bold')).place(x=183,y=155)
            self.playAudioBtn2 = Button(self.audio, text="Exit Programe !", command=self.audioDestroy ,  width=33  , bg='red', foreground='white', font=( 'arial',10, 'bold')).place(x=40,y=190)
 

    def playEngAudioPre(self):

        try:
            if self.currentPage < len(self.pageList):
                with pdfplumber.open(self.pdf_file) as self.pdf:
                    self.getPage = self.pdf.pages[self.currentPage]
                    self.pageLbl = Label(self.audio,  text=(f"Playing Page {self.currentPage} Out Of {len(self.pageList)}"),justify='center', bg='black',fg='green', width=35, height=5, font=('times new roman', 12)).place(x=13,y=40)
                    self.currentPage -= 1
                    self.cleanText = self.getPage.extract_text()
                    # play the audio
                    self.engine = pyttsx3.init()
                    self.engine.say(self.cleanText)
                    self.engine.runAndWait()

        except Exception as e:
            self.pageLbl = Label(self.audio,  text=(f"Error Occured : {e}"),justify='center', bg='black',fg='red', width=35, height=5, font=('times new roman', 12)).place(x=13,y=40)




    def playEngAudioNext(self):
        try:
            if self.currentPage < len(self.pageList):
                with pdfplumber.open(self.pdf_file) as self.pdf:
                    self.getPage = self.pdf.pages[self.currentPage]
                    self.pageLbl = Label(self.audio,  text=(f"Playing Page {self.currentPage} Out Of {len(self.pageList)}"),justify='center', bg='black',fg='green', width=35, height=5, font=('times new roman', 12)).place(x=13,y=40)
                    self.currentPage += 1
                    self.cleanText = self.getPage.extract_text()
                    # play the audio
                    self.engine = pyttsx3.init()
                    self.engine.say(self.cleanText)
                    self.engine.runAndWait()

        except Exception as e:
            self.pageLbl = Label(self.audio,  text=(f"Error Occured : {e}"),justify='center', bg='black',fg='red', width=35, height=5, font=('times new roman', 12)).place(x=13,y=40)



        
    def audioDestroy(self):
        self.engine.stop()
        self.audio.destroy()

    def preButton (self):
        # C:\Users\one\Downloads\The_Web_Application_Hackers_Handbook.pdf
        # print("Current Page No: ",self.currentPage+1, " Out of ", len(self.pageList))
        try:
            if self.currentPage < len(self.pageList):
                with pdfplumber.open(self.pdf_file) as self.pdf:
                    self.getPage = self.pdf.pages[self.currentPage]
                    self.translator = Translator()
                    self.translation = self.translator.translate(str(self.getPage.extract_text()), dest=self.target_language)
                    self.textLbl = Label(self.read,text=self.translation.text , fg='green',justify='left',  width=104, height=50,bg='black', font=('times new roman', 12)).place(x=13,y=40)
                    self.currentPage -= 1

        except Exception as e:
            self.textLbl = Label(self.read,text=(f"Error Occured : {e}"), fg='red',  width=100, height=50,bg='black', font=('times new roman', 14)).place(x=14,y=40)









    def nextButton(self):
        # print("Current Page No: ",self.currentPage +1, " Out of ", len(self.pageList))

        try:
            if self.currentPage < len(self.pageList):
                with pdfplumber.open(self.pdf_file) as self.pdf:
                    self.getPage = self.pdf.pages[self.currentPage]
                    self.translator = Translator()
                    self.translation = self.translator.translate(str(self.getPage.extract_text()), dest=self.target_language)
                    # print(self.translation.text)
                    self.textLbl = Label(self.read,text=self.translation.text , fg='green', justify='left',  padx=40,width=104, height=50,bg='black', font=('times new roman', 12)).place(x=13,y=40)
                    self.currentPage += 1

        except Exception as e:
            self.textLbl = Label(self.read,text=(f"Error Occured : {e}"), fg='red',  width=100, height=50,bg='black', font=('times new roman', 14)).place(x=14,y=40)



    def exit(self):
        self.root.destroy()

if __name__ == "__main__":
    root = Tk()
    app = MainProcess(root)
    root.mainloop()

