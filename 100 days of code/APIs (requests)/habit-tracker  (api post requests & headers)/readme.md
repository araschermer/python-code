<br />
<p align="center">

  <h3 align="center">Habit tracker</h3>

  <p align="center">
    project_description
    <br />
The Habit tracker:
The habit tracker is used to track a user-defined habit and show the continuous progress and performance.
<br />
    <br />
  </p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
        <li><a href="#license">License</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project
This project handles the advanced API authentication method using headers, POST,PUT,DELETE requests. In this project , the [pixela API](https://pixe.la) is used to track  a user set habit and show the daily progress/performance.\
##Example:

![Alt text](example.PNG?raw=true "Title")


### Built in:
* [Python](Python)
### Modules used:
* [requests](https://pypi.org/project/requests/)
### APIs used:
[pixela API](https://pixe.la) 



<!-- GETTING STARTED -->
#Getting Started

To get a local copy up and running follow these simple steps.

### Installation
1-download the project file.\
2-install and import the `requests` module.\
3-  in `main.py` save a private user authentication TOKEN of length between [8-128] characters, a username, a Habit-id(habit name) and a project-name in the  empty strings of 
```py
TOKEN = ""
USERNAME = ""
HABIT_ID = ""
PROJECT_NAME =""
```

7- run the `main.py` script, which will \
```py
# create a user   through the following line 
create_account(token=TOKEN, username=USERNAME, url=pixela_endpoint)
# create a habit  through the following line
create_habit(habit_id=HABIT_ID, project_name=PROJECT_NAME, url=graph_endpoint, headers=headers)
# post an new activity though the following line:
post_data(headers=headers) 
# which should require the user input in the terminal for the duration of the habit practicing of this activity.
```
The following  functions can also be used just by removing the `#` in the corresponding lines:
###### update_pixels(headers=headers)
###### delete_day_data(headers=headers)

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.

