Summary:	WindowMaker load gauge
Summary(pl):	Monitor obci��enia systemu dla WindowMakera
Name:		wmload
Version:	0.9.2
Release:	3
Copyright:      GPL
Group:          X11/Window Managers/Tools
Group(pl):	X11/Zarz�dcy Okien/Narz�dzia
Source0:	%{name}-%{version}.tgz
Source1:	wmload.desktop
BuildPrereq:	XFree86-devel
BuildPrereq:	xpm-devel
BuildRoot:	/tmp/%{name}-%{version}-root

%define _prefix	/usr/X11R6

%description
This is a load monitor which is designed to work with the PROC filesystem. 
Generally all Linux systems come with the PROC fs.

If you're using a different Unix and it doesn't have the PROC fs, first see 
if there is one available... otherwise this monitor won't work!

Work is currently underway to produce a more `portable' wmload that 
Solaris/Sun/HP etc.

%description -l pl
Program ten monitoruje obci��enie systemu korzystaj�c 
z systemu plik�w PROC. 

%prep
%setup -q

%build
xmkmf
make all \
	CDEBUGFLAGS="$RPM_OPT_FLAGS"
strip %{name}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_prefix},/etc/X11/applnk/DockApplets}

make DESTDIR=$RPM_BUILD_ROOT%{_prefix} install

install %{SOURCE1} $RPM_BUILD_ROOT/etc/X11/applnk/DockApplets

gzip -9nf README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.gz
%attr(755,root,root) %{_bindir}/%{name}
/etc/X11/applnk/DockApplets/wmload.desktop
