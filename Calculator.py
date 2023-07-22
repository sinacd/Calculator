import tkinter
from tkinter import *
from tkinter import ttk
from tkinter.font import BOLD, Font
import tkinter.messagebox
import logging
logging.basicConfig(filename='sample.log',level=logging.INFO,format='%(asctime)s:%(name)s:%(message)s')

root = Tk()
root.title('Calculator')
root.geometry('350x500')
height = 500
width = 350
root.minsize(width=width, height=height)
color='#202020'
root.configure(bg=color)
p1 = PhotoImage(file="icon.png")
root.iconphoto(False, p1)
#==================classes=============================

class ButtonStyle1(Button):

   def __init__(self, *args, **kwargs):
      super().__init__(*args, **kwargs)
      self.initial()
      self.bind('<Enter>', self.enter)
      self.bind('<Leave>', self.leave)

   def enter(self, event):
      self['bg'] = btnHoverBg

   def leave(self, event):
      self['bg'] = btnBg

   def initial(self):
      self['activebackground']=btnClickBg
      self['activeforeground']=btnNumberBg


#==================frames===============================
top1divHeight = height/2.77
fillStutus = 'both'
expandStatus = True
top2divHeight = height - top1divHeight
#=============================================================
btnClickBg = "#282828"
btnNumberBg = "#ffffff"
btnNegWidth = 8
btnNegheight = 19
btnBg = "#3b3b3b"
btnHoverBg = "#323232"
fontSize = ("Arial", 12)
btnNegheight1 = 2
#============================================functions================================================
class functions():
   def __init__(self):
      self.frame = Frame(root, width=0, height=20, bg=color)
      self.top1div = Frame(root, width=350, height=top1divHeight, bg=color)
      self.top2div = Frame(root, width=350, height=top2divHeight / 6, bg=color)
      self.top3div = Frame(root, width=350, height=top2divHeight / 6, bg=color)
      self.top4div = Frame(root, width=350, height=top2divHeight / 6, bg=color)
      self.top5div = Frame(root, width=350, height=top2divHeight / 6, bg=color)
      self.top6div = Frame(root, width=350, height=top2divHeight / 6, bg=color)
      self.top7div = Frame(root, width=350, height=top2divHeight / 6, bg=color)
      self.frame.pack(side=RIGHT, expand=expandStatus, fill=fillStutus)
      self.top1div.pack(side=TOP,expand=expandStatus, fill=fillStutus, pady=45)
      self.top2div.pack(side=TOP, expand=expandStatus, fill=fillStutus)
      self.top3div.pack(side=TOP, expand=expandStatus, fill=fillStutus)
      self.top4div.pack(side=TOP, expand=expandStatus, fill=fillStutus)
      self.top5div.pack(side=TOP, expand=expandStatus, fill=fillStutus)
      self.top6div.pack(side=TOP, expand=expandStatus, fill=fillStutus)
      self.top7div.pack(side=TOP, expand=expandStatus, fill=fillStutus)
      self.finished = False
      self.previousOprator = ""
      self.previousOperand = ""
      self.previousEquations = []
      self.ListHistoryButtons = []
      self.totalExpression = ""
      self.currentExpression = "0"
      self.totalLabel = Label(self.top1div, text=self.totalExpression, bg=color, fg='grey', anchor=tkinter.E, padx=24, width=80, height=0,
                      font=("Arial", 11))
      self.totalLabel.pack()

      self.currentLabel = Label(self.top1div, text=self.currentExpression, bg=color, fg='white', anchor=tkinter.E, padx=24, width=80,
                        height=0, font=("Arial", 40, BOLD))
      self.currentLabel.pack()
   def creatButton(self,numberOfButtons, frameName, value):
      for x in range(0, numberOfButtons):
         ButtonStyle1(frameName, command=lambda x=value[x]: self.addNumberToCurrentLabel(x), text=value[x],
                            width=btnNegWidth,
                            height=btnNegheight1, bg=btnBg, fg=btnNumberBg, relief='flat', font=fontSize).pack(side=LEFT, expand=True,fill='both', padx=1, pady=1)

   def addNumberToCurrentLabel(self,value):
      if (self.currentExpression == "0" or self.finished) and value != "." :  # remove zerp after adding value also delete value after an equasion
         self.currentExpression = ""
         self.currentLabelConfig()
         self.totalLabel.config(text=self.totalExpression)
         self.finished = False
      if value == "." and "." in self.currentExpression:
         self.currentExpression = self.currentExpression
      else:
         self.currentExpression += str(value)
         self.currentLabelConfig()

   def addOperatorToCurrentLabel(self,value):
      # if self.totalExpression[-1] = + * - /  fix this

      numbers = [1,2,3,4,5,6,7,8,9,0]
      self.totalExpression += self.currentExpression
      self.totalExpression += value
      self.previousOprator = value
      if self.totalExpression[-2] not in str(numbers):
         self.totalExpression = self.totalExpression[0:-2:1] + value
      self.currentExpression = ""
      operatorSymbol = {"*" : "\u00D7"}   #change * to x
      for key,value in operatorSymbol.items():
         tempExpression = self.totalExpression.replace(key,value)
      self.totalLabel.config(text=tempExpression)
   def showEqualInCurrentLabel(self):
      try:
         if self.totalExpression == "":
            self.totalExpression += self.currentExpression
            if self.previousOprator !="":
               self.totalExpression += self.previousOprator
               self.totalExpression += self.previousOperand
         else:
            if self.currentExpression == "" and self.previousOprator!= "":# for example if typed 3+=
               self.currentExpression = self.totalExpression[0:-1:1]
            self.previousOperand = self.currentExpression
            self.totalExpression += self.currentExpression
         self.totalExpression += "="
         self.currentExpression = str(eval(self.totalExpression[0:-1:1]))
         self.totalLabel.config(text=self.totalExpression)
         self.previousEquations += [self.totalExpression + self.currentExpression]
         if size.currentSize ==list(size.sizeDic.keys())[1]:
            self.addToHistory()
         self.currentLabelConfig()

      except Exception as s:
         logging.info(f'the error is {s}')
         logging.info(f'the totalExpression is {self.totalExpression}')
         logging.info(f'the currentExpression is {self.currentExpression}')
         logging.info(f'previousOprator  is {self.previousOprator}')
         logging.info(f'previousOperand  is {self.previousOperand}')
         logging.info(f'previousOperand  is {self.previousEquations}')
         logging.info(f'==========================================================')
         self.totalExpression += str(s)
         self.totalLabel.config(text=self.totalExpression)
         self.currentExpression = "Error"
         self.currentLabel.config(text=self.currentExpression)
         self.currentExpression = "0"
         self.previousOperand = ""
         self.previousOprator = ""
      finally:
         self.totalExpression = ""
         self.finished = True


   def backSpace(self):
      self.currentExpression = self.currentExpression[0:-1]
      self.currentLabelConfig()
      if self.currentExpression == "":
         self.currentExpression = "0"
         self.currentLabelConfig()
   def clear(self):
      self.currentExpression = "0"
      self.currentLabelConfig()
      self.totalExpression = ""
      self.totalLabel.config(text=self.totalExpression)
   def clearEntry(self):
      self.currentExpression = "0"
      self.currentLabelConfig()
   def square(self):
      self.totalExpression = self.currentExpression + "\u00b2"
      self.totalLabel.config(text=self.totalExpression)
      self.totalExpression =  ""
      self.currentExpression = str(eval(f"{self.currentExpression}**2"))
      self.currentLabelConfig()
      self.previousOperand = self.currentExpression
   def sqrt(self):
      self.totalExpression = "\u221a" + self.currentExpression
      self.totalLabel.config(text=self.totalExpression)
      self.totalExpression =  ""
      self.currentExpression = str(eval(f"{self.currentExpression}**0.5"))
      self.currentLabelConfig()
      self.previousOperand = self.currentExpression
   def negetive(self):
      self.currentExpression = str(eval(f"-{self.currentExpression}"))
      self.currentLabelConfig()
      self.previousOperand = self.currentExpression
   def reverse(self):
      self.currentExpression = str(eval(f"1/{self.currentExpression}"))
      self.currentLabelConfig()
      self.previousOperand = self.currentExpression
   def keyboardBind(self):
      numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0,"."]
      for number in numbers:
         root.bind(str(number) , lambda event,digit=number : self.addNumberToCurrentLabel(digit))
      operators = ["*","+","-","/"]
      for operator in operators:
         root.bind(operator , lambda event,digit=operator : self.addOperatorToCurrentLabel(digit))
      root.bind('<Return>', lambda event : self.showEqualInCurrentLabel())
      root.bind('<BackSpace>', lambda event : self.backSpace())
   def currentLabelConfig(self,):
      if self.currentExpression != "" and self.currentExpression[-1] != ".":
         flo = float(self.currentExpression)
         temp = '{0:.9g}'.format(flo)
         self.currentLabel.config(text=temp)
      else:
         self.currentLabel.config(text=self.currentExpression)
   def quit(self):
      if tkinter.messagebox.askyesno("Quit", "Are you sure to close the window"):
         # close the application
         root.after(300,root.quit())

   aTHIndex =0
   menu = []
   def addToHistory(self):
      if self.previousEquations != []:
         self.ListHistoryButtons += [Button(self.myCanvasFrame,
                                           command=lambda x=self.previousEquations[-1]: functions.setValuesFromHistory(
                                              x), text=self.previousEquations[-1], width=38, anchor=E,
                                           height=btnNegheight1, bg=color, activebackground=color,
                                           activeforeground=btnNumberBg, fg=btnNumberBg,
                                           relief='flat', font=fontSize
                                           )]
         self.ListHistoryButtons[-1].grid(row=2 + self.aTHIndex, column=0, pady=2, columnspan=3, ipadx=9)
         self.aTHIndex += 1
      self.HistoryLabel.destroy()
      self.myCanvas.config(scrollregion=self.myCanvas.bbox("all"), yscrollcommand=self.sb.set)

      def delete(x):
         self.ListHistoryButtons[x].destroy()
      #return value but 3 and remove from last
      def createMenu(x):
         self.menu += [Menu(self.ListHistoryButtons[x], tearoff=False,bg=color, fg=btnNumberBg,font=("Arial", 10))]
         self.menu[x].add_command(label="Delete", command=lambda: delete(x))
         self.ListHistoryButtons[x].bind('<Button-3>',lambda event , y = x :self.rightClickPopup(event,y))

      createMenu(self.aTHIndex-1)
      def enter( event,x):
         self.ListHistoryButtons[x]['bg'] = btnBg

      def leave( event,x):
         self.ListHistoryButtons[x]['bg'] = color
      self.ListHistoryButtons[self.aTHIndex-1].bind('<Enter>',lambda e,x=self.aTHIndex-1 :enter(e,x))
      self.ListHistoryButtons[self.aTHIndex-1].bind('<Leave>',lambda e,x=self.aTHIndex-1:leave(e,x))
#===================================
   def setValuesFromHistory(self,x):
      temp = x.split('=')
      self.totalExpression = temp[0]
      self.totalExpression += "="
      self.currentExpression = temp[1]
      self.totalLabel.config(text=self.totalExpression)
      self.currentLabelConfig()
      self.previousOperand = self.currentExpression
      self.totalExpression = ""
      self.finished = True

   def rightClickPopup(self,event,x):
      self.menu[x].tk_popup(event.x_root,event.y_root)

   def sharedPartsOfTheLayouts(self):
      self.totalLabel = Label(self.top1div, text=self.totalExpression, bg=color, fg='grey', anchor=tkinter.E, padx=24,
                              width=80, height=0,
                              font=("Arial", 11))
      self.totalLabel.pack()

      self.currentLabel = Label(self.top1div, text=self.currentExpression, bg=color, fg='white', anchor=tkinter.E,
                                padx=24, width=80,
                                height=0, font=("Arial", 40, BOLD))
      self.currentLabel.pack()

      btnNeg = ButtonStyle1(self.top7div, command=lambda: functions.negetive(), text='+/-', width=btnNegWidth,
                            height=btnNegheight1, bg=btnBg, fg=btnNumberBg, relief='flat', font=fontSize)
      btnNeg.pack(side=LEFT, expand=True, fill='both', padx=1, pady=1)
      functions.creatButton(2, self.top7div, [0, "."])
      btnEqual = Button(self.top7div, command=lambda: functions.showEqualInCurrentLabel(), text='=', width=btnNegWidth,
                        height=btnNegheight1, bg='#ffad80', fg='black', relief='flat', font=fontSize)
      btnEqual.pack(side=LEFT, expand=True, fill='both', padx=1, pady=1)
      # =========================================1 to 3 + ============================================
      functions.creatButton(3, self.top6div, [1, 2, 3])
      btnPlus = ButtonStyle1(self.top6div, command=lambda x="+": functions.addOperatorToCurrentLabel(x), text='+',
                             width=btnNegWidth, height=btnNegheight1, bg=btnBg, fg=btnNumberBg, relief='flat',
                             font=fontSize)
      btnPlus.pack(side=LEFT, expand=True, fill='both', padx=1, pady=1)
      # =========================================4 to 6 - ============================================
      functions.creatButton(3, self.top5div, [4, 5, 6, ])
      btnMinus = ButtonStyle1(self.top5div, command=lambda x="-": functions.addOperatorToCurrentLabel(x), text='-',
                              width=btnNegWidth, height=btnNegheight1, bg=btnBg, fg=btnNumberBg, relief='flat',
                              font=fontSize)
      btnMinus.pack(side=LEFT, expand=True, fill='both', padx=1, pady=1)
      # =========================================7 to 9 X ============================================
      functions.creatButton(3, self.top4div, [7, 8, 9])
      btnMultiply = ButtonStyle1(self.top4div, command=lambda x="*": functions.addOperatorToCurrentLabel(x), text='x',
                                 width=btnNegWidth, height=btnNegheight1, bg=btnBg, fg=btnNumberBg, relief='flat',
                                 font=fontSize)
      btnMultiply.pack(side=LEFT, expand=True, fill='both', padx=1, pady=1)
      # =========================================other btns  ============================================
      btnReverse = ButtonStyle1(self.top3div, command=lambda: functions.reverse(), text='1/x', width=btnNegWidth,
                                height=btnNegheight1, bg=btnBg, fg=btnNumberBg, relief='flat', font=fontSize)
      btnReverse.pack(side=LEFT, expand=True, fill='both', padx=1, pady=1)

      btnPower = ButtonStyle1(self.top3div, command=lambda: functions.square(), text='x\u00b2', width=btnNegWidth,
                              height=btnNegheight1, bg=btnBg, fg=btnNumberBg, relief='flat', font=fontSize)
      btnPower.pack(side=LEFT, expand=True, fill='both', padx=1, pady=1)

      btnRadical = ButtonStyle1(self.top3div, command=lambda: functions.sqrt(), text='\u221ax', width=btnNegWidth,
                                height=btnNegheight1, bg=btnBg, fg=btnNumberBg, relief='flat', font=fontSize)
      btnRadical.pack(side=LEFT, expand=True, fill='both', padx=1, pady=1)

      btnDevid = ButtonStyle1(self.top3div, command=lambda x="/": functions.addOperatorToCurrentLabel(x), text='÷',
                              width=btnNegWidth, height=btnNegheight1, bg=btnBg, fg=btnNumberBg, relief='flat',
                              font=fontSize)
      btnDevid.pack(side=LEFT, expand=True, fill='both', padx=1, pady=1)
      # =========================================first row btns ============================================
      btnReminder = ButtonStyle1(self.top2div, command=lambda x="%": functions.addOperatorToCurrentLabel(x), text='%',
                                 width=btnNegWidth, height=btnNegheight1, bg=btnBg, fg=btnNumberBg, relief='flat',
                                 font=fontSize)
      btnReminder.pack(side=LEFT, expand=True, fill='both', padx=1, pady=1)

      btnClearEntry = ButtonStyle1(self.top2div, command=lambda: functions.clearEntry(), text='CE', width=btnNegWidth,
                                   height=btnNegheight1, bg=btnBg, fg=btnNumberBg, relief='flat', font=fontSize)
      btnClearEntry.pack(side=LEFT, expand=True, fill='both', padx=1, pady=1)

      btnClearAll = ButtonStyle1(self.top2div, command=lambda: functions.clear(), text='C', width=btnNegWidth,
                                 height=btnNegheight1, bg=btnBg, fg=btnNumberBg, relief='flat', font=fontSize)
      btnClearAll.pack(side=LEFT, expand=True, fill='both', padx=1, pady=1)

      btnClear = ButtonStyle1(self.top2div, command=lambda: functions.backSpace(), text='⌫', width=btnNegWidth,
                              height=btnNegheight1, bg=btnBg, fg=btnNumberBg, relief='flat', font=fontSize)
      btnClear.pack(side=LEFT, expand=True, fill='both', padx=1, pady=1)
   # ===================================smallLayout===============================
   def smallLayout(self):
      self.top7div.pack_forget()
      self.top6div.pack_forget()
      self.top5div.pack_forget()
      self.top4div.pack_forget()
      self.top3div.pack_forget()
      self.top2div.pack_forget()
      self.top1div.pack_forget()
      self.frame.pack_forget()
      self.frame = Frame(root, width=0, height=20, bg=color)
      self.top1div = Frame(root,width=350,height=top1divHeight, bg=color)
      self.top2div = Frame(root,width=350,height=top2divHeight/6,bg=color)
      self.top3div = Frame(root,width=350,height=top2divHeight/6,bg=color)
      self.top4div = Frame(root,width=350,height=top2divHeight/6,bg=color)
      self.top5div = Frame(root,width=350,height=top2divHeight/6,bg=color)
      self.top6div = Frame(root,width=350,height=top2divHeight/6,bg=color)
      self.top7div = Frame(root,width=350,height=top2divHeight/6,bg=color)
      self.frame.pack(side=RIGHT, expand=expandStatus, fill=fillStutus)
      self.top1div.pack(side=TOP, expand=expandStatus, fill=fillStutus, pady=45)
      self.top2div.pack(side=TOP, expand=expandStatus, fill=fillStutus)
      self.top3div.pack(side=TOP, expand=expandStatus, fill=fillStutus)
      self.top4div.pack(side=TOP, expand=expandStatus, fill=fillStutus)
      self.top5div.pack(side=TOP, expand=expandStatus, fill=fillStutus)
      self.top6div.pack(side=TOP, expand=expandStatus, fill=fillStutus)
      self.top7div.pack(side=TOP, expand=expandStatus, fill=fillStutus)
      self.sharedPartsOfTheLayouts()
       #===================================BigLayout===============================
   def BigLayout(self):
      self.frame.pack_forget()
      self.top7div.pack_forget()
      self.top6div.pack_forget()
      self.top5div.pack_forget()
      self.top4div.pack_forget()
      self.top3div.pack_forget()
      self.top2div.pack_forget()
      self.top1div.pack_forget()
      self.frame = Frame(root, width=320, height=20, bg="brown")
      self.top1div = Frame(root, width=350, height=200, bg=color)
      self.top2div = Frame(root, width=350, height=top2divHeight / 6, bg=color)
      self.top3div = Frame(root, width=350, height=top2divHeight / 6, bg=color)
      self.top4div = Frame(root, width=350, height=top2divHeight / 6, bg=color)
      self.top5div = Frame(root, width=350, height=top2divHeight / 6, bg=color)
      self.top6div = Frame(root, width=350, height=top2divHeight / 6, bg=color)
      self.top7div = Frame(root, width=350, height=top2divHeight / 6, bg=color)
      self.frame.pack(side=RIGHT, expand=expandStatus, fill=fillStutus)
      self.top1div.pack(side=TOP, expand=expandStatus, fill=fillStutus, pady=45)
      self.top2div.pack(side=TOP, expand=expandStatus, fill=fillStutus)
      self.top3div.pack(side=TOP, expand=expandStatus, fill=fillStutus)
      self.top4div.pack(side=TOP, expand=expandStatus, fill=fillStutus)
      self.top5div.pack(side=TOP, expand=expandStatus, fill=fillStutus)
      self.top6div.pack(side=TOP, expand=expandStatus, fill=fillStutus)
      self.top7div.pack(side=TOP, expand=expandStatus, fill=fillStutus)
      self.sharedPartsOfTheLayouts()
 #====================================history section===========================
      self.myCanvas = Canvas(self.frame, bg=color,highlightthickness=0)
      self.myCanvas.pack(side=LEFT, fill=Y)
      self.sb = Scrollbar(self.frame, orient=VERTICAL, command=self.myCanvas.yview)
      self.sb.pack(side=RIGHT, fill=Y)
      self.myCanvas.configure(yscrollcommand=self.sb.set)
      self.myCanvas.bind('<Configure>', lambda e: self.myCanvas.configure(scrollregion=self.myCanvas.bbox("all")))
      self.myCanvasFrame = Frame(self.myCanvas, bg=color)
      self.myCanvas.create_window((0, 0), window=self.myCanvasFrame, anchor=NW)



      Button(self.myCanvasFrame, text='History', width=btnNegWidth,
                              height=btnNegheight1, bg=color,activebackground=color,activeforeground=btnNumberBg, fg=btnNumberBg, relief='flat', font=fontSize
                          ).grid(row=0, column=0, sticky=W, pady=2)
      self.HistoryLabel = Label(self.myCanvasFrame, text='There is no history yet',
             height=btnNegheight1, bg=color, activebackground=color, activeforeground=btnNumberBg, fg=btnNumberBg,
             relief='flat', font=("Arial", 11)
             )
      self.HistoryLabel.grid(row=1, column=0, pady=2,columnspan=2,sticky=W)

      sep = ttk.Separator(self.myCanvasFrame,orient='horizontal')
      sep.place(x = 2,y = 45, height = 1, width = 80)


#==========================instance of class functions===============
functions = functions()
functions.keyboardBind()
#==================================set layout size when changing size========================================
class size:
   def __init__(self):
      self.sizeDic = {350:functions.smallLayout , 750:functions.BigLayout }
      self.currentSize = None
      self.checkedSize = None
      root.bind('<Configure>', lambda event :self.checkSize(event) )
      root.update()
   def checkSize(self,event):
      if event.widget == root:
         for key in self.sizeDic :
            delta = event.width - key
            if delta >= 0:
               self.checkedSize = key
         if self.checkedSize !=self.currentSize :
            self.currentSize = self.checkedSize
            self.sizeDic[self.currentSize]()
#===============================================try========================================
size = size()
root.protocol("WM_DELETE_WINDOW", functions.quit)
root.mainloop()
root.destroy()

# self.frame.grid_propagate(False)
# self.frame.pack_propagate(True)
