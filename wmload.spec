Summary:	WindowMaker load gauge
Summary(pl):	Monitor obci±¿enia systemu dla WindowMakera
Name:		wmload
Version:	0.9.2
Release:	2
Copyright:      GPL
Group:          X11/Window Managers/Tools
Group(pl):	X11/Zarz±dcy Okien/Narzêdzia
Source:		%{name}-%{version}.tgz
BuildPrereq:	XFree86-devel
BuildPrereq:	xpm-devel
BuildRoot:	/tmp/%{name}-%{version}-root

%description
This is a load monitor which is designed to work with the PROC filesystem. 
Generally all Linux systems come with the PROC fs.

If you're using a different Unix and it doesn't have the PROC fs, first see 
if there is one available... otherwise this monitor won't work!

Work is currently underway to produce a more `portable' wmload that 
Solaris/Sun/HP etc.

%description -l pl
Program ten monitoruje obci±¿enie systemu korzystaj±c 
z systemu plików PROC. 

%prep
%setup -q

%build
xmkmf
make all CDEBUGFLAGS="$RPM_OPT_FLAGS"
strip wmload

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/usr/X11R6

make DESTDIR=$RPM_BUILD_ROOT/usr/X11R6 install

gzip -9nf README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.gz
%attr(755,root,root) /usr/X11R6/bin/wmload

%changelog
* Sat May 15 1999 Piotr Czerwiñski <pius@pld.org.pl>
  [0.9.2-2]
- initial release for PLD use,
- package is FHS 2.0 compliant.
