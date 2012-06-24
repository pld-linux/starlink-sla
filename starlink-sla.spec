Summary:	SLALIB - positional astronomy library
Summary(pl):	SLALIB - biblioteka do astronomii pozycyjnej
Name:		starlink-sla
Version:	2.4_11.218
Release:	1
License:	GPL
Group:		Libraries
Source0:	ftp://ftp.starlink.rl.ac.uk/pub/ussc/store/sla/sla.tar.Z
# Source0-md5:	b418183607ed5c7d7589134da8d233ec
URL:		http://www.starlink.rl.ac.uk/static_www/soft_further_SLALIB.html
BuildRequires:	gcc-g77
BuildRequires:	sed >= 4.0
BuildRequires:	starlink-htx
Requires:	starlink-htx
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		stardir		/usr/lib/star

%description
SLALIB is a library of routines intended to make accurate and reliable
positional-astronomy applications easier to write. Most SLALIB
routines are concerned with astronomical position and time, but a
number have wider trigonometrical, numerical or general applications.
The applications ASTROM, COCO, RV and TPOINT all make extensive use of
the SLALIB routines, as do a number of telescope control systems
around the world. The SLALIB versions currently in service are written
in Fortran 77 and run on VAX/VMS, several Unix platforms and PC.

%description -l pl
SLALIB to biblioteka funkcji maj�cych u�atwi� pisanie dok�adnych i
wiarygodnych aplikacji zwi�zanych z astronomi� pozycyjn�. Wi�kszo��
funkcji SLALIB odnosi si� do astronomicznych pozycji i czasu, ale jest
troch� og�lnych, trygonometrycznych i numerycznych. Aplikacje takie
jak ASTROM, COCO, RV i TPOINT intensywnie wykorzystuj� funkcje SLALIB,
podobnie jak wiele system�w steruj�cych teleskopami na �wiecie.
Aktualnie u�ywane wersje SLALIB-a s� napisane w Fortranie 77 i
dzia�aj� na systemach VAX/VMS, r�nych platformach uniksowych oraz PC.

%package devel
Summary:	Development files for SLA library
Summary(pl):	Pliki programistyczne biblioteki SLA
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Development files for SLA library.

%description devel -l pl
Pliki programistyczne biblioteki SLA.

%package static
Summary:	Static Starlink SLA library
Summary(pl):	Statyczna biblioteka Starlink SLA
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static Starlink SLA library.

%description static -l pl
Statyczna biblioteka Starlink SLA.

%prep
%setup -q -c

sed -i -e "s/-O'/%{rpmcflags} -fPIC'/" mk

%build
SYSTEM=ix86_Linux \
BLD_SHR='f() { g77 -shared -Wl,-soname $$1 -o $$1 $$2;}; f' \
./mk build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{stardir}/help

SYSTEM=ix86_Linux \
./mk install \
	STARLINK=%{stardir} \
	INSTALL=$RPM_BUILD_ROOT%{stardir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc sla.news
%{stardir}/dates/*
%docdir %{stardir}/docs
%{stardir}/docs/sun*
%attr(755,root,root) %{stardir}/share/*.so

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{stardir}/bin/sla_link*

%files static
%defattr(644,root,root,755)
%{stardir}/lib/*.a
