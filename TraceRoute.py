###################################################################################################################################
#Tested on: Windows 11, Visual Studio 2022, Python 3.9
###################################################################################################################################
#allow pings through firewall:
#https://www.thewindowsclub.com/how-to-allow-pings-icmp-echo-requests-through-windows-firewall
#Make sure all pings are allowed, I have not narrowed down what specific ping type it should be but allowing echo alone is not it
###################################################################################################################################
#Steps
# 1. Download the "Servers.txt" and this python file into same folder
# 2. Import icmplib using: pip install icmplib
#       Documentation Link:https://pypi.org/project/icmplib/
# 3. Run program, use a keyboard interrupt to stop(Ctrl+C), other methods of stopping tend not to save the data.
#       Sometimes this does not work, clicking on the terminal seems to fix it.   
# 4. Data saves in a file called ServerPingOutput.CSV
# 5. Output Format: [Server Name] [# of Hops] [IP of Hop] [RTT on Hop] [Unix Timestamp]
###################################################################################################################################

from icmplib import traceroute
import time
import csv


with open(r"ServerPingOutput.CSV", "w+") as output_file:
    output = csv.writer(output_file) 
    while (1):
        with open(r"Servers.txt") as file:
            for name in file:
                print(name)
                name = name.strip()
                hops = traceroute(name)
                last_distance = 0
                for hop in hops:
                    currenttime = time.time()
                    ttl = hop.distance
                    address = hop.address
                    rtt = hop.avg_rtt
                    
                    print(f'{ttl}    {address}    {rtt} ms')#print out all the hops
                    output.writerow([name, ttl,address,rtt, currenttime])
                    last_distance = hop.distance
