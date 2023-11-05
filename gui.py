from tkinter import *
from tkinter import ttk
from scraper import Scraper
import asyncio
import threading

root = Tk()
root.title("Film Review Visualizer")
root.geometry("500x500")

mainFrame = ttk.Frame(root, padding="10 10 10 10")
inputFrame = ttk.Frame(mainFrame, padding="10 10 10 10")

label = ttk.Label(inputFrame, text="Enter the name of a film.", font="TkHeadingFont")
loadingLabel = ttk.Label( anchor = CENTER )

filmTitle = StringVar()
titleInput = ttk.Entry(inputFrame, textvariable=filmTitle)

# lambda because we want to call the function instead of passing it as callable
# i.e. the scrape only runs after pressing the button
submitButton = ttk.Button(inputFrame, text="Go", command = lambda: scrape())

mainFrame.grid(column=0, row=0, sticky=(N, W, E, S))
inputFrame.grid(column=0, row=0, sticky=(N, W, E, S))
label.grid(column=0, row=1, padx=5, pady=5, sticky=(E, W))

loadingLabel.grid(column = 0, row = 2, pady = 5, padx = 5, sticky = (E, W))

titleInput.grid(column=0, row=3, padx=5, pady=5, sticky=(E, W))
submitButton.grid(column=0, row=4, padx=5, pady=5, sticky=(E, W))


root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
mainFrame.columnconfigure(0, weight=1)
mainFrame.rowconfigure(0, weight=1)
inputFrame.columnconfigure(0, weight=1)
inputFrame.rowconfigure(0, weight=1)
inputFrame.rowconfigure(1, weight=1)
inputFrame.rowconfigure(2, weight=1)
inputFrame.rowconfigure(3, weight=1)

# make the loading gif invisible first
loadingLabel.grid_remove()

# multithreading and async stuff to not block the gui while scraper is running
def scrape():
    threading.Thread(target = run_async_scraper, daemon=True).start()
    loadingLabel.grid()

def run_async_scraper():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(async_scraper())
    loop.close()

async def async_scraper():
    scraper = Scraper(filmTitle.get())
    scraper.scrape()
    # here is the critic_responses array
    print(scraper.critic_responses)
    loadingLabel.grid_remove()

# stuff for gif
frame_list = []
frame_index = 0
last_frame = 0

while True:
    try:
        part = f'gif -index {frame_index}'
        frame = PhotoImage(file = './loadingSMALL.gif', format = part)
    except:
        last_frame = frame_index - 1
        break
    frame_list.append(frame)
    frame_index += 1

def animate_frames(frame_number = 0 ):
    if frame_number > last_frame:
        frame_number = 0
    loadingLabel.config(image = frame_list[frame_number])
    root.after(100, animate_frames, frame_number + 1) 
    
animate_frames()
root.mainloop()