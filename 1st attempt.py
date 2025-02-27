from moviepy.video.io.VideoFileClip import VideoFileClip
import re

allperiods = []
firstNum = []
transarry = []
timeArry = []

def extract_clip(start,end,file):
    with VideoFileClip("1.mp4") as video:
        new = video.subclip(start,end)#87
        new.write_videofile('F:\\VidoeClips\\'+file)

def  Get_info_From_Srt_File():
    with open("Argo.2012.720p.BluRay.x264.YIFY.srt", encoding="utf-8") as f:
        all_lines = f.readlines()

    for line in all_lines:
        translation = re.search(r'^(<font color="#ffff80">)(.*)(</font>)$', line)
        period = re.findall(r'\d\d:\d\d:\d\d,\d*',line)
        # firstNumInTheLine = re.findall(r'^\d*$',line)

        # if firstNumInTheLine != [] and firstNumInTheLine != ['']:
            # firstNum.append(f'{firstNumInTheLine[0]}\n')

        if period != []:
            allperiods.append(period)
            timeArry.append(f"{period[0]} -----> {period[1]}\n")
        if translation != None:
            transarry.append(f'{translation.group(2)}\n')

def Write_Text_Files():
    add_to_text_file = 0
    for i in range(0, len(transarry)):
        add_to_text_file += 1
        with open(f'F:\\textFiles\\text{add_to_text_file}.txt', 'w+', encoding='utf_8') as txtfile:
            txtfile.writelines(f"{timeArry[i]}{transarry[i]}\n")

def Video_Cutter():
    add = 0
    for period in allperiods:
        E_S_time = []
        for time in period:
            seconds = float(time[0:2]) * 3600 + float(time[3:5]) * 60 + float(time[6:8]) + float(f'0.{time[9:12]}')
            E_S_time.append(seconds)
        print(E_S_time)
        add += 1
        extract_clip(E_S_time[0], E_S_time[1], f'Outout{str(add)}.mp4')

Get_info_From_Srt_File()
Write_Text_Files()
Video_Cutter()

