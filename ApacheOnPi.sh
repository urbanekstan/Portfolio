#This script will set up an Apache server on raspberry pi
#Also installs PHP, MySQL, and FTP

#REQUIRES USER INTERACTION

#http://www.wikihow.com/Make-a-Raspberry-Pi-Web-Server
#Edited by Stan Urbanek

#If starting from fresh, update system
sudo dpkg-reconfigure tzdata
sudo apt-get update
sudo apt-get upgrade

#Install Hexxeh's RPI update tool
sudo apt-get install ca-certificates
sudo apt-get install git-core
sudo wget https://raw.github.com/Hexxeh/rpi-update/master/rpi-update  -O /usr/bin/rpi-update && sudo chmod +x /usr/bin/rpi-update
sudo rpi-update
sudo shutdown -r now

#Set up SSH
ifconfig
sudo /etc/init.d/ssh start

#Install Apache and PHP
sudo apt-get install apache2 php5 libapache2-mod-php5
sudo service apache2 restart

#Confirm it works
ifconfig 
echo 'Confirm this worked - Put IP address of Pi in to web browser'

#Install MySQL
sudo apt-get install mysql-server mysql-client php-mysql 
#EDITED: WAS php5-mysql but had issues

#Install FTP
sudo chown -R pi /var/www
sudo apt-get install vsftpd

#Edit vsftpd.conf file
echo 'You MUST make the following changes to vsftpd.conf'
echo '1.  anonymous_enable=YES to anonymous_enable=NO'
echo '2.  Uncomment local_enable=YES and write_enable=YES by deleting the # symbol in front of each line'
echo '3.  then go to the bottom of the file and add force_dot_files=YES.'
echo 'Pausing for 10..'
sleep 10

sudo nano /etc/vsftpd.conf

#Restart service
sudo service vsftpd restart

ln -s /var/www/ ~/www
echo 'You can now FTP using the Pi user and access the /var/www folder via a shortcut that should appear on login.'
