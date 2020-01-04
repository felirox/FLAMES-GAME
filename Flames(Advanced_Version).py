from sys import platform
import os
from os import system as s
from gtts import gTTS 
from colorama import init, Fore, Back, Style
init()
from termcolor import colored
from time import sleep
import pygame as pg
import time as t

language='en'

def clear():
	if (platform=="linux" or platform=="linux2"):
		s("clear")
	elif (platform=="win32"):
		s("cls")

def colour(str = "",color = "red"):
	print (colored(str,color),end = "")

#alpha = list(string.ascii_uppercase)
def play_sound(music_file, volume=0.8):
    '''
    stream music with mixer.music module in a blocking manner
    this will stream the sound from disk while playing
    '''
    # set up the mixer
    freq = 25000   # audio CD quality, basically the speed in which the audio is played
    bitsize = -16    # unsigned 16 bit
    channels = 2     # 1 is mono, 2 is stereo
    buffer = 2500    # number of samples (experiment to get best sound)
    pg.mixer.init(freq, bitsize, channels, buffer,)
    # volume value 0.0 to 1.0
    pg.mixer.music.set_volume(volume)
    clock = pg.time.Clock()
    try:
        pg.mixer.music.load(music_file)
        print("Music file {} loaded!".format(music_file))
    except pg.error:
        print("File {} not found! ({})".format(music_file, pg.get_error()))
        return
    pg.mixer.music.play()
    while pg.mixer.music.get_busy():
        # check if playback has finished
        clock.tick(300)
	
clear()

name1 = input("\nEnter the first name : ").upper()
name2 = input("\n\nEnter the second name : ").upper()
introd='Welcome to the game '+name1+' and '+name2+' Hope you enjoy it.'
myobj = gTTS(text=introd, lang=language, slow=False)
myobj.save("welcome.mp3") 
play_sound('welcome.mp3')


list1 = [i for i in name1]
list2 = [i for i in name2]

l1,l2 = list1,list2
f1_list = []; f2_list = []

if (name1.find(' ')==-1):
	pass
else:
	l1[l1.index(' ')] = "-"

if (name2.find(' ')==-1):
	pass
else:
	l2[l2.index(' ')] = "-"

print (l1)
print (l2)

for i in range(len(l1)):
	for j in range(len(l2)):
		if (l1[i]==l2[j]):
			##################################### F1 COUNT ################################
			if (l1.count(l1[i]) >= 1):
				k=l1[i]
				for m in range(len(l1)):
					#print ("i : ",i," ",end="")
					#print ([m], end = "")
					if (l1[m])=="-":
						pass
					else:
						if (l1[m]==k):
							f1_list.append(m)
							#print (m)
							l1[m] = "-"
			else:
				f1_list.append(i)
			##################################### F2 COUNT ################################
			if (l2.count(l2[j]) >= 1):
				p=l2[j]
				for m in range(len(l2)):
					if (l2[m])=="-":
						pass
					else:
						if (l2[m]==p):
							f2_list.append(m)
							l2[m] = "-"
			else:
				f2_list.append(j)
			################################### NO MATCHES ################################
		else:
			pass

f1_list.sort()
f2_list.sort()

print ("\n\n")
print (l1)
print (l2)
print (f1_list)
print (f2_list)
final_count=0
for i in range(len(l1)):
	if l1[i]!="-":
		final_count+=1
for i in range(len(l2)):
	if l2[i]!="-":
		final_count+=1
print ("\n\nFinal Count : ",final_count)



F="FLAMES"
FLAMES=[i for i in F]
copy=[]
copy1=[]
i=len(FLAMES)
k=(final_count%len(FLAMES))
if k==0:
	k=len(FLAMES)-1
else:
	k-=1
print ("=============================>Temp FLAMES is : ",FLAMES)

while i!=1:
	print ("\n\tk is : ",k)
	print ("Element pop is : ",FLAMES[k])
	FLAMES.pop(k)
	print ("\t\tNew Length of FLAMES : ",len(FLAMES))
	if k==len(FLAMES) or k==0:
		z=0
		while len(copy)!=len(FLAMES):
			copy+=FLAMES[z]
			z+=1
		FLAMES+=copy
	else:
		k1=k
		k2=0
		print ("\t\t\tNew k is : ",k)
		p=FLAMES.index(FLAMES[-1])
		print ("->p is :",p,"\tElement at p : ",FLAMES[p])
		while len(copy)!=p:
			copy.append(FLAMES[k1])
			print ("Copy is : ",copy,"\tk1 is : ",k1)
			if copy[-1]==FLAMES[p]:
				break
			else:
				k1+=1
		print("\n")
		p1=FLAMES.index(FLAMES[k])
		print ("->p1 is : ",p1,"\tElement at p1 : ",FLAMES[p1])
		while len(copy1)!=p1:
			copy1.append(FLAMES[k2])
			print ("Copy1 is : ",copy1,"\tk2 is : ",k2)
			if copy1[-1]==FLAMES[p1]:
				break
			else:
				k2+=1
	FLAMES=[]
	FLAMES=copy+copy1
	print ("=============================>Temp FLAMES is : ",FLAMES)
	print ("\t\tLength of FLAMES : ",len(FLAMES))
	copy=[];copy1=[]
	k=(final_count%len(FLAMES))
	if k==0:
		k=len(FLAMES)-1
	else:
		k-=1
	i=len(FLAMES)

print ("\n\n\t\t\t\t\tFINAL FLAMES : ",FLAMES)

print ("\n\n\n\t\t\t\t\tHi, %s and %s!! Your results are below : "%(name1,name2))

if FLAMES[0]=="F":
	print ("\n\n\n\t\t\t\t\t\t\tYou both are FRIENDS!! :) \n\n\n\n\n\n\n\n")
	restext = 'You both are Friends'
	myobj = gTTS(text=restext, lang=language, slow=False)
	myobj.save("result.mp3")
elif FLAMES[0]=="L":
	print ("\n\n\n\t\t\t\t\t\t\tYou both are LOVERS!! ♥‿♥ \n\n\n\n\n\n\n\n")
	restext = 'You both are Lovers uwu'
	myobj = gTTS(text=restext, lang=language, slow=False)
	myobj.save("result.mp3") 
elif FLAMES[0]=="A":
	print ("\n\n\n\t\t\t\t\t\t\tYou both have an AFFAIR!! 😈 \n\n\n\n\n\n\n\n")
	restext = 'You both have an affair nice'
	myobj = gTTS(text=restext, lang=language, slow=False)
	myobj.save("result.mp3") 
elif FLAMES[0]=="M":
	print ("\n\n\n\t\t\t\t\t\t\tYou both will MARRY!! :O \n\n\n\n\n\n\n\n")
	restext = 'Congrats, you will marry each other'
	myobj = gTTS(text=restext, lang=language, slow=False)
	myobj.save("result.mp3") 
elif FLAMES[0]=="E":
	print ("\n\n\n\t\t\t\t\t\t\tYou both are ENEMIES!! :( \n\n\n\n\n\n\n\n")
	restext = 'You both are enemies. Hurry, grab a sword'
	myobj = gTTS(text=restext, lang=language, slow=False)
	myobj.save("result.mp3") 
elif FLAMES[0]=="S":
	print ("\n\n\n\t\t\t\t\t\t\tYou both are SIBLINGS!! \n\n\n\n\n\n\n\n")
	restext = 'You both are Siblings. No incest wink wink'
	myobj = gTTS(text=restext, lang=language, slow=False)
	myobj.save("result.mp3") 

play_sound('result.mp3')
t.sleep(3)
os.remove('welcome.mp3')
os.remove('result.mp3')