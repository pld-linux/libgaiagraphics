Summary:	Gaia Common Graphics support
Summary(pl.UTF-8):	Obsługa grafiki wspólna dla projektu Gaia
Name:		libgaiagraphics
Version:	0.5
Release:	1
License:	LGPL v3+
Group:		Libraries
Source0:	http://www.gaia-gis.it/gaia-sins/gaiagraphics-sources/%{name}-%{version}.tar.gz
# Source0-md5:	2fdc2f155718e9f20dcdf10e474fc225
URL:		https://www.gaia-gis.it/fossil/libgaiagraphics
BuildRequires:	cairo-devel
BuildRequires:	libgeotiff-devel >= 1.2.5
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libtiff-devel
BuildRequires:	libxml2-devel >= 2
BuildRequires:	pkgconfig
BuildRequires:	proj-devel >= 4
BuildRequires:	zlib-devel
Requires:	libgeotiff >= 1.2.5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libgaiagraphics is an open source library supporting common-utility
raster handling methods.

%description -l pl.UTF-8
libgaiagraphics to mająca otwarte źródła biblioteka obsługująca
ogólnonarzędziowe funkcje do obsługi grafiki rastrowej.

%package devel
Summary:	Header files for gaiagraphics library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki gaiagraphics
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	cairo-devel
Requires:	libgeotiff-devel >= 1.2.5
Requires:	libjpeg-devel
Requires:	libpng-devel
Requires:	libtiff-devel
Requires:	libxml2-devel >= 2
Requires:	proj-devel >= 4
Requires:	zlib-devel

%description devel
Header files for gaiagraphics library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki gaiagraphics.

%package static
Summary:	Static gaiagraphics library
Summary(pl.UTF-8):	Statyczna biblioteka gaiagraphics
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static gaiagraphics library.

%description static -l pl.UTF-8
Statyczna biblioteka gaiagraphics.

%prep
%setup -q

%build
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libgaiagraphics.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS
%attr(755,root,root) %{_libdir}/libgaiagraphics.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgaiagraphics.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgaiagraphics.so
%{_includedir}/gaiagraphics.h
%{_pkgconfigdir}/gaiagraphics.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libgaiagraphics.a
