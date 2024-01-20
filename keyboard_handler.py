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

# Define Input_I union for various input types
class Input_I(ctypes.Union):
    _fields_ = [("ki", KeyboardEvent),
                 ("mi", MouseEvent),
                 ("hi", HardwareEvent)]

# Define Input structure to hold input information
class Input(ctypes.Structure):
    _fields_ = [("type", ctypes.c_ulong),
                ("ii", Input_I)]

# Define press_key function
def press_key(key_code):
    """
    Simulate pressing a keyboard key.

    :param key_code: The virtual key code of the key to be pressed.
    """
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyboardEvent(0, key_code, 0x0008, 0, ctypes.pointer(extra))
    x = Input(ctypes.c_ulong(1), ii_)
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

# Define release_key function
def release_key(key_code):
    """
    Simulate releasing a keyboard key.

    :param key_code: The virtual key code of the key to be released.
    """
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyboardEvent(0, key_code, 0x0008 | 0x0002, 0, ctypes.pointer(extra))
    x = Input(ctypes.c_ulong(1), ii_)
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

# Test key press and release
if __name__ == '__main__':
    press_key(KEY_W)
    time.sleep(1)
    release_key(KEY_W)
    time.sleep(1)