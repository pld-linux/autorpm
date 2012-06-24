%include	/usr/lib/rpm/macros.perl
Summary:	RPM Auto-Installer or FTP Mirrorer
Summary(pl):	Auto instalator i ftp mirror pakietow rpm
Name:		autorpm
Version:	1.9.8.4
Release:	3
License:	GPL
Group:		Utilities/System
Group(pl):	Narz�dzia/System
Source0:	ftp://ftp.kaybee.org/pub/linux/%{name}-%{version}.tar.gz
URL:		http://www.kaybee.org/~kirk/html/linux.html
Requires:	whiptail
Requires:	/bin/rpm
Requires:	/usr/bin/whiptail
Requires:	/bin/mail
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
AutoRPM is a program that can do any combination of the following:
mirror RPMs from an FTP site, keep installed RPMs consistent with an
FTP site or local directory, and keep installed RPMs in a cluster or
network of systems consistent. It is highly flexible and even contains
a very nice, menu-driven Interactive-Install mode.

%description -l pl
AutoRPM jest programem, kt�ry mo�e wykonywa� dowoln� kombinacj�
nast�puj�cych czynno�ci: mirrorowanie pakiet�w rpm z podanego adresu
serwea ftp, aktualizowanie bazy zainstalowanych pakiet�w wzgl�dem
zawarto�ci serwera ftp lub katalogu lokalnego. Autorpm jest do�� �atwo
konfigurowalny i posiada do�� du�e mo�liwo�ci. Mo�na go u�ywa� w
trybie wsadowym i interakcyjnym gdzie posiada do�� przyjemny
interfejs.

%prep
%setup -q

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/etc/cron.daily,%{_mandir}/man{5,8},%{_sbindir}} \
	$RPM_BUILD_ROOT{/var/spool/autorpm,%{_sysconfdir}/autorpm.d/pools}

install autorpm.pl	$RPM_BUILD_ROOT%{_sbindir}/autorpm
install autorpm.conf	$RPM_BUILD_ROOT%{_sysconfdir}/autorpm.d/autorpm.conf.sample
touch $RPM_BUILD_ROOT%{_sysconfdir}/autorpm.d/autorpm.conf
install autorpm.d/* 	$RPM_BUILD_ROOT%{_sysconfdir}/autorpm.d/
install pools/* 	$RPM_BUILD_ROOT%{_sysconfdir}/autorpm.d/pools/

install autorpm.conf.5 	$RPM_BUILD_ROOT%{_mandir}/man5
install autorpm.8 	$RPM_BUILD_ROOT%{_mandir}/man8

sed  -e "s=/bin/bash=/bin/sh=" autorpm.cron > $RPM_BUILD_ROOT/etc/cron.daily/autorpm

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man*/* \
	README CHANGES CREDITS TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {README,CHANGES,CREDITS,TODO}.gz
%{_mandir}/man[58]/*
%defattr(640,root,root,750)
%dir /var/spool/autorpm
%dir %{_sysconfdir}/autorpm.d
%dir %{_sysconfdir}/autorpm.d/pools
%config(missingok) %verify(not mtime,md5,size) %{_sysconfdir}/autorpm.d/autorpm.conf.sample
%ghost %{_sysconfdir}/autorpm.d/autorpm.conf
%config(missingok) %verify(not mtime,md5,size) %{_sysconfdir}/autorpm.d/*updates*
%config(missingok) %verify(not mtime,md5,size) %{_sysconfdir}/autorpm.d/pools/*updates*

%attr(750,root,root) %{_sbindir}/autorpm
%attr(750,root,root) /etc/cron.daily/autorpm
