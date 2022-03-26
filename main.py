from pytube import YouTube
from pytube import Playlist

print()



print()

print('\x1b[31mTHIS TOOL IS PROVIDED FOR DOWNLOADING YouTube VIDEO, PLAYLIST, AUDIO \n'
      'ENTER THE URL OF THE YouTube VIDEO OR PLAYLIST TO DOWNLOAD')
print()

if (input("Do you agree? (y/n) > ") in ['y', 'Y']):

        print()
        print("1. video\n"
              "2. playlist\n"
              "3. audio")
        print()
        num = input("Enter > ")
        print()

        if num == '1':
            # singel video

            #from pytube import YouTube

            link = input("Enter the youtube video link : ")

            youtube_d = YouTube(link)

            videos = youtube_d.streams
            vid = list(enumerate(videos))
            for i in vid:
                print(i)
            print()
            strm = int(input("enter list number : "))
            print()
            print(f"Downloading : {youtube_d.title}")
            print()
            videos[strm].download()
            print()
            print("Successfully download")
            print()
        elif num == '2':
            # playlist

            #from pytube import Playlist

            url = input("Enter Playlist URL : ")

            py = Playlist(url)

            print(f"Downloading : {py.title}")

            for video in py.videos:
                video.streams.first().download()

            print()
            print("Successfully download")
            print()

        elif num == '3':
            # audio

            from pytube import YouTube

            link = input("Enter the youtube video link : ")
            print()

            youtube_d = YouTube(link)

            videos = youtube_d.streams.filter(only_audio = True)
            vid = list(enumerate(videos))
            for i in vid:
                print(i)
            print()
            strm = int(input("enter list number : "))
            print()
            print(f"Downloading : {youtube_d.title}")
            print()
            videos[strm].download()
            print()
            print("Successfully download")
            print()

        else:
            print('Bip bip')
            exit(0)



else:
        print('Bip bip')
        exit(0)



