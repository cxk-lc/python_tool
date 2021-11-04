# -*- coding: utf-8 -*-

import os
import time

from moviepy.editor import VideoFileClip


class ParameterError(Exception):
    pass


def video_to_gif(video_path, gif_path=None, quality=0.5):
    supported_formats = ['mp4', 'wmv', 'rm', 'avi', 'flv', 'webm', 'wav',
                         'rmvb']
    if not os.path.exists(video_path):
        raise ParameterError('The input file does not exist.')
    dir_path, video_file_name = os.path.split(video_path)
    name, extension = video_file_name.split('.')
    if extension.lower() not in supported_formats:
        raise ParameterError(f'*.{extension} file is not supported.')
    if not gif_path:
        gif_path = os.path.join(dir_path, f'{name}.gif')
    # print('Start conversion...')
    clip = VideoFileClip(video_path)
    clip.set_duration(clip.duration)
    clip.write_gif(gif_path, fps=clip.fps * quality, verbose=False)
    clip.close()
    # print(f'Output GIF to {gif_path} succeeded.')


if __name__ == '__main__':
    dividing_line = '-' * 10 + 'I am the dividing line' + '-' * 10
    while True:
        print('Please select your action: \na: Video to gif\nb: Exit')
        opt = input('Please enter:')
        print(dividing_line)
        if opt == 'a':
            path = input('Please enter the video path to convert: \n')
            print(dividing_line)
            try:
                video_to_gif(path)
            except Exception as e:
                print(e)
                print(dividing_line)
        else:
            print('Exiting...')
            time.sleep(0.5)
            break
