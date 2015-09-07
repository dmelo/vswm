VSNM - Very Simple Network Manager
==================================

As the name suggests it manages the network in a very simplistic way. This 
version have wifi WPA and WEP, with dhcp and static networks. To use it, just 
place the vsnm.cfg file at /etc/ and add there your existing networks. When you
call the script (without any argument) it will scan the available networks and
connect you to the first available network that appears on the cfg file.


DOWNLOAD
--------

VSNM can be found at GitHub
[https://github.com/dmelo/vsnm](https://github.com/dmelo/vsnm). A ZIP file can
be found on the link
[https://github.com/dmelo/vsnm/archive/master.zip](https://github.com/dmelo/vsnm/archive/master.zip). 
Replace `master` with the a version number (e.g.: 0.1) to get an specific
version.


INSTALL
-------

    cp vsnm /usr/local/bin/
    cp vsnm.cfg /etc/

Make sure `/usr/local/bin` is in your $PATH. Copy the following line into your
.bashrc file (or /etc/bashrc, or /etc/profile)

    export PATH=/usr/local/bin:$PATH

Reload the `.bashrc`

    source ~/.bashrc

Finally, edit `/etc/vsnm.cnf` to contain information about your networks.


USAGE
-----

    sudo vsnm

It will make the script read the /etc/vsnm.cfg file and connect to an available 
network listed there, if any.


AUTHOR
------

Written by Diogo Oliveira de Melo ( dmelo87 at gmail dot com ).


COPYRIGHT
---------

VSNM program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see
[http://www.gnu.org/licenses/](http://www.gnu.org/licenses/).
