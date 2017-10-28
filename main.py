import os
import glob
from time import sleep
from selenium import webdriver
import guitarpro
import keyboard
a = webdriver.Chrome()
path1 = 'C:/Users/anant/Downloads/'
path2 = 'C:/Users/anant/Desktop/to MIDI/'
sng = input("Enter name of song: ")
ars = input("Enter name of artist: ")
print("Searching the WORLD WIDE WEB for the SONG...")
a.get('http://www.songsterr.com/a/wa/bestMatchForQueryString?s='+sng+'&a='+ars)
b = a.find_element_by_class_name('new-revision-button')
b.click()
print("Song Found!!!")
print("Processing...")
c = a.find_element_by_class_name('inputText')
d = a.find_element_by_class_name('inputPassword')
c.send_keys('shwetankshrey@gmail.com')
d.send_keys('womenwhocode')
e = a.find_element_by_class_name('submit-button')
e.submit()
print("Downloading Song...")
f = a.find_elements_by_xpath("//*[contains(text(), '.gp')]")[0]
f.click()
fn = f.text
sleep(5)
print("Song downloaded!!!")
g = guitarpro.parse(path1+fn)
print("Splitting song into different instruments...")
h = g.tracks
j = 0
for i in h:
	j+=1
	g.tracks = [i]
	guitarpro.write(g, path1+'track'+str(j)+'.gp5')
i = 0
print("Acquiring sheet music of individual instruments...")
while i <= j:
	i += 1
	a.get('http://tabplayer.online')
	b = a.find_element_by_id('browser')
	b.click()
	sleep(2)
	keyboard.write(path1+'track'+str(i)+'.gp5')
	keyboard.press_and_release('enter')
	sleep(10)
	c = a.find_element_by_class_name('downloader-mid')
	c.click()
	print("Split and acquired notes of " + str(i) + " out of " + str(j) + " songs.")
	sleep(10)
sleep(30)
print("Converting sheet music into mp3 files...")
i = 0
while i <= j:
	list_of_files = glob.glob(path1+'*')
	fn = max(list_of_files, key=os.path.getctime)
	a.get('https://www.conversion-tool.com/midi')
	b = a.find_element_by_id('localfile')
	b.send_keys(fn)
	sleep(10)
	c = a.find_element_by_id('calcbuttonSimple')
	c.click()
	sleep(30)
	d = a.find_element_by_class_name('alert-link')
	d.click()
	os.remove(fn)
	print("Downloading mp3 of " + str(i) + " out of "+ str(j) + " songs.")
print("Thanks for using Destruction of Symphony.")
sleep(0.3)
print(".")
sleep(0.3)
print(".")
sleep(0.3)
print(".")
print("A sasta jugaad by sNeAkY sNeKs.. ;)")