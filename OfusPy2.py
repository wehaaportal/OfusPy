#!/usr/bin/python3
# -*- coding: utf-8 -*-

''' Load '''
from __future__ import unicode_literals
import os, sys, zlib, base64

from tkinter import filedialog
from tkinter import *

OfusPy = '''#!/usr/bin/env python3
# -*- coding: utf-8 -*-
################################################################################
#
#   OfusPy 2.0.1 - Ofuscador Python
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
        if pi_file.endswith('.py'):
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

class OfusAppGUI(Frame):
	font20 = 'Calibri 20'
	bfont20 = font20 + ' bold'
	file = subfolder = False
	folder = ''		

	def __init__(self, master=None):
		super().__init__(master)
		self.master = master
		master.title(u'OfusPy v2.0.1')
		master.resizable(False,False)
		self.CreateWidget()

	def Obfuscate(self):
		self.btnFile['state'] = 'disabled'
		self.btnOfus['text'] = 'Ofuscando espere..'
		self.btnOfus['state'] = 'disabled' 

		if self.file:
			try:
				head, tail = os.path.split(self.file)
				compilePiDir(dir = head, file = tail)
			except Exception as e:
				print('Error 0x000001') #TODO: Error ofuscar
			finally:
				self.btnOfus['state'] = 'normal'
				self.btnOfus['text'] = 'Ofuscar'
				self.btnOfus['state'] = 'disabled'
				self.file = False
				self.folder = ''
				self.btnFile['state'] = 'normal'
				self.txtFile['state'] = 'normal'
				self.txtFile.delete(0, END)
				self.txtFile['state'] = 'disabled'
				pass
		pass

	def CreateWidget(self):
		try:			
			''' Title '''
			self.title = Label(self.master)
			self.title['text'] = "Ofuscador Python 2.0.1"
			self.title['font'] = self.font20
			self.title.grid(padx=7, pady=5, row=0, column=1, columnspan=2, sticky=N)

			''' Button & Entry | File '''
			self.btnFile = Button(self.master)
			self.btnFile['text'] = "Archivo"
			self.btnFile['width'] = 20
			self.btnFile['command'] = self.OpenFile
			self.btnFile.grid(padx=7, pady=5, row=1, column=1)
			self.txtFile = Entry(self.master, state='disabled')
			self.txtFile['width'] = 60
			self.txtFile.grid(padx=7, pady=5, row=1, column=2)

			''' Button & Entry | Folder '''
			#TODO: implement widget

			''' Button Ofuscar '''
			self.btnOfus = Button(self.master, fg="white", bg="black")
			self.btnOfus['text'] = "Ofuscar"
			self.btnOfus['width'] = 50
			self.btnOfus['command'] = self.Obfuscate
			self.btnOfus.grid(padx=7, pady=5, row=4, column=2)
			self.btnOfus['state'] = 'disabled'

			''' Button Quit '''
			self.btnQuit = Button(self.master, text="Salir", width=20, fg="white", bg="red",
                              command=self.master.destroy)
			self.btnQuit.grid(padx=7, pady=5, row=4, column=1)			
		except Exception as e:
			print('Error 0x000002') #TODO: Error Tkinter Widget
		pass

	def OpenFile(self):	
		try:
			self.file=filedialog.askopenfilename(initialdir = ".",
				title = "Abrir",filetypes = (("Python files","*.py"),("all files","*.*")))
			self.txtFile['state'] = 'normal'
			self.txtFile.delete(0, END)
			if self.file:
				self.txtFile.insert(0, self.file)
				self.btnOfus['state'] = 'normal'		
			self.txtFile['state'] = 'disabled'
			pass
		except Exception as e:
			print('Error 0x000003') #TODO: Error Open file		
		pass
	
''' Init OfusApp '''	
if __name__ == '__main__':	    
    app = Tk()
    ofus = OfusAppGUI(app)
    app.mainloop()