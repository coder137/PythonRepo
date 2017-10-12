import sys
import logging
from flask import Flask

import xkcdDownloader as downloader
import fileIO
"""
-v
    for verbose print to console
-vf <filename>
    for logging to filename
-nl
    for no logging at all
-s <start_num>
    start downloading from number
    default is first number
-e <end_num>
    stop downloading at number
    default is last number
"""
# Main Program


#Flask Program

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello Flask"

if __name__ == "__main__":
    app.run()

#
print(sys.argv)

if '-vf' in sys.argv:
    f_name = sys.argv[sys.argv.index('-vf')+1]
    logging.basicConfig(filename=f_name,
                        level=logging.DEBUG,
                        format='%(levelname)s - %(message)s')
# elif '-v' in sys.argv or len(sys.argv) <= 1:
elif '-vf' not in sys.argv:
    # automatically start the logs
    logging.basicConfig(level=logging.DEBUG,
                        format='%(levelname)s - %(message)s')

if len(sys.argv) <= 1:
    # this is for people who cannot use command line and run from there
    get_commands = input("Do you want to input commands? y/n\n> ")
    # Make the input string lower case so you don't have to add more cases. :)
    get_commands = get_commands.lower()
    if get_commands is 'y':
        commands = input("ex. -s 100 -e 90\ninput> ")
        command_list = commands.split(" ")
        logging.debug(command_list)
        for i in command_list:
            sys.argv.append(i)

if '-nl' in sys.argv:
    logging.disable(logging.CRITICAL)

# Main function starts here
url = "https://xkcd.com"
filename = "parse.html"
folder = "Comic"

# Make folder if not present & get downloaded file(s) from folder dir
fileIO.makeFolder(folder)
downloaded = fileIO.getFiles(folder)
logging.info(str(downloaded)+"\n\n")

# get start_num. FIRST
# if -s is specified we dont need to init
if '-s' in sys.argv:
    pic_num = sys.argv[sys.argv.index('-s')+1]
    # downloader.site_join(start_num)
    # pic_url, prev_num, pic_num = downloader.get_schema(start_num, filename)
    # downloader.download_comic(pic_url, pic_num, folder)
else:
    # start from starting, FIRST
    pic_url, prev_num, pic_num = downloader.get_schema(url, filename)
    if pic_url is not -1:
        if pic_num not in downloaded:
            downloader.download_comic(pic_url, pic_num, folder)
        else:
            logging.info("Not Downloaded "+str(pic_num))
    else:
        logging.debug("Comic does not exist")
# NOTE, from here we get pic_num properly so use that ahead
pic_num = int(pic_num)

if '-e' in sys.argv:
    end_num = sys.argv[sys.argv.index('-e')+1]
else:
    # end at 1;
    end_num = '1'
    pass
# NOTE, from here we get end_num properly so use that
end_num = int(end_num)-1  # -1 so that we go till that number

for pnum in range(pic_num, end_num, -1):
    # check for pic_num
    snum = str(pnum)
    if snum not in downloaded:
        logging.info("Downloading "+snum)
        url = downloader.site_join(snum)
        pic_url, prev_num, pic_num = downloader.get_schema(url, filename)
        if pic_url is not -1:
            downloader.download_comic(pic_url, pic_num, folder)
            logging.info("Finished download "+snum+"\n")
        else:
            print("Comic does not exist")
            continue
        # NOTE, We do not use prev_num since we are manually checking
    else:
        logging.info("Already downloaded "+snum)
    # if there in files then do not download
    # else download
    pass

# if -s is specified

# downloader.main()
