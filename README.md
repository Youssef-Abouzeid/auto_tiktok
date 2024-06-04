# Automated TikTok Video Uploader

This project automates the creation and uploading of TikTok videos featuring Minecraft gameplay, AI voice-overs reading Reddit subreddit text, subtitles, and screenshots of subreddit posts.

## Directory Structure

- `main.py`: Main script to run the entire process.
- `config.py`: Configuration file for credentials and settings.
- `reddit_scraper/`: Contains the script to scrape Reddit.
- `tts/`: Contains the script for text-to-speech conversion.
- `video_editor/`: Contains the script for video editing and subtitle addition.
- `screenshot/`: Contains the script for capturing subreddit post screenshots.
- `tiktok_uploader/`: Contains the script to automate TikTok video uploads.

## Requirements

- Python 3.x
- Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Update the `config.py` file with your credentials.
2. Run the `main.py` script:
    ```bash
    python main.py
    ```

## Notes

- Ensure OBS Studio is set up to record Minecraft gameplay.
- Selenium requires ChromeDriver to be installed and configured properly.

