Get Out My Room v0.1
[![Python 3.6](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org/downloads/release/python-310/)
==============
I hate people coming in my room when i'm not there. Get Out My Room is a simple security system that sends notifications with videos to your phone whenever people enter you room. 

![Capture](https://user-images.githubusercontent.com/85095943/148777964-f801275a-64ff-45ce-9e2a-fcf2b46c1a0e.PNG)

Installation and Setup
==============
- Install the requirements 
```pip install -r requirements.txt```
- Set up a Pushbullet account on your PC and Phone
  
   For PC
      Go to Pushbullet.com

      Create an account

  ![Psuh-660x465](https://user-images.githubusercontent.com/85095943/148778992-a8f341ed-c43b-4472-b89f-c4af307bb9dd.png)

   For Phone
      Install the Pushbullet app on your phone.

      Log in using the same email address that you used to log in to your PC.

  ![Screenshot2021061920055143](https://user-images.githubusercontent.com/85095943/148779234-200c759d-120f-4e2c-b21f-4e508d6b5bcc.png)\
  
  - Once you have setup pushbullet you will need an api key. To do this go to pushbullet.com -> Settings -> Generate Access Token
  - Once the access token has been generated, go into ```scripts/config.py``` and paste you API key into the API_KEY field
  - Run ```main.py```

