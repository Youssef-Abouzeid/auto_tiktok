from moviepy.editor import VideoFileClip, AudioFileClip, ImageClip, CompositeVideoClip, TextClip

def create_video_with_subtitles(video_path, audio_path, screenshot_path, output_path, subtitles):
    video = VideoFileClip(video_path)
    audio = AudioFileClip(audio_path)
    video = video.set_audio(audio)
    
    screenshot = ImageClip(screenshot_path).set_duration(video.duration)
    video = CompositeVideoClip([video, screenshot.set_position(("center", "top"))])
    
    def add_subtitles(clip, text, duration, start_time):
        txt_clip = TextClip(text, fontsize=24, color='white')
        txt_clip = txt_clip.set_pos('bottom').set_duration(duration).set_start(start_time)
        return CompositeVideoClip([clip, txt_clip])
    
    start_time = 0
    for line in subtitles:
        video = add_subtitles(video, line, 3, start_time)
        start_time += 3
    
    video.write_videofile(output_path, codec='libx264')
