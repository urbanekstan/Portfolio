import socket
import pickle
import sys

# Define the port on which you want to connect
port = 12327

def main():

    # Get gameplay info ~ weap, glad, guesses
    rcvInfo = 1
    numGlad, numWeap, numGues = connectToServer(rcvInfo, [0])
    print(numGlad)

    rcvInfo = 0
    a,b = connectToServer(rcvInfo, [3,0,4,5])
    print(a)
    print(b)
    

    
def orderSolver(s, numGlad, numWeap, numGues):

    print('innit 2 winnit')

    

    
    return 0

def connectToServer(rcvInfo, orderGuess):
# Returns [numGlad, numWeap, numGues] if rcvInfo = 1
# Else    [a, b] if rcvInfo = 0
    
    # Create a socket object
    s = socket.socket()                      

    # connect to the server on local computer
    s.connect(('127.0.0.1', port))

    if rcvInfo:
        
        # Recieve start game info
        rec = pickle.loads(s.recv(1024))
        numGlad = rec[0]
        numWeap = rec[1]
        numGues = rec[2]

        # close the connection
        s.shutdown(socket.SHUT_RDWR)
        s.close()  
    
        return [numGlad, numWeap, numGues] 

    else:
        
        # Send order guess
        s.send(pickle.dumps(orderGuess))

        # Recieve (a,b) solution hint
        a,b = pickle.loads(s.recv(1024))
        
        # Close the connection
        s.shutdown(socket.SHUT_RDWR)
        s.close()  
    
        return [a,b]
    
    
main()
