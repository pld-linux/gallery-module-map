%define		_module		map
Summary:	Google Map Integration with Gallery
Summary(pl.UTF-8):   Integracja Google Map z Gallery
Name:		gallery-module-%{_module}
Version:	0.5.1d
Release:	0.10
License:	GPL
Group:		Applications/Publishing
Source0:	http://dl.sourceforge.net/gmap-module/%{_module}-module-%{version}.zip
# Source0-md5:	d5db85c689a24ff09dc0c3d4cf3f6e0f
URL:		http://gallery.sourceforge.net/
BuildRequires:	rpmbuild(macros) >= 1.268
BuildRequires:	unzip
Requires:	gallery >= 2.1.0
Requires:	php(ctype)
Requires:	webapps
Provides:	external-gallery-module
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdir		%{_datadir}/gallery/modules/%{_module}

%description
Google Map integration for Gallery. There is a theme that can be used
on any Gallery 2 albums and turn the display into a Google map. There
is also a Module that has many features but the default map shows
pictures from every albums.

%description -l pl.UTF-8
Integracja Google Map z Gallery. Jest to motyw, który można używać z
dowolnymi albumami Gallery 2, zamieniający ekran w mapę Google, a
także moduł, który ma wiele możliwości, ale domyślna mapa pokazuje
obrazy ze wszystkich albumów.

%prep
%setup -q -n %{_module}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_appdir}

cp -R * $RPM_BUILD_ROOT%{_appdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README*
%{_appdir}
