import pyautogui
import random
import time


def random_duration(min_value, max_value):
  return int(random.uniform(min_value, max_value))

def Sleep (t):
  time.sleep(float(t))

def twoM_delay ():
    print("\t\t[READING DELAY] \"Reading\" delay started. Waiting for 2 minutes...")
    pyautogui.scroll(10)
    Sleep(30) 
    pyautogui.scroll(-15)
    Sleep(30) # 1min
    pyautogui.scroll(30)
    Sleep(30)
    pyautogui.scroll(-40)
    Sleep(30) # 2 minutes done

print("\t\t\t\t[START EVENT]\n\t\t\t\t Waiting 2.5 seconds for user to tab into correct window")
Sleep(2.5)

scroll_clicks = 50

while True:
  # Scroll up for a random duration
  scroll_duration = random_duration(2, 15)
  print(f"[MOUSE] Scrolling up for {scroll_duration} seconds...")
  start_time = time.time()
  while time.time() - start_time < scroll_duration:
    pyautogui.scroll(scroll_clicks)  # Positive value scrolls up
    Sleep(0.1)  # Adjust sleep time for desired scroll speed

  # Delay for a random duration
  delay_duration = random_duration(2, 15)
  print(f"\t[DELAY] Waiting {delay_duration} seconds...")
  Sleep(delay_duration)

  # Scroll down for a random duration
  scroll_duration = random_duration(2, 15)
  print(f"[MOUSE] Scrolling down for {scroll_duration} seconds...")
  start_time = time.time()
  while time.time() - start_time < scroll_duration:
    pyautogui.scroll(-scroll_clicks)  # Negative value scrolls down
    Sleep(0.1)  # Adjust sleep time for desired scroll speed

  # Delay for a random duration
  delay_duration = random_duration(2, 15)
  print(f"\t[DELAY] Waiting {delay_duration} seconds...")
  Sleep(delay_duration)

  if (int(random_duration(1, 10)) == 2): # 1 in 3 chance to delay for a couple minutes "reading"
    twoM_delay()
