import os

from ffmpeg import video



class VideoAnalyser:
    # 找到视频，提取字幕，提取元数据，提取音频轨道，按预设的频率抽帧
    # 根据图片embedding，切分视频镜头，根据时间区间，获取音频，图片序列，提取每个镜头的信息
    # 汇总镜头信息，生成视频摘要
    def __init__(self, video_path):
        self.video_path = video_path

    def get_i_frame_from_ffmpeg(self):
        video.



def _get_I_frame_from_ffmpeg(video_path):
    # execute command line
    # ffmpeg -i input.mp4 -vf "select=eq(pict_type\,I)" -vsync vfr thumb%04d.png
    os.system('ffmpeg -i ' + video_path + ' -vf "select=eq(pict_type\,I)" -vsync vfr thumb%04d.png')