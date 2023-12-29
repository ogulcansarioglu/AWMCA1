# AtrractionNation

PWA Geolocation App built on postGIS and hosted on EC2. It helps users to plan their trip in Ireland, using real-time traffic data, a custom built reccomandation and search engine. 
It also has a LLM implementation as a virtual assistant. 

website: [ogulcansarioglu.site](ogulcansarioglu.site) (Please add / at the end when navigating as I disabled append_slahs (APPEND_SLASH = False) like /api/v1/att/) 

demo: [video demo:https://youtu.be/-8cSagH8g7I](https://youtu.be/-8cSagH8g7I)

note: html template is: main.html, not index.html

# AttractionFinger - ogulcansarioglu.site

This app allows users to find attractions (natural parks, museums etc) and get information about them using ChatGPT assistant, along with providing a link via Google Search. 
It comes up with travel plan based on user's interest and show real-time traffic data and routes for driving, cycling and walking. It also has a custom built search engine. 
The app uses a spatial database, and dataset from data.gov.ie (Irish Goverment).

It is PWA and can be installed on smart phones as well as used as a web application.

# Tech Stack

1. Database: PostgreSQL with PostGIS
2. Database management: PgAdmin4
3. Middle tier(s): Django
4. API Dev: Rest-Framework for Django
5. API for Real-Time Traffic Data: MapBox
6. AI API: open-ai
7. Responsive, Progressive Front-end: Bootstrap, Javascript, django-pwa
8. Mapping: Leaflet JS with OpenStreetMap
9. Deployment: AWS EC2, Docker (PostGis, PgAdmin4, Django App, Nginx)

# Dataset

The dataset consist of attractions in Ireland provided by data.gov.ie. I created a model, migrate and load it into the database and keep it at persistent storage. 

# Functionalities

# 1. Search: 

You can search by name, tag or location and the app will responsively, automatically bring you the first-match as you type. I find it very convinent and user friendly (rather than using search results in a text format etc). 

# 2. Get 10 Closest Attractions

The app starts with showing the closest attraction to the users location. 

# 2. Click on the learn more

You can click on the attraction icon, and a new information box will pop up with name, adress and Google Search link along with an option to launch an intelligent assistant (open-ai)

# 3. Build a Travel Plan with Real-Time Routing 

Using MapBox API, this app allows users the select attraction by clicking on the icons, and then calculates a route for them along with duration, traffic status/delay possibility. Users may select to drive, cycle or walk. 
Traffic and Routing are all real-time information handled on the fly. 

# 4. Reccomandations for Travel Plan

Based on user interest and couple of questions, a user can get a travel plan via my smart reccomandation system and see it on the map in real-time along with all the associated information described above.

# 5. Attraction Assistant (ChatGPT implementation)

You can ask any question about the attraction in a persistent chat with ChatGPT4 virtual assistant designed for this purpose. Right now it's on testing phase, but I plan to implement it fully in my spare time after the assigment.

# 6. Fully Complient PWA App

It can be installed on mobile phone or windows and run that way. I attached both screenshot and lighthouse evaluation.

![PWA](https://github.com/ogulcansarioglu/AWMCA1/assets/93154247/305ca113-d845-4da0-b28e-083c3b29b796)

![installwindows](https://github.com/ogulcansarioglu/AWMCA1/assets/93154247/ce5a1769-0774-47e0-ba04-274c5782c6ae)

# 5. RestApI

You can navigate to ogulcansarioglu.site/api/v1/att/ or chat/ to see the RestAPI that I built for them, populated from the database and used in map creation. 

![api-page](https://i.ibb.co/2vNJdqn/Whats-App-Image-2023-11-12-at-12-51-05.jpg)

# 5. Leaflet Map

Not an extra but I also implemented leaflet with openstreetmaps for geolacation amd map purposes that enables all the above. ]

# 6. PgAdmin4

![pgadmin4-page](https://i.ibb.co/p2LgNBR/Whats-App-Image-2023-11-12-at-12-50-33.jpg)


#Responstive and PWA Design (Web Browser, Iphone, Android)

1. Web Chrome:

![web](https://github.com/ogulcansarioglu/AWMCA1/assets/93154247/40cb1811-ced3-436b-bce4-de504469a954)


3. Mobile: 

a. Iphone 13 Pro Max:

![iphonePro14](https://github.com/ogulcansarioglu/AWMCA1/assets/93154247/91f0e162-b15f-4cab-bf8f-ab6948dca0d3)

![reco](https://github.com/ogulcansarioglu/AWMCA1/assets/93154247/a835282e-1c0f-4ede-ab54-f5b718e5fd02)

![road](https://github.com/ogulcansarioglu/AWMCA1/assets/93154247/9ee01999-2826-4bca-8a1f-c2d04081cfce)

b. Samsung S13, android: 


![Abdriud](https://i.ibb.co/6F0myDq/Whats-App-Image-2023-11-12-at-12-31-01.jpg)


# Future

The user will be able to responsively interact with virtualt assistant. I implemented the chatGPT functionality, but it needs to be Prompt Engineer for this special use-case which I didn't have enough time for (or else it will just chat about anything which shouldn't happen, it needs negative prompts to limit itself).
So for now I just leave at testing mock-up response. 

Users will be able to find hotels near to attractions of their chaice. I want to retrieve hotels closers to these locations that one can stay after selecting an attraction, I build some of the back-end for that but I didn't have enough time to enable it in the app. 












