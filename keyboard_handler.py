import ctypes
import time

# Define key constants
KEY_W = 0x11
KEY_A = 0x1E
KEY_S = 0x1F
KEY_D = 0x20
KEY_SPACE = 0x39

PTR_UL = ctypes.POINTER(ctypes.c_ulong)

# Structuring to represent a Keyboard Event
class KeyboardEvent(ctypes.Structure):
    _fields_ = [
        ("virtual_key", ctypes.c_ushort),
        ("scan_code", ctypes.c_ushort),
        ("flags", ctypes.c_ulong),
        ("timestamp", ctypes.c_ulong),
        ("extra_info", PTR_UL)
    ]

# Define HardwareEvent structure for hardware input
class HardwareEvent(ctypes.Structure):
    _fields_ = [
        ("message", ctypes.c_ulong),
        ("param_low", ctypes.c_short),
        ("param_high", ctypes.c_ushort)
    ]

# Define MouseEvent structure for mouse input
class MouseEvent(ctypes.Structure):
    _fields_ = [
        ("x_movement", ctypes.c_long),
        ("y_movement", ctypes.c_long),
        ("mouse_data", ctypes.c_ulong),
        ("flags", ctypes.c_ulong),
        ("timestamp", ctypes.c_ulong),
        ("extra_info", PTR_UL)
    ]