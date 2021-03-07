import os, sys, zlib, base64, json, time

lang = {}

'''
#Spanish
tr = 'es_ES'
lang[tr] = []
lang[tr].append({
    'trName': 'OfusPy',
    'trTitle': 'Ofuscador Python',
    'trExitTitle': 'Salir de la aplicación',
    'trExitBody': '¿Estás seguro de que quieres salir?',
    'trOfusTitle': 'Información',
    'trOfusBody': 'Completo',

    'trSeleFile': 'Seleccionar archivos',    
    'trBtnFile': 'Examinar',
    'trBtnFolder': 'Carpeta',
    'trBtnExit': 'Salir',
    'trBtnOfus': 'Ofuscar'
})
'''
#English
tr = 'en_EN'
lang[tr] = []
lang[tr].append({
    'trName': 'OfusPy',
    'trTitle': 'Python Obfuscator',
    'trExitTitle': 'Exit Application',
    'trExitBody': 'Are you sure you want to exit?',
    'trOfusTitle': 'Information',
    'trOfusBody': 'full',

    'trSeleFile': 'Select files', 
    'trBtnFile': 'Browse',
    'trBtnFolder': 'Folder',
    'trBtnExit': 'Close',
    'trBtnOfus': 'Obfuscate'
})


with open('local/'+tr+'.po', 'w') as outfile:
    json.dump(lang, outfile)