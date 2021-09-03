# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['MIPS_Autograder.py'],
             pathex=['/home/kamian/MIPS_Autograder'],
             binaries=[],
             datas=[ ('Frontend/resources/*', '.'),
                    ('Frontend/resources/Icons', 'Icons'),
                    ('Frontend/grader_data/*', 'grader_data/.'),
                    ('Autograder/*', 'Autograder/.'),
                    ('spim/*','spim/.'),
                    ('Autograder/template/*' ,'Autograder/template/.' ),
                    ('icon.ico','icon.ico')],
             hiddenimports=['PyQt5.sip'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='MIPS_Autograder',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False,
          icon='icon.ico' )
