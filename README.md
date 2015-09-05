VSNM - Very Simple Network Manager
==================================

As the name suggests it manages the network in a very simplistic way. This 
version have wifi WPA and WEP, with dhcp and static networks. To use it, just 
place the vsnm.cfg file at /etc/ and add there your existing networks. When you
call the script (without any argument) it will scan the available networks and
connect you to the first available network that appears on the cfg file.


INSTALL
-------

    cp vsnm.py /usr/local/bin/vsnm
    cp vsnm.cfg /etc/

Make sure `/usr/local/bin` is in your $PATH. After that, edit `/etc/vsnm.cnf`
to contain information about your networks.


USAGE
-----

    vsnm

It will make the script read the /etc/vsnm.cfg file and connect to an available 
network listed there, if any.
