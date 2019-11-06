#!/usr/bin/python3

# only options 1 and 4 are configured as of now

import vymgmt

def main():
    choice = "0"
    while choice == "0":
        print ("What do you want to do? ")
        print ("\t note - only options 1 and 4 are configured right now")
        print ("\t1) - change the hostname")
        print ("\t2) - enable / disable hardware offloading")
        print ("\t3) - create DNS entry for static hosts") 
        print ("\t4) - setup AirVPN client")
        print ("\t5) - setup ProtonVPN client")
        choice = input("select a choice: ")
        if choice == "1":
            print("")
            print("> Begin by connecting to the router.. ")
            print("")
            router = input("\t> Enter the routers IP address:\t")
            user = input("\t> Enter the username:\t\t")
            passwd = input("\t> Enter the password:\t\t")
            vyos = vymgmt.Router(router, user, password=passwd, port=2727)
            vyos.login()
            vyos.configure() 
            print("")
            input("\t---> Connected! Press Enter to continue..")
            hostname = input("\t\t> Enter a new hostname:\t")
            cmd = "system host-name " + hostname
            vyos.set(cmd)
            
            vyos.commit()
            vyos.save()
            vyos.exit()
            vyos.logout()
            print("\t\t> Success! Exiting now..")
        if choice == "4": print("")
            print("> Begin by connecting to the router.. ")
            print("")
            router = input("\t> Enter the routers IP address:\t")
            user = input("\t> Enter the username:\t\t")
            passwd = input("\t> Enter the password:\t\t")
            vyos = vymgmt.Router(router, user, password=passwd, port=2727)
            vyos.login()
            vyos.configure() 
            print("")
            input("\t---> Connected! Press Enter to continue..")
            source_address = input("\t\t> Enter a source address (vpn client) in CIDR:\t")
            rule = input("\t\t> Enter a new rule # (greater than 5005):\t")
            description = input("\t\t> Enter a SHORT description \n\t\t(surrounded by single quotes)\t")
            cmd1 = "service nat rule " + rule + " description " + description
            vyos.set(cmd1)
#            print(cmd1)
            cmd2 = "service nat rule " + rule + " log enable"
            vyos.set(cmd2)
#            print(cmd2)
            cmd3 = "service nat rule " + rule + " outbound-interface vtun1"
            vyos.set(cmd3)
#            print(cmd3)
            cmd4 = "service nat rule " + rule + " source address " + source_address
            vyos.set(cmd4)
#            print(cmd4)
            cmd5 = "service nat rule " + rule + " protocol all"
            vyos.set(cmd5)
#            print(cmd5)
            cmd6 = "service nat rule " + rule + " type masquerade"
            vyos.set(cmd6)
#            print (cmd6)
             
            rule = input("\t\t> Enter a new firewall rule # (no greater than 50): ")
            cmd7 = "firewall modify OPENVPN_ROUTE rule " + rule + " description " + description
            vyos.set(cmd7)
#            print(cmd7)
            cmd8 = "firewall modify OPENVPN_ROUTE rule " + rule + " source address " + source_address
            vyos.set(cmd8)
#            print(cmd8)
            cmd9 = "firewall modify OPENVPN_ROUTE rule " + rule + " modify table 1"
            vyos.set(cmd9)
#            print(cmd9)

            vyos.commit()
            vyos.save()
            vyos.exit()
            vyos.logout()
            print("\t\t> Success! Exiting now..")
main()
