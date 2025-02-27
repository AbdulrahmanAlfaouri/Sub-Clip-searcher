from moviepy.video.io.VideoFileClip import VideoFileClip
import re, pysrt


def extract_clip(start,end,file):
    with VideoFileClip("1.mp4") as video:
        new = video.subclip(start,end)#87
        new.write_videofile(f'F:\\VidoeClips\\{file}')

addToTextFile = 1
add = 1
subs = pysrt.open('1.srt',encoding='latin-1')

for i in subs:
    #extract start and end time for each word in the subtitles 
    with open(f'F:\\textFiles\\text{addToTextFile}.txt','w',encoding="utf-8") as txtFile:
        txtFile.writelines(f'{i.start} ----> {i.end}\n{i.text}')
        addToTextFile += 1
    start = str(i.start)
    end = str(i.end)
    
    #convert start(H:M:S) and end(H:M:S) into seconds
    startingSecnods = i.start.seconds + (i.start.minutes *60) + (i.start.hours *360) + float(f'0.{start[9:12]}')
    endingSeconds = i.end.seconds + (i.end.minutes *60) + (i.end.hours *360) + float(f'0.{end[9:12]}')
    print(startingSecnods,endingSeconds)

    #extract and save clips from the movie based on the startingSecnods and endingSeconds
    try:
        extract_clip(startingSecnods,endingSeconds,f'Outout{add}.mp4')
    except ValueError:
        print(startingSecnods-endingSeconds,'---------------------------------')
    add += 1



