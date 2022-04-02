# importing the module
from pytube import YouTube

# where to save
SAVE_PATH = r"C:\Users\varunpintu\Documents" #to_do

# link of the video to be downloaded
link=input("Enter the link of the video to download : ")

try:
    # object creation using YouTube
    # which was imported in the beginning
    yt = YouTube(link)
except:
    print("Connection Error") #to handle exception

# filters out all the files with "mp4" extension
mp4files = yt.streams.filter(resolution="1080p")

print(mp4files)
#to set the name of the file
#yt.set_filename('GeeksforGeeks Video')

# get the video with the extension and
# resolution passed in the get() function
temp=int(input("enter the itag number : "))
d_video = yt.streams.get_by_itag(temp)
try:
    # downloading the video
    d_video.download(SAVE_PATH)
except:
    print("SOME Error!")
print('Task Completed!')
