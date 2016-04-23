from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice
import time
import os
import subprocess as sp

wdir = '/dev/shm/'
spref = 'swipelicious-'

imgraw = wdir + spref + 'raw.png'
cooraw = wdir + spref + 'coord.txt'

def get_coords(img):
	img.writeToFile(imgraw, 'png')
	print 'shot taken'

	sp.call(['./vision.py', imgraw, cooraw])
	f = open(cooraw, 'r')
	ax, ay = [int(x) for x in f.readline().split()]
	bx, by = [int(x) for x in f.readline().split()]
	f.close()

	print ax, ay
	print bx, by
	return ax, ay, bx, by

def reload(device):
	time.sleep(1.5)
	img = device.takeSnapshot()
	return get_coords(img)

if __name__ == '__main__':
	device = MonkeyRunner.waitForConnection()
	device.drag((0,0), (1,1), duration, steps)

	while True:
		cmd = raw_input('State thy command: ')
		if cmd == '1':
			for i in range(0, 10):
				ax, ay, bx, by = reload(device)
				device.drag((bx,by), (ax,ay), duration, steps)
			ax, ay, bx, by = reload(device)
		elif cmd == '2':
			device.drag((bx,by), (bx,ay), duration, steps)
			ax, ay, bx, by = reload(device)
