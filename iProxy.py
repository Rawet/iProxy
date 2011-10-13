#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# iProxy
# Written by Dennis Rawet
# 2011

import urllib2
import httplib
import socket
import array

# File with proxies
file = "proxies.txt"

#Filename witch stores the working proxies, please add .txt
filename = "working.txt"


#Witch site you should "ping"
testsite = 'www.google.se'

# Seconds untill times out. 20(sec) is default
timeouttime = 10


# End of String-settings

def proxier(pip):
	try:
		testsite2 = "http://%s" % (testsite)
		proxy_handler = urllib2.ProxyHandler({'http': pip})
		opener = urllib2.build_opener(proxy_handler)
		opener.addheaders = [('User-agent', 'Mozilla/5.0')]
		urllib2.install_opener(opener)
		req=urllib2.Request(testsite2)
		sock=urllib2.urlopen(req)
		
		connect = httplib.HTTPConnection(testsite)
		connect.request("HEAD", "/")
		r1 = connect.getresponse()
		if r1.reason == "OK":
			print "%s works - Added to %s" % (pip, filename)
			
			try:
				file = open(filename, 'a')
				file.write("%s" % (pip))
				file.close()
			except IOError:
				print "Could not append to file!"
			
			
			
	except urllib2.HTTPError as e:
		print 'Error code: ', e.code
		return e.code
	except Exception as detail:
		print "Error: Timeout"
		return False		
def main():
	socket.setdefaulttimeout(timeouttime)
	
	proxyarray=[]
	
	for line in open(file, 'r').readlines():
		proxyarray.append((line))
	i = 1
	for currentProxy in proxyarray:
		print i,'. '
		proxier(currentProxy)
		i= i + 1
	
			
if __name__ == '__main__':
	main()
