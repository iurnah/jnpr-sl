def time_to_int(time):
    minutes = time.hour * 60 + time.minute
    seconds = minutes * 60 + time.second
    return seconds

def int_to_time(seconds):
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time

def print_attributes(obj):
    for attr in obj.__dict__:
        print attr, getattr(obj, attr)

class Time():
    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second
        
    def __str__(self):
        return '%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second)

#    def __add__(self, other):
#      seconds = self.time_to_int() + other.time_to_int()
#      return int_to_time(seconds)


    #type-based dispatch
    def __add__(self, other):
        if isinstance(other, Time):
            return self.add_time(other)
        else:
            return self.increment(other)

    def __radd__(self, other):
        print 'in __radd__'
        return self.__add__(other)
    
    def print_time(time):
        print '%.2d:%.2d:%.2d' % (time.hour, time.minute, time.second)

    def increment(self, seconds):
        seconds += self.time_to_int()
        return int_to_time(seconds)

    def time_to_int(time):
        minutes = time.hour * 60 + time.minute
        seconds = minutes * 60 + time.second
        return seconds

    def int_to_time(seconds):
        time = Time()
        minutes, time.second = divmod(seconds, 60)
        time.hour, time.minute = divmod(minutes, 60)
        return time

    def add_time(self, other):
        seconds = self.time_to_int() + other.time_to_int()
        return int_to_time(seconds)



'''The testing section begin'''
start = Time()
start.hour=9
start.minute=10
start.second=45
print 'instance start created!'

print 'Time.print_time(start)'
Time.print_time(start)

print 'start.print_time()'
start.print_time()

delta = raw_input('Enter the increment value: >')

print 'end is created:)'
end = start.increment(int(delta))

print 'end.increment(%d)' % (int(delta))
end.print_time()

time = Time()
time.print_time()

time = Time(9)
time.print_time()

time = Time(9, 10)
time.print_time()

start1 = Time(9, 45)
duration = Time(1, 35)

print start1 + duration
print start1 + 1337
