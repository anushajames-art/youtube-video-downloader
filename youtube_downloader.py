#!/usr/bin/env python3
"""
Simple YouTube Video Downloader
Downloads videos from YouTube URLs to your device
"""

import os
import sys
from pathlib import Path

try:
    from yt_dlp import YoutubeDL
except ImportError:
    print("❌ yt_dlp not installed. Install it first:")
    print("   pip install yt-dlp")
    sys.exit(1)


def download_youtube_video(url, output_path="downloads"):
    """
    Download a YouTube video from the given URL
    
    Args:
        url (str): YouTube video URL
        output_path (str): Directory to save the video (default: 'downloads')
    
    Returns:
        bool: True if successful, False otherwise
    """
    
    # Create output directory if it doesn't exist
    Path(output_path).mkdir(parents=True, exist_ok=True)
    
    # Configure yt_dlp options
    ydl_opts = {
        'format': 'best[ext=mp4]/best',  # Download best quality MP4
        'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
        'quiet': False,
        'no_warnings': False,
    }
    
    try:
        print(f"🔗 Downloading: {url}")
        print(f"📁 Saving to: {os.path.abspath(output_path)}")
        
        with YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            filename = ydl.prepare_filename(info)
            
        print(f"✅ Downloaded successfully!")
        print(f"📄 File: {filename}")
        return True
        
    except Exception as e:
        print(f"❌ Error downloading video: {str(e)}")
        return False


def main():
    """Main function to handle user input and download"""
    
    print("=" * 50)
    print("🎬 YouTube Video Downloader")
    print("=" * 50)
    
    # Get YouTube URL from user
    url = input("\n🔗 Paste YouTube URL: ").strip()
    
    if not url:
        print("❌ No URL provided!")
        return
    
    # Validate URL
    if "youtube.com" not in url and "youtu.be" not in url:
        print("❌ Invalid YouTube URL!")
        return
    
    # Get custom output path (optional)
    custom_path = input("\n📁 Output folder (press Enter for 'downloads'): ").strip()
    output_path = custom_path if custom_path else "downloads"
    
    # Download the video
    if download_youtube_video(url, output_path):
        print(f"\n🎉 Done! Check the '{output_path}' folder.")
    else:
        print("\n❌ Download failed.")


if __name__ == "__main__":
    main()
