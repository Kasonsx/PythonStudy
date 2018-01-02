import win32api,win32con,win32gui
import time
# print(win32api.GetCursorPos())#获取鼠标当前位置
def left_click(x, y, no_stop=False, times=1, sleeptime=0.3):
	win32api.SetCursorPos((x, y))#设置鼠标位置
	while no_stop|times:
		win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)#鼠标左键按下
		win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)#鼠标左键松开
		time.sleep(sleeptime)
		times -= 1 


if __name__ == '__main__':
	x, y = win32api.GetCursorPos()
	left_click(x, y, False, 20)
	# win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
	# win32api.SetCursorPos((x+150,y+150))
	# win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)

