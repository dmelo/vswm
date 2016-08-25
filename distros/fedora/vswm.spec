Name: vswm 
Version: 0.4
Release: 1%{?dist}
Summary: Very Simples Wireless Manager. Allow a simple management of wireless networks.
Group: System Environment/Base
License: GPLv3
URL: http://diogomelo.net/vswm
Source0: https://github.com/dmelo/vswm/archive/%{version}.zip

Requires: python, rfkill, wpa_supplicant, dhcp-client, wireless-tools

%description
As the name suggests it manages the wireless network in a very simplistic way.
This version have wifi WPA and WEP, with dhcp and static networks. To use it,
just place the vswm.cfg file at /etc/ and add there your existing networks. When
you call the script (without any argument) it will scan the available networks
and connect you to the first available network that appears on the cfg file.

%prep
%setup -q

%install
install -d $RPM_BUILD_ROOT/%{_sbindir}
install -d $RPM_BUILD_ROOT/%{_sysconfdir}
install -d $RPM_BUILD_ROOT/%{_mandir}/man8/
install vswm $RPM_BUILD_ROOT/%{_sbindir}
install vswm.cfg $RPM_BUILD_ROOT/%{_sysconfdir}
install man8/vswm.8 $RPM_BUILD_ROOT/%{_mandir}/man8/

%files
%{_sbindir}/vswm
%{_mandir}/man8/vswm.8*

%config(noreplace) %{_sysconfdir}/vswm.cfg
%doc AUTHOR README.md
%license COPYING

%changelog
* Tue Aug 23 2016 Diogo Oliveira de Melo <dmelo87@gmail.com> 0.4-1
- Flush IP address from device, before connecting to network

* Tue May 31 2016 Diogo Oliveira de Melo <dmelo87@gmail.com> 0.3-1
- Make output output more clean
- Enforce DNS directive

* Sat Feb 13 2016 Diogo Oliveira de Melo <dmelo87@gmail.com> 0.2-1
- Rename project to VSWM - Very Simple Wireless Manager
- Improve documentation

* Tue Sep 08 2015 Diogo Oliveira de Melo <dmelo87@gmail.com> 0.1-1
- Initial version of the package
