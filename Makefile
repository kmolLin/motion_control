# Executable packing script using PyInstaller on Windows.

all: build

build: launch.py
	pyinstaller -F $< -i icons/motor.ico -n "Motion Control Simulator" \
--hidden-import=PyQt5.QtPrintSupport

clean:
	-rd build /s /q
	-rd dist /s /q
	-del *.spec
