# Alarm Clock in Python

## Description
This is a simple alarm clock script written in Python. It allows users to set a specific time for the alarm to go off, and once the set time has passed, it plays an alarm sound (a `.mp3` file). The script also provides a countdown of time remaining until the alarm sounds.

## Features
- Set the alarm time in hours, minutes, and seconds.
- Countdown timer that shows time remaining until the alarm.
- Plays an alarm sound when the countdown reaches zero.

## Requirements
- Python 3.x.
- The `playsound` library to play the alarm sound. Install it using the following command:

   ```bash
   pip install playsound
   ```

- An audio file named `alarm.mp3` in the same directory as the script.

## Installation

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/Daniel-Abiy/alarm-clock
   ```

2. Navigate to the project folder:

   ```bash
   cd alarm-clock
   ```

3. Install the required library:

   ```bash
   pip install playsound
   ```

4. Place your desired alarm sound in the project folder and name it `alarm.mp3`.

5. Run the alarm clock script:

   ```bash
   python alarm_clock.py
   ```

## How to Use
1. Enter the amount of hours, minutes, and seconds for the alarm time when prompted.
2. The script will begin counting down and display the time remaining until the alarm.
3. Once the countdown reaches zero, the alarm sound will play.

## Example

```
The amount of hours: 0
The amount of minute: 1
The amount of seconds: 30
The Alarm will sound in:00:01:29
...
The Alarm will sound in:00:00:00
(plays alarm sound)
```

## Contributing
Feel free to fork the project, make improvements, and submit pull requests.

## License
This project is open-source and available under the MIT License.
