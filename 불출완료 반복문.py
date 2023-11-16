import pyautogui
import time


while True:
    repeat_count = int(input("반복할 횟수를 입력하세요 (0 입력 시 종료): "))

    if repeat_count == 0:
        break  # Exit the loop if the user enters 0

    for _ in range(repeat_count):
        # 순번 1 클릭
        pyautogui.click(61, 394)

        # python 입력 창으로 복귀
        pyautogui.hotkey('alt', 'tab')

        # 불출수량 입력받기
        불출수량 = input("불출수량 = ")

        # 다시 ERP 입력창으로 이동
        pyautogui.hotkey('alt', 'tab')

        # 불출수량 Entry 클릭
        pyautogui.click(1738, 781)

        # 불출수량 입력
        pyautogui.typewrite(불출수량)

        # 입력 후 1초 대기
        time.sleep(0.5)

        # 불출버튼 클릭
        pyautogui.click(66, 706)
        time.sleep(0.5)

        # 불출 확인/취소 [확인]
        pyautogui.click(1064, 158)
        time.sleep(0.5)

        # 불출 마무리
        pyautogui.click(1136, 157)
