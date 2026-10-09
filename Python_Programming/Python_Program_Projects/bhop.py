import pymem
import pymem.process
import win32api
import time

# Offsets
LOCAL_PLAYER = 0xD8C2CC  # Example offset, update with the correct one
FORCE_JUMP = 0x51ED760  # Example offset, update with the correct one
HEALTH = 0x100  # Example offset, update with the correct one
FLAGS = 0x104  # Example offset, update with the correct one

def bhop() -> None:
    pm = pymem.Pymem('csgo.exe')

    # Get client module address
    client = pymem.process.module_from_name(pm.process_handle, 'client.dll').lpBaseOfDll

    # Hack loop
    while True:
        time.sleep(0.01)

        # Check if space bar is pressed
        if not win32api.GetAsyncKeyState(0x20):
            continue

        local_player = pm.read_uint(client + LOCAL_PLAYER)

        if not local_player:
            continue

        # Check if player is alive
        if pm.read_int(local_player + HEALTH) <= 0:
            continue

        # Check if player is on the ground
        if pm.read_uint(local_player + FLAGS) & 1:
            pm.write_uint(client + FORCE_JUMP, 6)
            time.sleep(0.01)
            pm.write_uint(client + FORCE_JUMP, 4)

if __name__ == '__main__':
    bhop()
