Summary:	WindowMaker load gauge
Summary(pl):	Monitor obci±¿enia systemu dla WindowMakera
Name:		wmload
Version:	0.9.2
Release:	5
License:	GPL
Group:		X11/Window Managers/Tools
Source0:	http://www.cs.mun.ca/~gstarkes/wmaker/dockapps/files/%{name}-%{version}.tgz
# Source0-md5:	6498bcb49f09d203ac5a304b3c149d75
Source1:	%{name}.desktop
Patch0:		%{name}-ComplexProgramTargetNoMan.patch
URL:		http://www.cs.mun.ca/~gstarkes/wmaker/dockapps/sys.html#wmload
BuildRequires:	XFree86-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
This is a load monitor which is designed to work with the PROC
filesystem. Generally all Linux systems come with the PROC fs.

If you're using a different Unix and it doesn't have the PROC fs,
first see if there is one available... otherwise this monitor won't
work!

%description -l pl
Program ten monitoruje obci±¿enie systemu korzystaj±c z systemu plików
PROC.

%prep
%setup -q
%patch0 -p1

%build
xmkmf
%{__make} all \
	CDEBUGFLAGS="%{rpmcflags}" \
	CC=%{__cc}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_prefix},%{_applnkdir}/DockApplets}

%{__make} DESTDIR=$RPM_BUILD_ROOT%{_prefix} install

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/DockApplets


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/%{name}
%{_applnkdir}/DockApplets/wmload.desktop
