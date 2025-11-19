# Bulk MKV to MP4 Converter (Stream Copy)

A simple and fast Python script to batch convert `.mkv` video files to `.mp4` format without re-encoding.

It uses **FFmpeg stream copying** (`-c copy`), meaning the conversion is instantaneous and there is **zero quality loss**.

## 🚀 Features

- **Batch Processing**: Automatically detects and converts all `.mkv` files in the current folder.
- **Zero Quality Loss**: Uses stream copy (`vcodec='copy'`, `acodec='copy'`) instead of re-encoding.
- **Fast Performance**: Converts gigabytes of video in seconds.
- **Cross-Platform**: Works on Windows, macOS, and Linux (as long as Python and FFmpeg are installed).

## 📋 Prerequisites

1. **Python 3.x** installed.
2. **FFmpeg** installed on your system and added to your system PATH.
   - *Windows*: [Download Build](https://gyan.dev/ffmpeg/builds/), extract, and add `bin` folder to PATH.
   - *Mac*: `brew install ffmpeg`
   - *Linux*: `sudo apt install ffmpeg`

## 🛠️ Installation

1. Clone this repository or download the script.
2. Install the required Python wrapper:

```bash
pip install -r requirements.txt