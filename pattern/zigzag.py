import time,sys
spaces=0
isInc= True

try:
    while True:
        print(' '*spaces, end='')
        print('********')
        time.sleep(0.1)
        if isInc:
            spaces+=1
            if spaces==20:
                isInc=False
        else:
            spaces-=1
            if spaces==0:
                isInc=True
except KeyboardInterrupt:
    sys.exit()