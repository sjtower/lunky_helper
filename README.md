# GetimOliver's Lunky Helper

https://www.twitch.tv/getimoliver

A simple program to keep track of things in Spelunky 2.
 1. Hou Yi's Bow
 2. Sisters
 3. orbs in the Cosmic Ocean.

## Prerequisites

1. Python 3.x
2. Joy2Key

## Intallation

After installing Python 3, run the following commands
```
pip install pyWinhook
pip install pygame
```

## Running

1. This program only supports the keyboard. PyWinhook does not support controllers, so you will have to use Joy2Key if you want to interact using a controller. 
    - The default key for the bow is "Right"
    - The default key for orbs is "Left"
    - The default key for sisters is "Up"
    - Personally I like to bind orbs to L1 and bow/sisters to L2 or L3
1. Open a command prompt and execute the following:
    - navigate to where you downloaded the program. EG:
    ```
        cd C:\Users\Oliver\Downloads\lunky_helper
    ```
   - Use Python to execute `main.py':
   ```
        python main.py
   ```
1. I use a .bat file to run these steps. There is an example included in the download directory.
