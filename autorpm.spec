Summary:	RPM Auto-Installer or FTP Mirrorer
Summary(pl):	Auto instalator i ftp mirror pakietow rpm
Name:		autorpm
Version:	1.8
Release:	1
Copyright:	GPL
Group:		Utilities/System
Group(pl):	Narzêdzia/System
Source:		ftp://ftp.kaybee.org/pub/linux/%{name}-%{version}.tar.gz
URL:		http://www.kaybee.org/~kirk/html/linux.html
Requires:	rpm
Requires:	dialog
Requires:	libnet
Requires:	mailx
BuildRoot:	/tmp/%{name}-%{version}-root

%description
AutoRPM is a program that can do any combination of the following: mirror
RPMs from an FTP site, keep installed RPMs consistent with an FTP site or
local directory, and keep installed RPMs in a cluster or network of systems
consistent. It is highly flexible and even contains a very nice, menu-driven
Interactive-Install mode.

%description -l pl
AutoRPM jest programem, który mo¿e wykonywaæ dowoln± kombinacjê
nastêpuj±cych czynno¶ci: mirrorowanie pakietów rpm z podanego adresu serwea
ftp, aktualizowanie bazy zainstalowanych pakietów wzglêdem zawarto¶ci
serwera ftp lub katalogu lokalnego. Autorpm jest do¶æ ³±two konfigurowalny i
posiada do¶æ du¿e mo¿liwo¶ci. Mo¿na go u¿ywaæ w trybie wsadowym i
interakcyjnym gdzie posiada do¶æ przyjemny interfejs.

%prep
%setup -q

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/etc/cron.daily,%{_mandir}/man{5,8},%{_sbindir}} \
	$RPM_BUILD_ROOT/var/spool/autorpm

install autorpm.pl $RPM_BUILD_ROOT%{_sbindir}/autorpm
install autorpm.conf $RPM_BUILD_ROOT/etc/autorpm.conf.sample

install autorpm.conf.5 $RPM_BUILD_ROOT%{_mandir}/man5
install autorpm.8 $RPM_BUILD_ROOT%{_mandir}/man8

ln -sf ../..%{_sbindir}/autorpm $RPM_BUILD_ROOT/etc/cron.daily/autorpm

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man*/* \
	README CHANGES CREDITS TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {README,CHANGES,CREDITS,TODO}.gz
%dir /var/spool/autorpm
%attr(600,root,root) %config(missingok) /etc/autorpm.conf.sample
%attr(750,root,root) %{_sbindir}/autorpm
%attr(750,root,root) /etc/cron.daily/autorpm
%{_mandir}/man[58]/*
