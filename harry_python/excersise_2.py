import time

hour = int(time.strftime("%H"))

if hour>=5 and hour<12:
    print("Good Morning")
elif hour>=12 and hour<17:
    print("Good Afternoon")
elif hour>=17 and hour< 21:
    print("Good Evening")
else:
    print("Good Night")