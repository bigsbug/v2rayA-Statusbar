from setuptools import setup

APP = ["main.py"]
DATA_FILES = []
OPTIONS = {
    "argv_emulation": False, 
    "packages": ["rumps"],
    "plist": {
        "LSUIElement": True,
        'CFBundleName': 'V2rayA',
        'CFBundleDisplayName': 'V2rayA',
        'CFBundleIdentifier': 'bigsbug.v2raya',
        'CFBundleVersion': '1.0.0',
    },

}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={"py2app": OPTIONS},
    setup_requires=["py2app"],
)
