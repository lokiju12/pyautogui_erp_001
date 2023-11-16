from pynput.keyboard import Controller, Key
import pyautogui


def type_kor(text):
    keyboard = Controller()
    keyboard.press(Key.ctrl)
    keyboard.press('`')
    keyboard.release('`')
    keyboard.release(Key.ctrl)
    keyboard.type(text)


불출예정내용 = '전산 소모품 불출'  # input("불출예정내용 : ")

while True:
    repeat_count = int(input("반복할 횟수를 입력하세요 (0 입력 시 종료): "))

    if repeat_count == 0:
        break  # Exit the loop if the user enters 0

    for _ in range(repeat_count):
        # print('검색 Button')
        pyautogui.click(1800, 305)

        # print('순번 (1)')
        pyautogui.click(65, 370)

        # print('접수 Button')
        pyautogui.click(70, 305)

        # print('불출 예정 내용Entry')
        pyautogui.click(1100, 575)

        type_kor(불출예정내용)

        # print('확인 Button')
        pyautogui.click(1020, 620)

        # print('완료 Button 1')
        pyautogui.sleep(0.5)
        pyautogui.press('enter')

        # print('원점복귀')
        pyautogui.click(2400, 280)
