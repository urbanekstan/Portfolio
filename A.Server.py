import socket               
import pickle
import sys

# reserve a port
port = 12327

def main():

   s = connectSocket()
   
   # Mastermind API
   numGlad, numWeap, numGues = 4, 6, 1
   orderCorrect = [3,0,1,2]
   sendInfo, guesToken = 1, numGues
     
   pack = [numGlad, numWeap, numGues]

   # a forever loop until we interrupt it or 
   # an error occurs
   while True:
   
      # Establish connection with client.
      c, addr = s.accept()     
      print ('\nGot connection from ' + str( addr))

      if sendInfo:
         print('Sending info')
         c.send(pickle.dumps(pack))
         sendInfo = 0

      else:

         print('Recieve guess')
         clientAns = pickle.loads(c.recv(1024))

         # Check answer
         a,b = handleGuess(numGlad, orderCorrect, clientAns)
         c.send(pickle.dumps([a,b]))
         
         sendInfo = 1 # JUST FOR NOW
         guesToken -= 1

      print('numGues ' + str(guesToken))
      if guesToken == 0:
         print('\nBreak')
         break
 
      # Close the connection with the client
      c.close()

   # Close server socket
   print('Server shutdown')
   s.shutdown(socket.SHUT_RDWR)
   s.close()

   
def connectSocket():
   
   # create a socket object
   s = socket.socket()         
   print ("Socket successfully created")            
 
   # Next bind to the port
   # empty string = listen to local network
   s.bind(('', port))        
   print ("socket binded to " + str(port))
 
   # put the socket into listening mode
   s.listen(5)     
   print ("socket is listening")

   return s

   
def handleGuess(numGlad, orderCorrect, orderGuess):

   a,b = 0,0
   
   for j in range(0, numGlad):

      if (orderGuess[j] == orderCorrect[j]):
         b += 1
      if orderGuess[j] in orderCorrect:
         a += 1
         
   return [a,b]


main()
