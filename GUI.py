import yt_dlp
import tkinter as tk
from tkinter import messagebox, filedialog
from tkinter import ttk

def download_video():
    link = link_entry.get().strip()
    if not link:
        messagebox.showerror("Error", "Please enter a link.")
        return

    # Let the user choose the save location
    output_path = filedialog.asksaveasfilename(defaultextension=".mp4", filetypes=[("MP4 files", "*.mp4")])
    if not output_path:
        messagebox.showinfo("Cancelled", "Download cancelled.")
        return

    ydl_opts = {
        'outtmpl': output_path,  # Output file name
        'format': 'best',        # Select the best video format
        'progress_hooks': [progress_hook],  # Add progress hook
    }

    try:
        progress_bar.start()  # Start the progress bar animation
        root.update_idletasks()  # Update the GUI
        print("Downloading...")
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([link])
        messagebox.showinfo("Success", f"Download finished successfully. Saved as '{output_path}'.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")
    finally:
        progress_bar.stop()  # Stop the progress bar animation

# Progress hook to update the progress bar
def progress_hook(d):
    if d['status'] == 'downloading':
        percent = d.get('downloaded_bytes', 0) / d.get('total_bytes', 1) * 100
        progress_bar['value'] = percent
        root.update_idletasks()

# Set up the GUI
root = tk.Tk()
root.title("YouTube Video Downloader")

# Create and place widgets
frame = tk.Frame(root, padx=10, pady=10)
frame.pack(padx=10, pady=10)

tk.Label(frame, text="Enter YouTube Link:").grid(row=0, column=0, sticky="w")
link_entry = tk.Entry(frame, width=50)
link_entry.grid(row=0, column=1, padx=5, pady=5)

progress_bar = ttk.Progressbar(frame, orient="horizontal", length=400, mode="determinate")
progress_bar.grid(row=1, columnspan=2, pady=10)

download_button = tk.Button(frame, text="Download", command=download_video)
download_button.grid(row=2, columnspan=2, pady=10)

# Run the application
root.mainloop()
