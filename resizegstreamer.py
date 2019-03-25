'''I figured it out, and it can be done by adding a video-filter element. the code to add is the following:'''

VideoCrop = Gst.ElementFactory.make('videocrop', 'VideoCrop')
VideoCrop.set_property('top', 100)
VideoCrop.set_property('bottom', 100)
VideoCrop.set_property('left', 50)
VideoCrop.set_property('right', 150)
player.set_property('video-filter', VideoCrop)

'''and below id the entire source code, tested on both linux and Windows'''

import os, sys
import Tkinter as tkinter

import gi
gi.require_version('Gst', '1.0')
gi.require_version('GstVideo', '1.0')
gi.require_version('GdkX11', '3.0')
from gi.repository import Gst, GObject, GdkX11, GstVideo

def set_frame_handle(bus, message, frame_id):
    if not message.get_structure() is None:
        print message.get_structure().get_name()
        if message.get_structure().get_name() == 'prepare-window-handle':
            display_frame = message.src
            display_frame.set_property('force-aspect-ratio', True)
            display_frame.set_window_handle(frame_id)

window = tkinter.Tk()
window.title('')
window.geometry('500x400')

GObject.threads_init()
Gst.init(None)

# can aslo use display_frame = tkinter.Frame(window)
display_frame = tkinter.Canvas(window, bg='#030')

display_frame.pack(side=tkinter.TOP,expand=tkinter.YES,fill=tkinter.BOTH)
frame_id = display_frame.winfo_id()

player = Gst.ElementFactory.make('playbin', None)

filepath = os.path.realpath('kbps.mp4')
filepath2 = "file:///" + filepath.replace('\\', '/').replace(':', '|')
player.set_property('uri', filepath2)