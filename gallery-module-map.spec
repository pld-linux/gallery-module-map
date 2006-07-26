%define		_module		map
Summary:	Google Map Integration with Gallery
Name:		gallery-module-%{_module}
Version:	0.5.1d
Release:	0.1
License:	GPL
Group:		Applications/Publishing
Source0:	http://dl.sourceforge.net/gmap-module/%{_module}-module-%{version}.zip
# Source0-md5:	d5db85c689a24ff09dc0c3d4cf3f6e0f
URL:		http://gallery.sourceforge.net/
BuildRequires:	rpmbuild(macros) >= 1.268
BuildRequires:	unzip
Requires:	gallery >= 2.1.0
Requires:	webapps
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdir		%{_datadir}/gallery/modules/%{_module}

%description
Google Map integration for Gallery. There is a theme that can be used on any Gallery 2 albums and turn the display into a google map. There is also a Module that has many feature but the default map shows pictures from every albums.

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
%dir %{_appdir}
%{_appdir}
