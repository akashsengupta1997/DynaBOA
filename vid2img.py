import os
import os.path as osp
import cv2
import subprocess
import glob
import config

def video_to_images(vid_file, img_folder=None, return_info=False):
    if img_folder is None:
        img_folder = osp.join('/tmp', osp.basename(vid_file).replace('.', '_'))

    os.makedirs(img_folder, exist_ok=True)

    command = ['ffmpeg',
               '-i', vid_file,
               '-f', 'image2',
               '-v', 'error',
               f'{img_folder}/%06d.png']
    print(f'Running \"{" ".join(command)}\"')
    subprocess.call(command)

    print(f'Images saved to \"{img_folder}\"')

    return img_folder

vid_dir = config.InternetData_ROOT
vid_files = [os.path.join(vid_dir, f) for f in os.listdir(vid_dir) if f.endswith('.mp4')]
for vid_file in vid_files:
    forename = osp.basename(vid_file)[:-4]
    print(vid_file)
    video_to_images(vid_file, f'{vid_dir}/images/{forename}')