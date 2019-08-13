# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['main.py'],
             pathex=['/home/nemmtor/python_scripts/gdw'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)

for d in a.datas:
    if 'pyconfig' in d[0]:
        a.datas.remove(d)
        break

a.datas += [('ikona.gif',r'./pliki/ikona.gif', 'Data'),
            ('goldwin.png',r'./pliki/goldwin.png', 'Data'),
            ('rodo.txt',r'./pliki/rodo.txt', 'Data'),
            ('tresc.txt',r'./pliki/oferta/tresc.txt', 'Data'),
            ('129.pdf',r'./pliki/oferta/129.pdf', 'Data'),
            ('159.pdf',r'./pliki/oferta/159.pdf', 'Data'),
            ('199.pdf',r'./pliki/oferta/199.pdf', 'Data'),
            ('Goldwin.pdf',r'./pliki/oferta/Goldwin.pdf', 'Data'),
            ('ikona.ico',r'./ikona.ico', 'Data')]


pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='Goldwin',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False,
	      icon='ikona.ico',
		  version='version.txt')
