from downloader.video_downloader import download_video
from utils.validator import is_valid_url

def main():
    url = input("Enter video URL: ").strip()

    if not is_valid_url(url):
        print("Invalid URL")
        return

    download_video(url)
    print("Download completed!")

if __name__ == "__main__":
    main()
