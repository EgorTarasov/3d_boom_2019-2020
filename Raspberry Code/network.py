'''
Module to connect smartbin to server
'''
import requests


class Connection:
    '''
    object to estasblish connection
    between raspberry pi
    and server
    '''

    def __init__(self):
        '''
        setting up server ip
        and host ip
        '''
        self.hostname = '192.168.0.27'
        self.server_ip = '192.168.0.33:8000'

    def get_ip(self):
        '''
        returns: self.ip
        '''
        return self.hostname

    def send_data(self, data):
        '''
        sending data to server
        '''
        response = requests.get('https://' + self.server_ip + '/put' + str(data))
        if response.status_code == 200:
            command, value = 'send', 200
        else:
            command, value = 'send error', 404
        return command, value
