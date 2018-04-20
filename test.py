# import pydub
# sound = pydub.AudioSegment.from_mp3("Recording/180128-222450.mp3")
# sound.export("Recording/180128-222450.wav", format="wav")

# import win32api                                                               
# # win32api.ShellExecute(0, 'open', 'notepad.exe', '', '', 0)           # 后台执行  
# # win32api.ShellExecute(0, 'open', 'notepad.exe', '', '', 1)           # 前台打开  
# # win32api.ShellExecute(0, 'open', 'notepad.exe', '1.txt', '', 1)      # 打开文件  
# win32api.ShellExecute(0, 'open', 'http://www.sohu.com', '', '', 1)   # 打开网页  
# # win32api.ShellExecute(0, 'open', 'D:\\Opera.mp3', '', '', 1)         # 播放视频  
# # win32api.ShellExecute(0, 'open', 'D:\\hello.py', '', '', 1)          # 运行程序  

import myChat

myChat.main()