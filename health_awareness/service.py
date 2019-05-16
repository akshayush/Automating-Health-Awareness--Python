import time
import pyglet
import win32api
import sys
import os
from check import *
import socket

import win32serviceutil

import servicemanager
import win32event
import win32service

print(os.path.abspath(os.getcwd()))

start_time=time.time()
time_out=10 ##seconds
time_for_exercise_win=0.8
#test()
#lets_start(time_out,start_time,time_for_exercise_win)



class SMWinservice(win32serviceutil.ServiceFramework):
    '''Base class to create winservice in Python'''

    _svc_name_ = 'awarenessservice'
    _svc_display_name_ = 'Python Service'
    _svc_description_ = 'Python Service Description'

    @classmethod
    def parse_command_line(cls):
        '''
        ClassMethod to parse the command line
        '''
        win32serviceutil.HandleCommandLine(cls)

    def __init__(self, args):
        '''
        Constructor of the winservice
        '''
        print('i am in init')
        win32serviceutil.ServiceFramework.__init__(self, args)
        self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)
        socket.setdefaulttimeout(60)


    def SvcStop(self):
        '''
        Called when the service is asked to stop
        '''
        #
        self.stopping=True
        #self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        #win32event.SetEvent(self.hWaitStop)

    def SvcDoRun(self):
        '''
        Called when the service is asked to start
        '''
        print('i m running')
        self.start()
        print('i m run')
        servicemanager.LogMsg(servicemanager.EVENTLOG_INFORMATION_TYPE,
                              servicemanager.PYS_SERVICE_STARTED,
                              (self._svc_name_, ''))
        print("My code is here")

# entry point of the module: copy and paste into the new module
# ensuring you are calling the "parse_command_line" of the new created class
if __name__ == '__main__':
    SMWinservice.parse_command_line()
