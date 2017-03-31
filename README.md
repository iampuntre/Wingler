# Wingler
An automation script to restart Huawei Wingle for Raspberry Pi. A crucial feature to automatically restart the Wingle
without human intervention.

## Getting Started
Your Raspberry Pi needs to be connected to the internet via Huawei Wingle.

### Prerequisites
Make sure you have git installed on your Raspberry Pi. To install git -
```
sudo apt-get install git
```

### Installing
Follow these instructions -


Update your drivers and download newer packages
```
sudo apt-get update
```

Install PhantomJS for Raspberry Pi
```
cd /tmp
sudo wget https://github.com/aeberhardo/phantomjs-linux-armv6l/archive/master.zip
sudo unzip master.zip
cd phantomjs-linux-armv6l-master
sudo bunzip2 *.bz2
sudo tar xf *.tar
sudo cp phantomjs-1.9.0-linux-armv6l/bin/phantomjs /usr/bin
```

Check for PhantomJS Installation
```
phantomjs --version
```

Clone the repository
```
cd ~
git clone https://github.com/iampuntre/Wingler.git
cd Wingler
```

Install the requirements
```
pip install -r requirements.txt
```

### Running the script
Run the python code
```
python wingle_web_scraper.py
```

## License
This project is licensed under the MIT License. See the LICENSE file for more details.