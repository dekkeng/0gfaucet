import os, pyautogui, pyscreeze
import time
from datetime import datetime
from dotenv import load_dotenv

#pyautogui.PAUSE=0

load_dotenv("config.txt")

class Tor:
    def __init__(self):
        self.tor_tab = self.getPos("tor_tab")
        self.TOR_TIMEOUT = float(os.getenv('TOR_TIMEOUT', 30))
        if self.tor_tab != None:
            self.click(self.tor_tab)
            self.wait(1)
            self.quitTor()

    def updatePos(self):
        #self.log(f'Getting position...')
        self.address_input = self.getPos("address_input")
        self.request_btn = self.getPos("request_btn")
        self.fail = self.getPos("fail")
        self.success = self.getPos("success")
 
    def start(self, addr):
        count = 0
        timeout = time.time() + 60*self.TOR_TIMEOUT
        while True:
            if self.TOR_TIMEOUT != 0 and time.time() > timeout:
                break

            self.updatePos()
            if self.request_btn != None:
                #self.log(f'Request ready')
                if self.address_input != None:
                    #self.log(f'Address input')
                    self.click(self.address_input)
                    self.wait(1)
                    self.key(addr)
                    self.wait(1)
                self.click(self.request_btn)
                self.wait(3)
                
            if self.fail != None:
                self.click(self.fail)
                count = count+1
                if count > 3:
                    self.log('Skipped')
                    break
                self.log(f'Failed, retrying [{count}/3]...')
                self.refreshTor()
            
            if self.success != None:
                self.click(self.success)
                self.log(f'Success')
                break

            self.wait(5)

    def getPos(self, file, conf = 0.95):
        try:
            return pyscreeze.locateCenterOnScreen('./sample/'+file+'.png', confidence = conf)
        except Exception as e:
            return None

    def getAllPos(self, file, conf = 0.7):
        return pyscreeze.locateAllOnScreen('./sample/'+file+'.png', confidence = conf)

    def refreshTor(self):        
        self.log('Refresh Tor')
        pyautogui.keyDown('Ctrl')
        pyautogui.keyDown('Shift')
        pyautogui.keyDown('L')
        pyautogui.keyUp('L')
        pyautogui.keyUp('Ctrl')
        pyautogui.keyUp('Shift')
        self.wait(5)

    def quitTor(self):        
        self.log('Quit Tor')
        pyautogui.hotkey('alt', 'f4')

    def key(self, msg):
        self.log(f'Key {msg}')
        pyautogui.typewrite(msg)

    def wait(self, length = 0.01):
        time.sleep(length)
    def move(self, pos):
        pyautogui.moveTo(pos, duration=0.01)

    def drag(self, pos1, pos2):
        pyautogui.mouseDown(pos1, duration=0.01)
        pyautogui.dragTo(pos2, duration=0.2)
        pyautogui.mouseUp(pos2, duration=0.01)
        
    def click(self, pos):
        self.move(pos)
        pyautogui.click([pos[0], pos[1]])
        
    def log(self, msg):
        """Msg log"""
        t = datetime.now().strftime('%H:%M:%S')
        print(f'[{t}] MESSAGE: {msg}')

time.sleep(3)

def main():    
    tor = Tor()
    
    START_ADDR = int(os.getenv('START_ADDR', 1))
    TOR_PATH = os.getenv('TOR_PATH', 'C:/Users/WIN/Desktop/Tor Browser/Browser/firefox.exe')
    os.startfile(TOR_PATH)
    time.sleep(5) 
    
    try:
        f = open("addrs.txt", "r")
        lines = f.readlines()
        count = 0
        total = len(lines)

        if START_ADDR > 1:
            tor.log(f'Continue from address {START_ADDR}')

        for addr in lines:
            count = count+1
            if count < START_ADDR:
                continue
            addr = addr.replace("\n", "")
            tor.log(f'[{count}/{total}] Getting faucet of account={addr}...')
            tor.start(addr)
            tor.refreshTor()
        tor.quitTor()
    except Exception as e:
        tor.log(e)
        pass

main()