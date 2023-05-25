# Ubuntu-Modification-and-Improvement

In comparison to other operating systems generally, Ubuntu is not very user pleasant. In order to increase productivity, keeping users informed, and helping them understand their system, we intend to offer additional functionalities.

## Objective and Features

The lack of GUI in Ubuntu, and update notifications are quite obvious. Hence we are planning to implement the following:

- System stats - (CPU and memory information, RAM usage information)
- New Unread Mail Notifier
- Automatic Meet Join

The detailed explanation of the features and their implementation methodologies are listed below.

### System Stats

This feature will provide us with details regarding the memory usage of the system along with the CPU usage. Along with a live line graph depicting the current CPU & RAM usage.
The GUI hence serves the purpose of making the information available to users without much technical knowledge of the commands.

Methodology:

- Using shell scripts, the data about memory and CPU is extracted using grep command
- The front end python tkinter program calls the respective shell script according to the button clicked
- This data is then read by the front end python tkinter script and displayed on the screen
- The data is extracted continuously in a loop and displayed on the window with the help of MATPLOTLIB
- The funcanimation function in MATPLOTLIB is used to call the required function again and again to generate the animation.

### Automatic Meet Join

In many situations, we might need to join a google meet on a regular basis. While a possible solution is to keep all such meet links in one place, it’s still fairly tedious. Hence, this feature would be implemented such that the user can enter their meet joining time and days of the week the meeting is held on.

Methodology:

- A GUI has been developed where the user can enter their meeting details (meetgui.py)
- Another script is written in python which uses web scraping to join a particular meet whenever it is called
- A cron job is set up for each meeting based on the user input. It executes the python scripts to enable automatic joining.

### New Unread Mail Notifier

A mail notifier would notify the user about any new mail within a minute of its arrival. Hence the user can focus on work without worrying about missing out on any mail, thus increasing productivity.

Methodology:

There are mainly 2 scripts which are integrated with CRON Jobs. These scripts are:

- Mail scraper: Extracts the latest unread mail data from gmail entered and stores it in JSON Format
- Notif script: Checks the value of date in JSON file periodically and whenever there is a difference (indicating a new mail), sends a notification to the user mentioning the mail data.
