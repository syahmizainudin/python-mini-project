import datetime

class Stopwatch:
    # Start the stopwatch
    def __init__(self):
        self.isStart = False
        self.isStop = True
    
    def start(self):
        if self.isStart == False:
            self.start_time = datetime.datetime.now()
            self.isStart = True
            self.isStop = False
            self.event('Start', self.start_time)
        else:
            print('Stopwatch had already start')
    
    # Stop the count and print the duration
    def stop(self):
        if self.isStop == False:
            self.stop_time = datetime.datetime.now()
            self.isStart = False
            self.isStop = True
            self.event('Stop', self.stop_time)
            self.duration_time = self.stop_time - self.start_time
            print(self.duration_time)
        else:
            print('Stopwatch is currently not running')
    
    # Reset the start, stop and duration of the stopwatch
    def reset(self):
        self.start_time = ''
        self.stop_time = ''
        self.duration_time = 0
        print('Stopwatch had been reset.')
        
    # Log the start and stop event into a file called events.txt    
    def event(self, trigger, time):
        with open('output/events.txt','a') as f:
            f.write(trigger + '\t' + str(time) + '\n')