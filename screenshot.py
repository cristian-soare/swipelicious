#!/usr/bin/python2

import gtk.gdk
import time

def screenshot():
	w = gtk.gdk.get_default_root_window()
	sz = w.get_size()
	pb = gtk.gdk.Pixbuf(gtk.gdk.COLORSPACE_RGB,False,8,350,660)
	pb = pb.get_from_drawable(w,w.get_colormap(),100,100,0,0,350,660)

	if (pb != None):
	    pb.save("screenshot.png","png")

if __name__ == '__main__':
	screenshot()
	print "screenshot taken"
