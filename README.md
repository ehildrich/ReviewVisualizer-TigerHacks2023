# ReelEyes ReviewVisualizer-TigerHacks2023

## About the Project

This project is our submission to University of Missouri's TigerHacks 2023 event. The project scrapes movie review text from critics' reviews on Rotten Tomatoes for a given movie title and returns two visualizations.

1. A word cloud of the significant words in the movie reviews
2. A bar plot of the 15 most frequently used, significant words in the critics' reviews

### Built With

The entire project was built in Python. The particular packages used in each section will be listed below.

#### Front-End
- tkinter

#### Back-End
- Beautifulsoup
- requests
- selenium
- pandas
- matplotlib.pyplot
- wordcloud (see Acknowledgements)

## Getting Started

### Prerequisites

1. Install Python: [https://www.python.org/downloads/](https://www.python.org/downloads/)
2. Install Python dependencies:
   ```
   pip install beautifulsoup4
   pip install requests
   pip install -U selenium
   pip install pandas
   pip install -U matplotlib
   pip install wordcloud
   ```

### Installation

1. Clone Github repository:
   ```
   git clone https://github.com/ehildrich/ReviewVisualizer-Tigerhacks2023
   ```
2. Open `gui.py` and run in Python editor.
3. Type a movie title into the text field and click the "Go" button. 

## Usage

## Contact
- Dottie Hildrich: ehlidrich
- Roshan Thapa Magar: rosnMagar
- Rebecca Rushman: rrushman02
- Beamlak Tekle: 

## Acknowledgements
The wordcloud Python package was developed by Github user amueller and is available [here](amueller.github.io/word_cloud)
