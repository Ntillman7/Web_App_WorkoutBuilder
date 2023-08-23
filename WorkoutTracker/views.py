import datetime
import os
import re
from django.shortcuts import render, redirect, get_object_or_404
from .forms import WorkoutForm
from .models import Workout, WorkoutFavorites, WorkoutInformation
import requests
import json
from bs4 import BeautifulSoup

# Story #1: Build the basic app -----------------------------


def workout_home(request):
    return render(request, 'WorkoutTracker/WT_home.html')

# Story #2: Create your model -------------------------------


def workout_create(request):
    form = WorkoutForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('WT_log')
    content = {'form': form}
    return render(request, 'WorkoutTracker/WT_create.html', content)

# Story #3: Display all items from database ------------------


def workout_log(request):
    workout = Workout.Workouts.all()
    content = {'workout': workout}
    return render(request, 'WorkoutTracker/WT_log.html', content)

# Story #4: Details page --------------------------------------------


def workout_details(request, pk):
    workout = get_object_or_404(Workout, pk=pk)
    content = {'workout': workout}
    return render(request, 'WorkoutTracker/WT_details.html', content)

# Story #5: Edit and Delete Functions ------------------------------


def workout_update(request, pk):
    workout = get_object_or_404(Workout, pk=pk)
    form = WorkoutForm(data=request.POST or None, instance=workout)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('WT_log')
    content = {'form': form, 'workout': workout}
    return render(request, 'WorkoutTracker/WT_update.html', content)


def workout_delete(request, pk):
    workout = get_object_or_404(Workout, pk=pk)
    if request.method == 'POST':
        workout.delete()
        return redirect('WT_log')
    content = {'workout': workout}
    return render(request, 'WorkoutTracker/WT_delete.html', content)


# Story #6-(BS Pt 1): Setup Beautiful Soup ---------------------------
# Story #7-(API Pt 2): Parse through JSON


def workout_api(request):
    url = "https://weatherapi-com.p.rapidapi.com/current.json"

    querystring = {"q": "40.7,-111.8"}

    headers = {
        "X-RapidAPI-Key": "466348d428msh9ae0638872d331cp12eba3jsn19454232443a",
        "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    print(response.json())

    api_info = json.loads(response.text)
    state = api_info['location']['region']
    city = api_info['location']['name']
    location = str(city + ', ' + state)

    conditions = api_info['current']['condition']['text']

    wind_speed = api_info['current']['wind_mph']
    wind = 'Wind speed: ' + str(wind_speed) + ' mph'

    humidity_perc = api_info['current']['humidity']
    humidity = 'Relative Humidity: ' + str(humidity_perc) + '%'

    temp_int = api_info["current"]["temp_f"]
    temperature = str(api_info["current"]["temp_f"]) + ' \N{DEGREE SIGN}F'

    content = {'location': location, "conditions": conditions, "temperature": temperature,
               "temp_int": temp_int, "wind": wind, "humidity": humidity}

    return render(request, 'WorkoutTracker/WT_api.html', content)

# Story #6-(BS Pt 1): Setup Beautiful Soup ----------------------------------------
# Story #7-(BS Pt 2): Parse through html


def workout_bsoup(request):
    page = requests.get("https://www.cdc.gov/physicalactivity/basics/adults/index.htm")

    soup = BeautifulSoup(page.content, 'html.parser')
    info = soup.find_all("div", class_="cdc-textblock")[0].get_text()
    info2 = soup.find_all("div", "p", class_="cdc-textblock")[2].get_text()
    info3 = soup.find_all("div", "p", class_="cdc-textblock")[3].get_text()

    content = {"info": info, "info2": info2, "info3": info3}

    return render(request, 'WorkoutTracker/WT_bsoup.html', content)


def workout_bsoup2(request):
    html = requests.get("https://www.health.com/fitness/workout-schedule")
    page = BeautifulSoup(html.content, 'html.parser')
    data = page.find_all("ul", class_="comp mntl-sc-block mntl-sc-block-html")[0]
    listItem = []
    for li in data.find_all("li"):
        listItem.append(li.text)

    content = {"data": data, "listItem": listItem}

    return render(request, 'WorkoutTracker/WT_bsoup2.html', content)


def workout_upper(request):
    html = requests.get("https://www.strengthlog.com/exercise-directory/")
    page = BeautifulSoup(html.content, 'html.parser')
    data = page.find_all("ol")[0]
    listItem = []
    for li in data.find_all("li"):
        listItem.append(li.text)

    data1 = page.find_all("ol")[1]
    listItem1 = []
    for li in data1.find_all("li"):
        listItem1.append(li.text)

    data2 = page.find_all("ol")[5]
    listItem2 = []
    for li in data2.find_all("li"):
        listItem2.append(li.text)

    content = {"data": data, "listItem": listItem, "data1": "data1", "listItem1": listItem1,
               "data2": data2, "listItem2": listItem2}

    return render(request, 'WorkoutTracker/WT_upper.html', content)


def workout_lower(request):
    html = requests.get("https://www.strengthlog.com/exercise-directory/")
    page = BeautifulSoup(html.content, 'html.parser')
    data = page.find_all("ol")[4]
    listItem = []
    for li in data.find_all("li"):
        listItem.append(li.text)

    data1 = page.find_all("ol")[6]
    listItem1 = []
    for li in data1.find_all("li"):
        listItem1.append(li.text)

    data2 = page.find_all("ol")[7]
    listItem2 = []
    for li in data2.find_all("li"):
        listItem2.append(li.text)

    content = {"data": data, "listItem": listItem, "data1": "data1", "listItem1": listItem1,
               "data2": data2, "listItem2": listItem2}

    return render(request, 'WorkoutTracker/WT_lower.html', content)



def get_bsoup2():
    # We are doing the same thing as workout_bsoup2() but instead of returning a render, we are returning a dictionary
    html = requests.get("https://www.health.com/fitness/workout-schedule")
    page = BeautifulSoup(html.content, 'html.parser')
    data = page.find_all("ul", class_="comp mntl-sc-block mntl-sc-block-html")[0]
    listItem = []
    for li in data.find_all("li"):
        listItem.append(li.text)

    content = {"fave-schedule": listItem}

    return content


def get_upper():
    # We are doing the same thing as workout_upper() but instead of returning a render, we are returning a dictionary
    html = requests.get("https://www.strengthlog.com/exercise-directory/")
    page = BeautifulSoup(html.content, 'html.parser')
    data = page.find_all("ol")[2]
    listItem = []
    for li in data.find_all("li"):
        listItem.append(li.text)

    content = {"upper-data": listItem}

    return content


def get_lower():
    # We are doing the same thing as workout_lower() but instead of returning a render, we are returning a dictionary
    html = requests.get("https://www.strengthlog.com/exercise-directory/")
    page = BeautifulSoup(html.content, 'html.parser')
    data = page.find_all("ol")[4]
    listItem = []
    for li in data.find_all("li"):
        listItem.append(li.text)

    content = {"lower-data": listItem}

    return content


def workout_save(request):
    data = []
    # We are appending the dictionaries returned from the functions above to a list
    data.append(get_bsoup2())
    data.append(get_upper())
    data.append(get_lower())

    # We are checking if the path to save the JSON exists, if not, we are creating it
    if not os.path.exists('WorkoutTracker/data'):
        os.makedirs('WorkoutTracker/data')
    else:
        pass
    
    # We are checking if the JSON file exists, if not, we are creating it
    if not os.path.exists('WorkoutTracker/data/account_data.json'):
        # We are creating the JSON file and dumping the data into it
        with open('WorkoutTracker/data/account_data.json', 'w') as f:
            json.dump(data, f)
    else:
        # We are opening the JSON file and dumping the data into it, this will
        # overwrite the existing data in the JSON file
        with open('WorkoutTracker/data/account_data.json', 'w') as f:
            json.dump(data, f)

    # We are opening the JSON file and loading the data into a variable
    with open('WorkoutTracker/data/account_data.json') as f:
        data = json.load(f)

        # We are assigning the data from the JSON file to variables
        fave_schedule = data[0]['fave-schedule']
        upper_data = data[1]['upper-data']
        lower_data = data[2]['lower-data']

        # Save the data to the database
        workout_save_db(fave_schedule, upper_data, lower_data)

        print("Data saved to database")

        return workout_saved_db(request)

# Save data to the database
def workout_save_db(schedules, upper, lower):
    # Split the schedules into a list
    for schedule in schedules:
        # Create a new workout object
        workout = WorkoutInformation()
        # Get the current day of the week
        today = datetime.datetime.today().weekday()
        # Parse the day of the week from the list, Monday: Cardio, Tuesday: Upper Body, etc.
        day_of_the_week = schedule.split(':')
        day_of_the_week = day_of_the_week[0]
        # Check if today matches the day of the week, if not,
        # then find the next day of the week that matches and get
        # the date of that day and assign it to the workout object,
        # if today matches the day of the week, then assign today's date to the workout object
        if day_of_the_week == 'Monday':
            if today == 0:
                workout.date = datetime.datetime.today()
            else:
                workout.date = datetime.datetime.today() + datetime.timedelta(days=(7 - today))
        elif day_of_the_week == 'Tuesday':
            if today == 1:
                workout.date = datetime.datetime.today()
            else:
                workout.date = datetime.datetime.today() + datetime.timedelta(days=(8 - today))
        elif day_of_the_week == 'Wednesday':
            if today == 2:
                workout.date = datetime.datetime.today()
            else:
                workout.date = datetime.datetime.today() + datetime.timedelta(days=(9 - today))
        elif day_of_the_week == 'Thursday':
            if today == 3:
                workout.date = datetime.datetime.today()
            else:
                workout.date = datetime.datetime.today() + datetime.timedelta(days=(10 - today))
        elif day_of_the_week == 'Friday':
            if today == 4:
                workout.date = datetime.datetime.today()
            else:
                workout.date = datetime.datetime.today() + datetime.timedelta(days=(11 - today))
        elif day_of_the_week == 'Saturday':
            if today == 5:
                workout.date = datetime.datetime.today()
            else:
                workout.date = datetime.datetime.today() + datetime.timedelta(days=(12 - today))
        elif day_of_the_week == 'Sunday':
            if today == 6:
                workout.date = datetime.datetime.today()
            else:
                workout.date = datetime.datetime.today() + datetime.timedelta(days=(13 - today))
        else:
            workout.date = datetime.datetime.today()
        
        # Assign the type of workout to the property and
        # assign the cardio and cardio duration properties,
        # remove spaces from the beginning of the string only
        workout.type = schedule.split(':')[1]
        workout.type = workout.type.lstrip()
        if 'Cardio' in workout.type:
            workout.cardio = True
            workout.cardio_duration = 15
        else:
            workout.cardio = False
            workout.cardio_duration = 0

        # Check if the workout is or contains upper or lower body,
        # if it is, then assign the description and duration properties to the
        # upper or lower body data
        if 'Upper body' in workout.type:
            # Format the list to remove the brackets and quotes so that the text can be saved to the database
            upper = str(upper)
            upper = upper.replace('[', '')
            upper = upper.replace(']', '')
            upper = upper.replace("'", '')
            upper = upper.replace('"', '')
                
            # Assign the description and duration properties to the upper body data
            workout.description = upper
            workout.duration = 30
        elif 'Lower body' in workout.type:
            # Format the list to remove the brackets and quotes so that the text can be saved to the database
            lower = str(lower)
            lower = lower.replace('[', '')
            lower = lower.replace(']', '')
            lower = lower.replace("'", '')
            lower = lower.replace('"', '')

            # Assign the description and duration properties to the lower body data
            workout.description = lower
            workout.duration = 30
        else:
            workout.description = 'N/A'
            workout.duration = 0

        # Save the workout to the database
        workout.save()


def workout_saved_db(request):
    workout = WorkoutInformation.information.all()
    content = {'workouts': workout}
    return render(request, 'WorkoutTracker/WT_save2.html', content)


def fave_workout(request, pk):
    if request.method == 'POST':
        # Get the item from the database
        item = get_object_or_404(Workout, pk=pk)
        
        # If there is already a favorite for this item, don't create a new one
        if WorkoutFavorites.objects.filter(item=item).exists():
            print("Favorite already exists.")
            return redirect('WT_log')
        # Create a new favorite for the item
        favorite = WorkoutFavorites(item=item)
        # Save the favorite
        favorite.save()

        # Redirect to the favorites page
        favorites = WorkoutFavorites.objects.all()

        # Create a list of the items in the favorites
        item_list = [favorite.item for favorite in favorites]

        # Create a list of the items in the favorites
        content = {'favorites': item_list}

        return render(request, 'WorkoutTracker/WT_faves.html', content)
    else:
        return redirect('WT_log')


def favorite_workouts(request):
    favorites = WorkoutFavorites.objects.all()
    item_list = [favorite.item for favorite in favorites]
    content = {'favorites': item_list}

    return render(request, 'WorkoutTracker/WT_faves.html', content)
