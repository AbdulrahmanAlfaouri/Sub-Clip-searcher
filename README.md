# Sub-Clip-searcher
a program that gets the clip of a movie that matches a searten searched word in the subtitles 

-the idea is for each sentance we have to extract its 'start' and 'finish' time from the subtitles file and save this sentance in its own .txt file like '1.txt' then '2.txt' and so on
-then we cut the movie into small .mp4 file that correspondance with each 'start' and 'finish' times for the .txt files we made 
-then when we input a sentance we want to search the program fist searches all the subtitles then gets the 'start' and 'end' time for that sentance then it extract the clip from the movie from the 'start' to the 'end' times' which in correspondance will have the sentance we inputed

1-the 1st attempt
  1--'Get_info_From_Srt_File' gets the spacific (H:M:S) for each sentence from the subtitles file) then 
  2--'Write_Text_Files' cuts the subtitles file into many txt files each file contains 1 sentence and ie (1st sentance ->         1.txt, 2nd sentance -> 2.txt, . . . and so on) 
  3--then the 'Video_Cutter' function cuts the movie into many .mp4 video files and names then in correspondance to each       sentance in the subtitles ie( 1st sentance -> 1.txt -> 1.mp4, 2nd sentance -> 2.txt -> 2.mp4 . . , and so on)

2-the 2nd attempt
  same as the 1st attempt but uses pysrt which make it easer to work with the subtitles file

-the 'main' script file
  here we get the .txt files we extracted then compare the sentance we inputed to search it the sentances in each of the .txt file and get the .mp4 clip from the movie that corrisponde to that sentance

