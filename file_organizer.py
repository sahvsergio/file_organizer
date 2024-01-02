"""
This file organizes files from the downloads folder into separate folders in the system, based on file extensions
"""
# !/usr/bin/python3
# standard library imports
import shutil
import os


#related third party mports 
import rich
from rich.prompt import Prompt

hello=Prompt.ask('Enter the file path')



__author__ = 'Sergio Andrés Herrera Velásquez'







#python3 / home/sahvsergio/Documents/projects/file_organizer/file_organizer.py
#


# Text file extensions
text_extensions = ['.txt', '.doc', '.docx', '.pdf', '.html', '.csv']


# Image file extensions
image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff']

# Audio file extensions
audio_extensions = ['.mp3', '.wav', '.flac', '.aac', '.ogg', '.wma']

# Video file extensions
video_extensions = ['.mp4', '.avi', '.mkv', '.mov', '.wmv', '.flv']
archive_extensions=  shutil.get_archive_formats()


# home directory
with os.scandir(os.path.join(os.path.expanduser('~'), 'Downloads')) as files:

    for entry in files:
        #
        text_dir = os.path.join(os.path.expanduser('~'), 'Documents')
        image_dir = os.path.join(os.path.expanduser('~'), 'Pictures')
        audio_dir = os.path.join(os.path.expanduser('~'), 'Music')
        video_dir = os.path.join(os.path.expanduser('~'), 'Videos')

        if not entry.name.startswith('.') and entry.is_file:
            entry_name, entry_ext = os.path.splitext(entry.name)
            if entry_ext in text_extensions:
                shutil.move(os.path.join(os.path.expanduser(
                    '~'), 'Downloads', entry.name), os.path.join(text_dir, entry.name))
            elif entry_ext in image_extensions:
                shutil.move(os.path.join(os.path.expanduser(
                    '~'), 'Downloads', entry.name), os.path.join(image_dir, entry.name))
            elif entry_ext in audio_extensions:
                shutil.move(os.path.join(os.path.expanduser(
                    '~'), 'Downloads', entry.name), os.path.join(audio_dir, entry.name))
            elif entry_ext in video_extensions:
                shutil.move(os.path.join(os.path.expanduser(
                    '~'), 'Downloads', entry.name), os.path.join(video_dir, entry.name))
            elif entry_ext in archive_extensions[0] or  archive_extensions[1] or archive_extensions[2] or archive_extensions[3] or archive_extensions[4]:
                shutil.move(os.path.join(os.path.expanduser('~'), 'Downloads', entry.name), os.path.join(text_dir, entry.name))
