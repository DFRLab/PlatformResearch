# Platform Research

<p>Investigating new platforms as potential research tools</p>

---

# Support

1. All OS systems if using the programming language python.
2. The file platforms.exe is only available for Windows OS.


## Requirements

- Python 3.6 or higher
- Follow `requirenments.txt` if using python.

## Run

1. `git clone https://github.com/DFRLab/PlatformResearch.git`, to download the source code.
2. `cd PlatformResearch`, to enter the directory.
3. `pip3 install -r requirements.txt` or just `pip install -r requirements.txt`, to install the requirements.
4. `python main.py -h`, to know more about the available commands.

## Commands
Command | Description
:--- | :---
\--help / \-h | Show help screen.
\--app / \-a | Specify platform on which the program will collect data.

---

## Note

1. More platforms and analysis tools will be added soon.

---

## Alternative Platforms to Explore:

- Bitchute

---

### Bitchute

<p>BitChute is YouTube-like web application to share video content. According to its website, the platform <i>aims to put creators first and provide them with a service that they can use to flourish and express their ideas freely</i>.</p>

**Features**

- No official or third-party APIs.
- BitChute contains video listings of popular and trending videos, as well as recommended channels on the platform.
- By using Python's Selenium is possible to access BitChute via a web-driver and extract the most recent information, categorized by trending videos, trending tags, popular videos, recommended channels, and all videos featured in the homepage at the moment.
- Although there is a Register/Login buttons, the content is public. There is no need to create an account to watch the videos on BitChute or to extract information using Python's Selenium.
