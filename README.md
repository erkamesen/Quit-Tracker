# Quit-Tracker
Quit Tracker app with made it Flask MicroFramework

## Content
- [Features](https://github.com/erkamesen/Quit-Tracker/blob/master/README.md#features)
- [Technologies](https://github.com/erkamesen/Quit-Tracker/blob/master/README.md#technologies)
- [Installation & Usage](https://github.com/erkamesen/Quit-Tracker/blob/master/README.md#installation--usage)
- [Snaps](https://github.com/erkamesen/Quit-Tracker/blob/master/README.md#snaps)

---
## Features
- Users can register
- Users can send message with telegram from the contact section.
- User can track the time elapsed since he/she quit smoking.
- User can track the money that he/she has not given to cigarettes during this period.
- An average cigarette takes 10 minutes from a person's life. The user can track how much time he/she has saved.
- User will be motivated as they see the progress.
- 60 quotes from the json file are randomly displayed to the user.
- If user smokes and quits again, he/she can update their information.
- quit smoking not LIFE !!

## Technologies
<div align=center>
<img src=https://user-images.githubusercontent.com/25181517/192107854-765620d7-f909-4953-a6da-36e1ef69eea6.png wirdth=60 height=60>
<img src=https://user-images.githubusercontent.com/25181517/192158954-f88b5814-d510-4564-b285-dff7d6400dad.png wirdth=60 height=60>
<img src=https://user-images.githubusercontent.com/25181517/183898674-75a4a1b1-f960-4ea9-abcb-637170a00a75.png wirdth=60 height=60>
<img src=https://user-images.githubusercontent.com/25181517/117447155-6a868a00-af3d-11eb-9cfe-245df15c9f3f.png wirdth=60 height=60>
<img src=https://user-images.githubusercontent.com/25181517/183423507-c056a6f9-1ba8-4312-a350-19bcbc5a8697.png wirdth=60 height=60>
<img src=https://user-images.githubusercontent.com/25181517/183423775-2276e25d-d43d-4e58-890b-edbc88e915f7.png wirdth=60 height=60>
</div>

## Install & Usage


- Clone the repository:

```
git clone https://github.com/erkamesen/Quit-Tracker.git
```

- Navigate to the directory:

```
cd Quit-Tracker
```

- To get started with the Quit Tracker app, you'll need to have the following dependencies installed on your machine:
- install the requirements:

```
pip install -r requirements.txt
```
- Set Telegram token in controller/utils.py
```
logger = Logger(token=os.getenv("APIKey"),
                chat_id=os.getenv("chatID"))  # TELEGRAM BOT
```
- Run the application:

```
flask run
```


Portfolio project should now be running on your local machine at http://localhost:5000

- Register and use your Quit Tracker 👍👍👍

## Snaps

<div align=center>
<h4 > Index </h4> 
<img src=https://user-images.githubusercontent.com/120065120/223231004-3760bad5-a126-40db-b09b-54db8120659a.png>
<div>


<div align=center>
<h4 > Stats </h4> 
<img src=https://user-images.githubusercontent.com/120065120/223231096-617a034a-5472-4dd8-9c26-fef460d1a10c.png>
<img src=https://user-images.githubusercontent.com/120065120/223231205-f9db4def-fcf8-4e31-9793-9ec3fb63b3e0.png>
<div>

<div align=center>
<h4 > Login </h4> 
<img src=https://user-images.githubusercontent.com/120065120/223231405-a2e6ad63-8976-43f9-a824-cfde50d81f5b.png>
<div>

<div align=center>
<h4 > Register </h4> 
<img src=https://user-images.githubusercontent.com/120065120/223231295-409e21d8-3b8f-4872-a3b4-db8d824427d3.png>
<div>


<div align=center>
<h4 > Contact </h4> 
<img src=https://user-images.githubusercontent.com/120065120/223231489-d6bec193-3859-40f6-825e-be5b0a08d6c9.png>
<div>











