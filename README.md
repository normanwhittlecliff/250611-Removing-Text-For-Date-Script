<!-- COMMENT BEGINS



COMMENT ENDS --> 

# Removing Text For Date

A simple Python script that takes a given (in the script) folder path. <br>
Inside this folder, the script renames every single file in it by removing the text in front of it until it hits a number. 

This script was created by me, Norman, with the intention of organizing my photos and videos by date in its name. Every media in my phone has the date in its name, but some also have stuff like the application name in front of it, like Instagram or Zangi. To unify every media in one folder and sort it by date, I created this script that stripts the front text of the name, leaving the date. 

Any text that comes after the date is not modified.

#### Example:

| Before        | After |
| ------------- |:-------------:|
| Camera20250611_134050.png    | 20250611_134050.png     |
| Zangi20250611.png     | 20250611.png     |
| Instagram20250611.png | 20250611.png     |
| Capture354.png        | 354.png          |
| 20250611_134050.png    | 20250611_134050.png     |

The bit of code that you might wanna take a look is the `directory_path`. Change it to the folder path of your liking.

```
# Replace this path with the folder you want to clean up

directory_path = r"C:\Users\Norman Whittlecliff\Pictures\Phone Storage\camera"  # Example for Windows

# directory_path = "/home/user/Pictures"  # Example for Linux/Mac
```

## Information
- **Project ID**: 250611
- **Creator**: Norman Whittlecliff (Norman Santos)
- **Date of Creation**: June 11, 2025
- **Language**: Python

## Dependencies

- **Python 3**: I assume you already have it in your computer, but yeah, this one is needed to run the script.

## Warning

This script DOES NOT have safety features. Once it chnages the file's name, it's done. 

