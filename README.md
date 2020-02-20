# Awwards
## Author
Alice mwihaki
  
# Description  
This project allows users to post their projects for other users to rate according to design, usability, creativity and content.

 
## User Story  
  
* A user can view posted projects and their details.  
* A user can post a project to be rated/reviewed. 
* A user can rate/ review other users' projects.  
* Search for projects.  
* View projects overall score.
* A user can view their profile page.  
  

  
## Setup and Installation  
To get the project : 
  
##### Clone the repository:  
 ```bash 
 https://github.com/cynthiaoduol/project-awwards.git 
```

##### Install and activate Virtual  
 ```bash 
- python3 -m venv virtual - source virtual/bin/activate  
```  


##### Navigate into the folder and install requirements with te command:
 ```bash 
pip install -r requirements.txt 
```

##### Install Dependencies  
 ```bash 
 pip install -r requirements.txt 
```  
 ##### Setup Database  
  SetUp your database User,Password, Host then make migrations:
 ```bash 
python manage.py makemigrations instagram
 ``` 
 Then Migrate: 
 ```bash 
 python manage.py migrate 
```
##### Run the application  
 ```bash 
 python manage.py runserver 
``` 
##### Testing the application  
 ```bash 
 python manage.py test 
```
Open the application on your browser `127.0.0.1:8000`.  
  

## BDD
| Behavior            | Input                         | Output                        | 
| ------------------- | ----------------------------- | ----------------------------- |
| User visits the app and gets directed to the homepage  | User clicks on a project to review | Directed to the login page | 
If user has no account, they click on `sign up` | User signs up | User is redirected to the log in page |
|  Single projecct loads | User clicks on vote  | Modal appears where they vote |
|  Homepage loads | Click `profile` | User's profile appears | 
| Homepage loads | Click `Submit Project` button | User's redirected to a page where they can upload a project |  
| Homepage loads | User inputs in the search form and presses enter | Searched results show |

## Technologies Used
* Python3.6
* Django
* HTML
* Bootstrap

## Known Bugs
can't be rated based on:

1. Design
2. Usability
3. Content

## contacts
for more information or questions:
   alicekibe65@gmal.com

## License
This project is Licensed under MIT. ©2019 Copyright.
