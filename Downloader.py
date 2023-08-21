from pytube import YouTube
from sys import argv

link = str(input("Enter YT Link: "))
yt = YouTube(link)
stream = yt.streams.get_highest_resolution()
stream.download("C:/Users/mitmp/Videos/Downloaded YT Videos")
print("Successfully Downloaded: " + yt.title + " By: " + yt.author)