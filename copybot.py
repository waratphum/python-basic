#copybot.py
import pyautogui as pg
import time
def CopyText(nextline=0):
    
    ########### LINE 1 #####################
    #-ใช้เมาส์คลิกไปยังตำแหน่งที่ต้องการก็อปปี้ (ด้านหน้า)
    # x=424, y=741
    time.sleep(1)#รอ 1 วินาที
    start_point= (418,741+nextline)
    pg.click(start_point)

    #-ลากไปให้สุดบรรทัด
    time.sleep(1)
    end_point=(518,741+nextline)
    pg.dragTo(end_point,duration=2)

    #-กดปุ่ม Ctrl+c เพื่อก็อปปี้
    pg.hotkey('ctrl','C')

    #-ขยับเมาส์ไปทางด้านซ้าย
    left_notepad=(99,741+nextline)
    pg.click(left_notepad)
    #-กดCtrl+v เพื่อวางแล้วกด Enter
    pg.hotkey('ctrl','v')
    pg.press('enter')
for i in range(10):
    CopyText(18*i)

