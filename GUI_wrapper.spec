# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['GUI_wrapper.py'],
             pathex=['/home/kamian/MIPS_Autograder'],
             binaries=[],
             datas=[ ('Frontend/resources/*', '.'),
                    ('Frontend/resources/Icons', 'Icons'),
                    ('Frontend/resources/temp', 'temp'),
                    ('Frontend/grader_data/*', 'grader_data/.'),
                    ('Autograder/*', 'Autograder/.'),
                    ('Autograder/template/*' ,'Autograder/template/.' )],
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
          name='GUI_wrapper',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True )
