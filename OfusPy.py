#!/usr/bin/python3
# -*- coding: utf-8 -*-

''' Load '''
from __future__ import unicode_literals
import os, sys, zlib, base64, json, time, random, logging
from locale import getdefaultlocale

from tkinter import *
from tkinter import messagebox, filedialog, ttk

name = 'logs/ofuspy_{}_{}.log'.format(time.strftime('%Y-%m-%d', time.localtime()), random.randrange(9999))

_v = ' 2.0.5b6'

OfusPy = '''#!/usr/bin/env python3
# -*- coding: utf-8 -*-
################################################################################
#
#   OfusPy 2.0.5b6 - Ofuscador Python
#   Pacheco, Matias W. <mwpacheco@outlook.es>
#   Copyright (c) 2021 Wehaa Portal Soft.
#   License MIT
#
#   WARNING! Do 'NOT' change. You may experience problems with the file.!
#
################################################################################

import zlib, base64
exec(zlib.decompress(base64.b64decode('%s')))
'''

def compilePiDir(dir, file=False, map=None, **compilePi_args):
    def compile_pi(pi_dir, pi_file):
        if pi_file.endswith('.py') or pi_file.endswith('.pyw'):
            py_dir = pi_dir
            py_file = 'compressed_'+ pi_file[:-3] + '.py'

            if map is not None:
                py_dir, py_file = map(py_dir, py_file)

            try:
                os.makedirs(py_dir)
            except:
                pass

            pi_path = os.path.join(pi_dir, pi_file)
            py_path = os.path.join(py_dir, py_file)

            pi_file = open(pi_path, 'rb')
            py_file = open(py_path, 'w')

            try:
                compilePi(pi_file, py_file, **compilePi_args)
            finally:
                pi_file.close()
                py_file.close()

    if file:
        if os.path.isfile(os.path.join(dir, file)):
            compile_pi(dir, file)

def compilePi(pifile, pyfile):
    try:
        pifname = pifile.name
    except AttributeError:
        pifname = pifile

    original_data = pifile.read()    
    compressed_data = zlib.compress(original_data, zlib.Z_BEST_COMPRESSION)
    gzipped_data = base64.b64encode(compressed_data).decode()

    pyfile.write(OfusPy % (gzipped_data))

class OfusPySplash(Toplevel):
	def __init__(self, parent):
		Toplevel.__init__(self, parent)

		self.title("OfusPySplash 0.0.5")

		#Center Windows
		w = 390
		h = 160
		x = self.winfo_screenwidth() // 2 - w // 2
		y = self.winfo_screenheight() // 2 - h // 2
		self.geometry(str(w) + "x" + str(h) + "+" + str(x) + "+" + str(y))
		#Canvas
		image_file = "assets/ofusplash.png"
		image = PhotoImage(file=image_file)
		canvas = Canvas(self, height=h, width=w, bg="#000")
		canvas.create_image(0, 0, image=image,anchor='nw')
		canvas.pack(fill="both", expand=True)

		self.overrideredirect(1) #Hide Title Bar 
		self.update()
		pass

class OfusAppGUI(Frame):
	TR = {}
	loadfile=[]
	ok = False
	def __init__(self, master=None):
		super().__init__(master)
		self.master = master

		master.withdraw() #Hide App
		splash = OfusPySplash(self)
		time.sleep(6)
		splash.destroy()

		#Language
		self.language, self.encoding = getdefaultlocale()
		self.OfusLang()	

		#OfusApp
		master.title(self.TR['trName'] + _v)
		master.resizable(False,False)
		master.geometry('720x250')
		master.iconbitmap('assets/ofuspy.ico')

		self.CreateWidget()

		master.deiconify() #Show App
		pass

	def Obfuscate(self):
		try:
			#print(self.loadfile)	
			if self.loadfile:				
				for file in self.loadfile:
					head, tail = os.path.split(file)										
					compilePiDir(dir = head, file = tail)
					self.ok = True
					time.sleep(2)
			pass
		except Exception as e:
			print(e)
			logging.error(" Error Obfuscate ")			
			messagebox.showerror('ERROR', '0x000003') #TODO: Error Obfuscate
		finally:
			self.loadfile = []
			self.btnOfus['state'] = 'disabled'			
			self.boxFile.delete('1.0', END)
			if self.ok:
				messagebox.showinfo(message=self.TR['trOfusBody'], title=self.TR['trName'])
			pass
		self.ok = False 

	def OpenFile(self):
		try:
			self.file=filedialog.askopenfilenames(initialdir = ".",
				title =self.TR['trSeleFile'], filetypes = (("Python files","*.py;*.pyw"),("all files","*.*")))

			for files in self.file: 
				self.boxFile.insert('1.0', files + '\n')
				self.loadfile.append(files)

			if self.boxFile:
				self.btnOfus['state'] = 'normal'
		except Exception as e:
			print(e)
			logging.error(" Does 'NOT' open the file ")
			messagebox.showerror('ERROR', '0x000002') #TODO: Does 'NOT' open the file	
		pass

	''' Widget Tkinter '''
	def CreateWidget(self):
		try:
			''' Logo & Title '''
			self.title = Label(self.master, font=('', 15, 'bold'))
			self.title['text'] = self.TR['trTitle'] + ' ' + _v
			self.title.grid(padx=7, pady=25, row=0, column=1, columnspan=2, sticky=N)

			''' Button & Text | File '''			
			self.boxFile = Text(self.master, width=66, height=5)
			self.boxFile.grid(padx=9, pady=5, row=1, column=1)
			
			self.btnFile = Button(self.master, command=self.OpenFile, width=20, height=5, bg='#856ff8')
			self.btnFile['text'] = self.TR['trBtnFile']
			self.btnFile.grid(row=1, column=2, pady=5, padx=5)

			self.Line = Label(self.master, fg='white', font=('', 5, ''))
			self.Line['text'] = '-'*250
			self.Line.grid(padx=7, pady=5, row=3, column=1, columnspan=2, sticky=N)

			self.btnExit = Button(self.master, command=self.OfusExit, width=20, fg="white", bg="red")
			self.btnExit['text'] = self.TR['trBtnExit']
			self.btnExit.grid(row=4, column=2, padx=5, pady=5)

			''' Button Ofuscar '''
			self.btnOfus = Button(self.master, fg="white", bg="#6C3483",  width=75, command=self.Obfuscate)
			self.btnOfus['text'] = self.TR['trBtnOfus']			
			self.btnOfus.grid(padx=7, pady=5, row=4, column=1)
			self.btnOfus['state'] = 'disabled'
		except Exception as e:
			print(e)
			logging.error(" Error Tkinter Widget ")
			messagebox.showerror('ERROR', '0x000001') #TODO: Error Tkinter Widget

	def OfusExit(self):
		MsgBox = messagebox.askquestion(self.TR['trExitTitle'], self.TR['trExitBody'])
		if MsgBox == 'yes':
			self.master.destroy() # Closing the GUI window			

	''' Language '''
	def OfusLang(self):
		self.language = self.language if os.path.isfile('local/'+self.language+'.po')  else 'en_EN'
		try:
			if os.path.isfile('local/'+self.language+'.po'):
				with open('local/'+self.language+'.po') as json_file:
					data = json.load(json_file)				
					for p in data[self.language]:
						for key, value in p.items():
							self.TR[key] = value			
		except Exception as e:
			print(e)
			logging.error(" Does 'NOT' load the language ")
			messagebox.showerror('ERROR', '0x000000') #TODO: Does 'NOT' load the language
		pass

if __name__ == "__main__":
	''' OfusLogs '''
	logging.basicConfig(filename=name, encoding='utf-8', level=logging.DEBUG)
	logging = logging.getLogger('OfusPy')

	app = Tk()
	ofus = OfusAppGUI(app)
	app.mainloop()