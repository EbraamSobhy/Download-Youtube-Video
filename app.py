import yt_dlp

try:
    link = input("Enter a link to download: ").strip()

    # Set output file name and path
    output_path = "Video_Download.mp4"
    ydl_opts = {
        'outtmpl': output_path,  # Output file name
        'format': 'best'        # Select the best video format
    }

    print("Downloading...")
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])

    print(f"Download finished successfully. Saved as '{output_path}'.")
except Exception as e:
    print(f"An error occurred: {e}")
