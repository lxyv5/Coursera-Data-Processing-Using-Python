# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 12:35:16 2017

@author: Xinyu Li
"""

# Filename: helloworld.py
import wx 
class Frame1(wx.Frame):
 def __init__(self,superior):
        wx.Frame.__init__(self, parent = superior, title = "Example", pos= (100,200), size= (200,100))
        panel = wx.Panel(self)
        text1= wx.TextCtrl(panel, value = "Hello, World!", size = (200,100))
if __name__ == '__main__': 
    app =wx.App()
    frame = Frame1(None)
    frame.Show(True)
    app.MainLoop() 