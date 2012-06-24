%include	/usr/lib/rpm/macros.perl
Summary:	RPM Auto-Installer or FTP Mirrorer
Summary(pl):	Automatyczny instalator i mirror FTP pakiet�w rpm
Name:		autorpm
Version:	3.3.3
Release:	0.2
License:	GPL
Group:		Applications/System
Source0:	ftp://ftp.kaybee.org/pub/linux/%{name}-%{version}.tar.gz
# Source0-md5:	7d81dd57443223a184694378ab72b57b
Source1:	%{name}-pld-updates.conf
Source2:	%{name}-pld-updates
Patch0:		%{name}-config.patch
URL:		http://www.kaybee.org/~kirk/html/linux.html
BuildRequires:	rpm-perlprov
Requires:	/bin/rpm
Requires:	whiptail
# any reason for whiptail being duplicate? should be mentioned here.
Requires:	/bin/mail
Requires:	/usr/bin/whiptail
BuildArch:	noarch
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
serwera FTP, aktualizowanie bazy zainstalowanych pakiet�w wzgl�dem
zawarto�ci serwera FTP lub katalogu lokalnego. Autorpm jest do�� �atwo
konfigurowalny i posiada do�� du�e mo�liwo�ci. Mo�na go u�ywa� w
trybie wsadowym i interakcyjnym gdzie posiada do�� przyjemny
interfejs.

%prep
%setup -q
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/etc/cron.daily,%{_mandir}/man{5,8},%{_sbindir}} \
	$RPM_BUILD_ROOT{/var/spool/autorpm,%{_sysconfdir}/autorpm.d/pools} \
	$RPM_BUILD_ROOT%{_sysconfdir}/autorpm.d/addons

install autorpm.pl					$RPM_BUILD_ROOT%{_sbindir}/autorpm
install autorpm.d/sample_configs/autorpm.conf-sample	$RPM_BUILD_ROOT%{_sysconfdir}/autorpm.d/autorpm.conf

install man/autorpm.conf.5 	$RPM_BUILD_ROOT%{_mandir}/man5
install man/autorpm.8 		$RPM_BUILD_ROOT%{_mandir}/man8
install %{SOURCE1}		$RPM_BUILD_ROOT%{_sysconfdir}/autorpm.d/pld-updates.conf
install %{SOURCE2}		$RPM_BUILD_ROOT%{_sysconfdir}/autorpm.d/pools/pld-updates

sed  -e "s=/bin/bash=/bin/sh=" autorpm.cron > $RPM_BUILD_ROOT/etc/cron.daily/autorpm

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc docs/{README,CREDITS,queue.format} project/{CHANGES,TODO} autorpm.d/support/{tips,introduction.txt}
%doc autorpm.d/sample_configs
%{_mandir}/man[58]/*
%defattr(640,root,root,750)
%dir /var/spool/autorpm
%dir %{_sysconfdir}/autorpm.d
%dir %{_sysconfdir}/autorpm.d/pools
%dir %{_sysconfdir}/autorpm.d/addons
%config(missingok) %verify(not mtime,md5,size) %{_sysconfdir}/autorpm.d/autorpm.conf
%config(missingok) %verify(not mtime,md5,size) %{_sysconfdir}/autorpm.d/pld-updates.conf
%config(missingok) %verify(not mtime,md5,size) %{_sysconfdir}/autorpm.d/pools/pld-updates

%attr(755,root,root) %{_sbindir}/autorpm
%attr(750,root,root) /etc/cron.daily/autorpm
