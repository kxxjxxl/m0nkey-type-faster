# m0nkey-type-faster

in a world where you can automate everything, automate typing faster because that is very helpful to develop your typing skills (the part where you type a script to type faster) 

## Requirements

this bot requires the following Python packages:

- selenium
- pynput

you can install these packages using pip:

```bash
pip install selenium pynput
```


## Requirements
First, replace the value of chrome_driver_path in the monkey_type_bot function call with the path to your ChromeDriver.

Then, simply run the Python script (why are you even reading this repo if you do not know how to run a python script lmaoo):
```bash
python fast.py
```
by default, the bot will type 1000 words and then stop. you can change this by providing a different value for max_words when calling monkey_type_bot.

the speed at which the bot types words can be adjusted using the delay parameter. by default, it waits 0.00075 seconds between each action. you can make the bot type faster by decreasing this value, or slower by increasing it.

## Note

this bot is not for educational purposes only. dont use it responsibly, just type away
