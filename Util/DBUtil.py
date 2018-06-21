'''
Created on Jun 19, 2018

@author: M1030081
'''
import MySQLdb as mdb


class MySQLDB(object):
    '''
    classdocs
    '''
    __connection=None
    
    def __init__(self):
        try: 
            self.__connection=mdb.connect("localhost","root","root","testpythondb")
            print("connection established successfully")
        except Exception as e:
            print(e)
            raise Exception("Error in connection")
        else:
            print("connection created without any error!")
        finally:
            print("attempt to create connection was made.")
        
    def get_connection(self):
        return self.__connection
    
    def close_connection(self):
        self.__connection.close()