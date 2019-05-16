import win32serviceutil
import win32service
import win32event
import servicemanager
import socket
import time
import logging
import subprocess 
import sys


logging.basicConfig(
    filename = 'C:\\Users\\Akshay\\Desktop\\service\\awarenessservice.log',
    level = logging.DEBUG, 
    format = '[helloworld-service] %(levelname)-7.7s %(message)s'
)

class HelloWorldSvc (win32serviceutil.ServiceFramework):
    _svc_name_ = "AWARENESS"
    _svc_display_name_ = "AWARENESS SERVICE"
    
    def __init__(self,args):
        win32serviceutil.ServiceFramework.__init__(self,args)
        self.stop_event = win32event.CreateEvent(None,0,0,None)
        socket.setdefaulttimeout(60)
        self.stop_requested = False
    
    def SvcStop(self):
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        win32event.SetEvent(self.stop_event)
        logging.info('Stopping service ...')
        self.stop_requested = True
    
    def SvcDoRun(self):
        self.ReportServiceStatus(win32service.SERVICE_RUNNING)
        win32event.WaitForSingleObject(self.hWaitStop, win32event.INFINITE)
        servicemanager.LogMsg(
            servicemanager.EVENTLOG_INFORMATION_TYPE,
            servicemanager.PYS_SERVICE_STARTED,
            (self._svc_name_,'')
        )
        
        while 1:
              self.main()
    
    def main(self):
        logging.info(' ** Hello Awareness World ** ')
        # Simulate a main loop
        

if __name__ == '__main__':
    if len(sys.argv) == 1:
         servicemanager.Initialize()
         servicemanager.PrepareToHostSingle(HelloWorldSvc)
         servicemanager.StartServiceCtrlDispatcher()
    else:
         sys.frozen="windows_exe"
         win32serviceutil.HandleCommandLine(HelloWorldSvc)