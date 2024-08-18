import sys
import time
import argparse
from pynput.mouse import Button, Controller as MouseController
from pynput.keyboard import Controller as KeyboardController, Key

def click_mouse_fixed(clicks_per_second, duration, position):
    mouse = MouseController()
    mouse.position = position

    end_time = time.time() + duration
    while time.time() < end_time:
        mouse.position = position
        mouse.click(Button.left)
        print(f'Clicked at fixed position: {position}', end='\r')
        time.sleep(1 / clicks_per_second)

def click_mouse_freely(clicks_per_second, duration):
    mouse = MouseController()
    end_time = time.time() + duration
    while time.time() < end_time:
        position = mouse.position
        mouse.click(Button.left)
        print(f'Clicked at position: {position}', end='\r')
        time.sleep(1 / clicks_per_second)

def press_key(key, presses_per_second, duration):
    keyboard = KeyboardController()
    end_time = time.time() + duration
    while time.time() < end_time:
        keyboard.press(key)
        keyboard.release(key)
        print(f'Pressed {key} key', end='\r')
        time.sleep(1 / presses_per_second)

def get_mouse_position():
    mouse = MouseController()
    return mouse.position

def monitor_mouse_position():
    mouse = MouseController()
    try:
        while True:
            position = mouse.position
            print(f'Current mouse position: {position}', end='\r')
            time.sleep(0.5)
    except KeyboardInterrupt:
        position = mouse.position
        print(f"\nMonitoring stopped. Last mouse position: {position}")

def main():
    parser = argparse.ArgumentParser(description='Mouse Clicker and Key Press Simulator')
    parser.add_argument('action', choices=['mouse', 'keyboard'], help='Choose action: mouse or keyboard')
    parser.add_argument('presses_per_second', type=int, help='Number of actions per second')
    parser.add_argument('duration', type=int, help='Duration in seconds')
    parser.add_argument('key', type=str, nargs='?', default='k', help='Key to press (default: k)')

    args = parser.parse_args()

    if args.action == 'mouse':
        if len(args.key) == 2:  # 如果提供了位置参数
            position = (float(args.key[0]), float(args.key[1]))
            click_mouse_fixed(args.presses_per_second, args.duration, position)
        else:
            click_mouse_freely(args.presses_per_second, args.duration)
    elif args.action == 'keyboard':
        key = args.key
        # 处理特殊键
        if key in ['enter', 'space', 'tab', 'backspace', 'esc']:
            key = getattr(Key, key)
        press_key(key, args.presses_per_second, args.duration)

if __name__ == '__main__':
    main()
