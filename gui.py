from tkinter import *
from tkinter import ttk
from scraper import Scraper
import visualizer
import asyncio
import threading


# multithreading and async stuff to not block the gui while scraper is running
def scrape():
    threading.Thread(target = run_async_scraper, daemon=True).start()
    print("async process started") 

def run_async_scraper():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(async_scraper())
    loop.close()

async def async_scraper():
    if filmTitle.get() != "": 
        scraper = Scraper(filmTitle.get())
        scraper.scrape()
        visualizer.review_visuals(scraper.critic_responses, scraper.movie_name)

root = Tk()
root.title("Film Review Visualizer")

mainFrame = ttk.Frame(root, padding="10 10 10 10")

logoImage = PhotoImage(file="ReelEyesLogo.png").subsample(6, 6)
logo = ttk.Label(mainFrame, text="placeholder", image=logoImage)

label = ttk.Label(mainFrame, text="Enter the name of a film.", font="TkHeadingFont")

filmTitle = StringVar()
titleInput = ttk.Entry(mainFrame, textvariable=filmTitle)

# lambda because we want to call the function instead of passing it as callable
# i.e. the scrape only runs after pressing the button
submitButton = ttk.Button(mainFrame, text="Go", command = lambda: scrape())

imageFrame = ttk.LabelFrame(mainFrame, text="Output", width=600, height=500, borderwidth=5)

graphButton = ttk.Button(mainFrame, text="Graph")
cloudButton = ttk.Button(mainFrame, text="Cloud")


mainFrame.grid(column=0, row=0, sticky=(N, W, E, S))
logo.grid(column=0, row=0, columnspan=2, rowspan=3)
label.grid(column=2, row=0, columnspan=2, padx=5, pady=5, sticky=(E, W))
titleInput.grid(column=2, row=1, columnspan=2, padx=5, pady=5, sticky=(E, W))
submitButton.grid(column=2, row=2, columnspan=2, padx=5, pady=5, sticky=(E, W))
imageFrame.grid(column=0, row=3, columnspan=4)
graphButton.grid(column=2, row=4)
cloudButton.grid(column=3, row=4)


root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
mainFrame.columnconfigure(0, weight=1)
mainFrame.columnconfigure(1, weight=1)
mainFrame.columnconfigure(2, weight=1)
mainFrame.columnconfigure(3, weight=1)
mainFrame.rowconfigure(0, weight=1)
mainFrame.rowconfigure(1, weight=1)
mainFrame.rowconfigure(2, weight=1)
mainFrame.rowconfigure(3, weight=1)
mainFrame.rowconfigure(4, weight=1)


root.mainloop()