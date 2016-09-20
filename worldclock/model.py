from time import sleep
from datetime import datetime
from pytz import timezone

class WorldClock:

    def __init__(self):
        self.initMap()

    def initMap(self):
        self.worldmap = []
        self.worldmap.append('                *****  **********      *  *             **')
        self.worldmap.append('          **** * ** *    *******                    *  ***********  *')
        self.worldmap.append('******************* **    **    **      ** ** *******************************')
        self.worldmap.append('  ***  **********   ***                 * **************************    *')
        self.worldmap.append('         ****************           *********************************')
        self.worldmap.append('          ************             ***** **   ********************* *')
        self.worldmap.append('          **********                 **      ******************* * *')
        self.worldmap.append('            ****                   *****************************')
        self.worldmap.append('               **                 ************ ****  **** *****')
        self.worldmap.append('                 **              ************* *      *    **')
        self.worldmap.append('                    ****           *************                *')
        self.worldmap.append('                   *******             ***** *              * ***')
        self.worldmap.append('                    *********           ******               *      **')
        self.worldmap.append('                    ********            ******                    * *')
        self.worldmap.append('                      ******            *****  *              ********')
        self.worldmap.append('                     ****                ***                  *********')
        self.worldmap.append('                     ****                                           **     *')
        self.worldmap.append('                     **                                                   *')
        self.worldmap.append('                     *')

    def getCopenhagenTime(self):
        return datetime.now(tz=timezone('Europe/Copenhagen')).strftime('%a, %H:%M')

    def getTokyoTime(self):
        return datetime.now(tz=timezone('Asia/Tokyo')).strftime('%a, %H:%M')        

    def getNewYorkTime(self):
        return datetime.now(tz=timezone('US/Eastern')).strftime('%a, %H:%M')

    def getRarotongaTime(self):
        return datetime.now(tz=timezone('Pacific/Rarotonga')).strftime('%a, %H:%M')

    def getHongKongTime(self):
        return datetime.now(tz=timezone('Asia/Hong_Kong')).strftime('%a, %H:%M')        

    def getNairobeTime(self):
        return datetime.now(tz=timezone('Africa/Nairobi')).strftime('%a, %H:%M')        
    
if __name__ == '__main__':
    wc = WorldClock()
    for line in wc.worldmap:
        print(line)
