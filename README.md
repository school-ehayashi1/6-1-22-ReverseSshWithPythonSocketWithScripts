# A Beginner's Guide to a Reverse Shell Usb 
*By US_ML_ehayashi1 and MarkAppprogrammer*


*Requires netcat for the user


In this repo we illustrate a basic client and server script for executing reverse shells. The basic theorized method for use is to download the client and cmd.txt onto a USB. *Please note that you must enable auto play for the client program to automatically execute once plugged in.* 

The program, in theory, would execute the client program, connecting to the server program which, in this case, would be made via a socket tcp connection(IPv4, socket stream). 

The server side would handle the different connections by multi-threading. Once exchanging a secure connection, the client script would execute a netcat command to create a reverse ssh(nc ip:port ~/bin/sh), enabling scripts to be run by the server side(listening via nc -lvp port)

The client script will be able to share the malware when a media device is plugged in therfore alowing the malware to spread. It will also be able to spread to the network using the client script to send infected packets to the router which will then spread to its devices.

After, the means of attack are up to you. We have provided a few simple scripts for you to utilize. Keep in mind, these programs are intended for basic pentesting and malware analysis, and were made as a fun hobby on the side, as an expression of creativity to exercise our knowledge.

*Please note that none of the authors, contributors, administrators, vandals, or anyone else connected with the makers of this repository/program, in any way whatsoever, can be responsible for your use of the information and code contained in or linked from these web pages.*