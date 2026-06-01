# -*- mode: python ; coding: utf-8 -*-

import sys
from pathlib import Path

block_cipher = None

# 收集 PyQt5 的所有数据（确保 platform plugin 被包含）
pyqt5_dir = None
try:
    import PyQt5
    pyqt5_dir = Path(PyQt5.__file__).parent
except ImportError:
    pass

a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('assets/icon.ico', 'assets'),
    ],
    hiddenimports=[
        'win32gui', 'win32con', 'win32process', 'win32api',
        'keyboard',
        'PyQt5',
        'PyQt5.sip',
        'PyQt5.QtWidgets',
        'PyQt5.QtGui',
        'PyQt5.QtCore',
    ],
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

# 如果 PyQt5 已安装，确保 platform plugin 被包含
if pyqt5_dir:
    plugins_src = pyqt5_dir / 'Qt5' / 'plugins' / 'platforms'
    if plugins_src.exists():
        a.datas += [(
            str(p.relative_to(pyqt5_dir.parent.parent)),
            str(p)
        ) for p in plugins_src.glob('*')]
        print(f"[INFO] 已添加 Qt platform 插件: {plugins_src}")

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='BossKey',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=False,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='assets/icon.ico',
    uac_admin=True,
)
