# Making a CountDown Calculator



import time
from tqdm import tqdm
import cowsay

print("\n\n\n\t\tWelcome to the CountDown Clock.  \n\n")
stopwatch = int(input("For How long You Want To Set CountDown(in seconds):  "))


print() # for extra line in the teminal
with tqdm(total=stopwatch) as pbar:
    for i in range(stopwatch):
        time.sleep(1)
        pbar.update(1)

cowsay.cow(f"{stopwatch} sec are over!!!!\n\n")

print(), print() #for extra line in the teminal

