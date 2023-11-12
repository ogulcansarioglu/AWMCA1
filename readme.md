# AWMCA1
Responsive Progressive Geolocation App built on postGIS and hosted on EC2 

website: ogulcansarioglu.site

# AttractionFinger - ogulcansarioglu.site

This app allows users to find attractions (natural parks, museums etc) and get information about them using ChatGPT assistant, along with providing a link via Google Search. 
The app uses a spatial database, and dataset from data.gov.ie (Irish Goverment)

# Tech Stack

1. Database: PostgreSQL with PostGIS
2. Database management: PgAdmin4
3. Middle tier(s): Django
4. API Dev: Rest-Framework for Django
5. AI: open-ai 
6. Responsive, Progressive Front-end: Bootstrap, Javascript, django-pwa
7. Mapping: Leaflet JS with OpenStreetMap
8. Deployment: AWS EC2, Docker (PostGis, PgAdmin4, Django App, Nginx)

# Dataset

The dataset consist of attractions in Ireland provided by data.gov.ie. I created a model, migrate and load it into the database and keep it at persistent storage. 

# Functionalities

# 1. Search: 

You can search by name, tag or location and the app will responsively, automatically bring you the first-match as you type. I find it very convinent and user friendly (rather than using search results in a text format etc). 

# 2. Click on the learn more

You can click on the attraction icon, and a new information box will pop up with name, adress and Google Search link along with an option to launch an intelligent assistant (open-ai)

# 3. Attraction Assistant (ChatGPT implementation)

You can ask any question about the attraction in a persistent chat with ChatGPT4 virtual assistant designed for this purpose. Right now it's on testing phase, but I plan to implement it fully in my spare time after the assigment.

# 4. RestApI

You can navigate to ogulcansarioglu.site/api/v1/att/ to see the RestAPI that I built for it, populated from the database and used in map creation. I also have ogulcansarioglu.site/api/v1/chat/ which is functionality based so won't be rendering anything but you can send
POST request via Postman or curl. 

# 5. Leaflet Map

Not an extra but I also implemented leaflet with openstreetmaps for geolacation amd map purposes that enables all the above. ]


#Responstive Design (Web Browser, Iphone, Android)

1. Web Chrome:

![alt-text](https://i.ibb.co/kMv3hs7/web.jpg)

2. Mobile: 

a. Iphone 13 Pro Max:

![Iphone 13](https://i.ibb.co/Tm6FgRX/Whats-App-Image-2023-11-12-at-12-27-05.jpg)

![Iphone 13](https://i.ibb.co/Pc4yrn5/Whats-App-Image-2023-11-12-at-12-27-07.jpg)

b. Samsung S13, android: 


![Abdriud](https://i.ibb.co/6F0myDq/Whats-App-Image-2023-11-12-at-12-31-01.jpg)


# Future

The user will be able to responsively interact with virtualt assistant. I implemented the chatGPT functionality, but it needs to be Prompt Engineer for this special use-case which I didn't have enough time for (or else it will just chat about anything which shouldn't happen, it needs negative prompts to limit itself).
So for now I just leave at testing mock-up response. 

Users will be able to find hotels near to attractions of their chaice. I want to retrieve hotels closers to these locations that one can stay after selecting an attraction, I build some of the back-end for that but I didn't have enough time to enable it in the app. 












