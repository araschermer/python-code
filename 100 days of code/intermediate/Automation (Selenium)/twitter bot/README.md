### In this project, I used Selenium to implement a tweet bot to write tweets to the internet provider complaining about the internet speed, once the speed goes lower than the promised speed 
#### first: the bot checks out the internet speed on [speed test](https://www.speedtest.com) 
##### I used Selenium to get to the speed test webpage and accept the cookies pop up, and start the test to obtain the following information:
- Download speed 
- Upload speed
- PING
#### If either of these properties are less than their promised values, then the Bot logs in [Twitter](https://www.twitter.com) and given a username and password (that are stored in the environment variables) and tweets to the internet provider with  a complaint  containing the current download/upload/ping speed.
- ##### In check_speed_test.py, I implemented the internet speed checking automation.
- ##### In login.py, I implemented the  automation twitter logging.
- ##### In tweet.py, I implemented the automated tweeting at the internet provider (given a complaint)
- ##### In main.py, I implemented the driver initialization, called the internet-speed checking function to test the internet speed  and compare it to the promised speed. once it is lower than the promised values: the driver launches the twitter page, logs in, and tweets to the internet provider
