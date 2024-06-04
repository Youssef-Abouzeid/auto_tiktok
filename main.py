from reddit_scraper.scraper import get_top_post
from tts.text_to_speech import text_to_speech
from video_editor.editor import create_video_with_subtitles
from screenshot.capture import capture_screenshot
from tiktok_uploader.uploader import upload_to_tiktok
import config

def main():
    subreddit = 'subreddit_name'
    title, text, url = get_top_post(subreddit)
    
    text_to_speech(text, 'voiceover.mp3')
    
    # Assuming OBS has already recorded gameplay to 'gameplay.mp4'
    
    capture_screenshot(url, 'screenshot.png')
    
    create_video_with_subtitles('gameplay.mp4', 'voiceover.mp3', 'screenshot.png', 'output_video.mp4', text.split('. '))
    
    upload_to_tiktok('output_video.mp4', title)

if __name__ == "__main__":
    main()
