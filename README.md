# Biebernet-Biebemotion-Box
Wrapping Twitter, natural language processing for sentiment analysis, and text-to-speech APIs togther with code to control LEDs, every hour on the hour you can have Justin Bieber serenade you with his tweets -- with mood lighting to boot

# Dependencies
You need to install [wiringPi](http://wiringpi.com/download-and-install/) to control the LEDs, and you need to have SPI enabled from the options when running `sudo raspi-config`

[eSpeak](http://espeak.sourceforge.net/) is used for text-to-speech, which you can install by running `sudo apt-get install espeak`

Make sure you have all your audio dependencies installed for text-to-speech to work by following this [guide](https://www.google.com/search?client=ubuntu&channel=fs&q=raspberry+pi+text+to+speech&ie=utf-8&oe=utf-8)

Finally, the [python-twitter](https://github.com/bear/python-twitter) API needs to be installed, which can be done by running `sudo pip install python-twitter`

# Installation and Setup
Clone this repo using `git clone git@github.com:kbreitton/Biebernet-Biebemotion-Box.git`

For the Twitter API to work, you need to have proper authentication keys. You will need to make a file called `api-keys.txt` in the same folder as all these files. This textfile should contain only 4 lines: Consumer Key, Consumer Key Secret, Access Token Key, Access Token Key Secret. These API keys can be found from [https://apps.twitter.com](https://apps.twitter.com) 

Run `make`
and run `chmod +x driver.py`

Edit your `~/.bashrc` file and at the end add these lines:
```
cd path/to/Biebernet-Biebemotion-Box                                                                                                                                        
./driver.py
```

Edit your crontab (run `crontab -e`) to include the line `@hourly path/to/Biebernet-Biebemotion-Box/driver.py` to run hourly

Finally hardware-wise, follow the [pin-out guide](http://wiringpi.com/pins/) from wiringPi and connect the [LPD8806](https://www.adafruit.com/products/306) strips over SPI to the Pi
