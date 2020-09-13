# Shibe Downloader by @fsalamic    
# Features of the program:

 - ability to download multiple dog (shibe) pictures by using the https://shibe.online API
 - creates a folder called shibe if you don't have one in the folder
 - if you have the folder, downloads images by subsequently naming them (for example if you have shibe-1,..,3 in the folder, it will download the new files while naming them shibe 4,5,...)

# How to use this program
First things first you will need to install the required dependencies by doing the command bellow (make sure that you have pip installed) :

```pip3 install requests```

If you don't have pip installed , do the following commands (if you are using ubuntu) :
```
sudo apt update
sudo apt install python3-pip
```
After installing the needed dependencies , do the following commands :
```
git clone https://github.com/fsalamic/shibe-downloader.git
cd shibe-downloader
```
Once you do these commands, you're good to go:
```
python3 downloader.py
```
