"""
This file organizes
files from the downloads
folder into separate folders in the system,
"""
# !/usr/bin/python3
# standard library imports
import shutil
import os

# related third party imports
import rich
from rich import print as rprint
from rich.console import Console
from rich.prompt import Prompt
from rich.progress import track
from rich.layout import Layout
from dotenv import load_dotenv




#identiify the
__author__ = 'Sergio Andrés Herrera Velásquez'
__email__='sergioandresherrera@gmail.com'

# load the environment variables
load_dotenv()


# Text file extensions
text_extensions = os.getenv('text_extensions')
# Image file extensions
image_extensions = os.getenv('image_extensions')
# Audio file extensions
audio_extensions = os.getenv('audio_extensions')
# Video file extensions
video_extensions = os.getenv('video_extensions')
#Archive_extensions
archive_extensions=  shutil.get_archive_formats()


#console
console=Console()

text_files=[]
image_files=[]
audio_files=[]


# home directory
with os.scandir(os.path.join(os.path.expanduser('~'), 'Downloads')) as files:

    for entry in files:
        #destination paths
        text_dir = os.path.join(os.path.expanduser('~'), 'Documents')
        image_dir = os.path.join(os.path.expanduser('~'), 'Pictures')
        audio_dir = os.path.join(os.path.expanduser('~'), 'Music')
        video_dir = os.path.join(os.path.expanduser('~'), 'Videos')
        
        with console.status("[bold green]Fetching data...") as status:
            
            
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
            console.log(f'[bold][red]Done!')