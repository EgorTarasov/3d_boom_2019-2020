import datetime


class Logger:
    '''
    Simple logging class
    '''
    def __init__(self):
        '''
        this method setting up file namea and date
        '''
        self.file_name = str(datetime.date.today()) + '.txt'
        self.log = open(self.file_name, 'w')
        self.log.write('new_log \n')
        self.log.close()
    
    def write(self, command, value):
        '''
        generates easy to read and understand
        line of action and valuable data
        '''
        log = str(datetime.datetime.now()) + ' ' + str(command) + ' ' + str(value) + '\n'
        file = open(self.file_name, 'a') 
        file.write(log)
        file.close()
        print(log)
    
    def __del__(self):
        '''
        closing file after working
        '''
        self.log.close()

