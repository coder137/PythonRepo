# Working

xkcdDownloader downloads images from [the xkcd site](https://xkcd.com) from the first page all the way upto the last page (1st comic).
Images are saved as 'img_num'.'img_name' in the Comic Folder

An additional check feature is added so that no file is downloaded twice.
If the file exists insde the Comic Directory that image is not downloaded from the xkcd site again.
Thereby maximizing efficiency

**If any file is accidentaly deleted just run the script, it will automatically find the file that isn't present and download it**

# Pre-requisites

Install dependencies using `pip install -r requirements.txt`

External Modules used are
* requests
	* `pip install requests`
	* http/https requests
* BeautifulSoup
	* `pip install beautifulsoup4`
	* html file parsing

# Commands

These are the commands you can use to maximize efficiency

* -v
    * for verbose print to console
* -vf filename
    * for logging to filename
* -s start_num
    * start downloading from number
    * default is first number (from the first webpage)
* -e end_num
    * stop downloading at number
    * default is last number (till the last webpage) /1/

*Verbose mode (-v) to console is on by default*


# Compilation

Compiling into one single executable exe file

`pip install pyinstaller`

`pyinstaller -F run.py`

# Run

Replace `python run.py` with `run.exe`

* python run.py -s 100 -e 90
	downloads from the 100th comic till the 90th comic
* run.exe -s 100 -e 90
	downloads from the 100th comic till the 90th comic
* run.exe -vf "log.txt"
	downloads from the first comic till the last comic and saves logs in log.txt file (no logs on screen)
* run.exe -v -s 100
	downloads from the 100th comic till the last comic and outputs logs on the console


Have Fun xD
