import time

def drop_album():
    album = "I AM MUSIC"
    for i in album:
        print("Album is called", album)
        time.sleep(2)
        print("Dropping in:")
        time.sleep(2)
        def timeValue():
            for v in range(10000, 0, -1):
                print(v)
                time.sleep(1)
            

                if v == 1:
                    print("I could’ve been dropped it, but I have to make sure it’s right. This album is for the fans.")
                    timeValue()
        timeValue()

drop_album()
