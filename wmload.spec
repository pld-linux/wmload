Summary: WindowMaker load gauge
Name: wmload
Version: 0.9.2
Release: 1
Source0: wmload-%{version}.tgz
Copyright: GPL
Group: X11/Utilities
BuildRoot: /var/tmp/wmload-root

%description
This is a load monitor which is designed to work with the PROC filesystem. 
Generally all Linux systems come with the PROC fs.

If you're using a different Unix and it doesn't have the PROC fs, first see 
if there is one available... otherwise this monitor won't work!

Work is currently underway to produce a more `portable' wmload that 
Solaris/Sun/HP etc.

%prep
%setup -q

%build
xmkmf
make all
strip wmload

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT/usr/X11R6
make DESTDIR=$RPM_BUILD_ROOT/usr/X11R6 install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc README
/usr/X11R6/bin/wmload
