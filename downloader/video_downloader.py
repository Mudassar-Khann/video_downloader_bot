import yt_dlp

def download_video(url):
    options = {
        "outtmpl": "videos/%(title)s.%(ext)s",
        "format": "best"
    }

    with yt_dlp.YoutubeDL(options) as ydl:
        ydl.download([url])
