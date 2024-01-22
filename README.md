
# File Organizer

## What it does



![Logo](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/th5xamgrr6se0x5ro4g6.png)

The file organizer  is an automation script  that uses python3 with its libraries os, shutil and rich so that it reads the names of the files in the Downloads folder and moves it to the corresponding based on their file extension as a way of automating moving files to their corresponding file.

Ubuntu 23.10 desktop  was used as it is a linux distro that I am quite familiar with.

Python 3.11 was used because it is the programming language I am more familiar with and also because its flexibility and multiple libraries which allow for ease in the implementation of os automation tasks. 

The python libraries used were:

*OS for os operations such as reading a directory's content, changing directories, filepath operations.

*Shutil was used for its different file moving utilities.

*Rich was used in order to provide some additional styling and features to the cli output and progress making it easier on the eyes for the end user.

Some features I plan to implement in the future are :

*Adding a  way of prompting the user to provide the filepath that they want to organize.

*Adding a summary of the total files moves by filetype and extension.

*Adding tests




## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

text_extensions = ['.txt', '.doc', '.docx', '.pdf', '.html', '.csv']


# Image file extensions
image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff']

# Audio file extensions
audio_extensions = ['.mp3', '.wav', '.flac', '.aac', '.ogg', '.wma']

# Video file extensions
video_extensions = ['.mp4', '.avi', '.mkv', '.mov', '.wmv', '.flv']

## Installation


![Logo](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/th5xamgrr6se0x5ro4g6.png)

