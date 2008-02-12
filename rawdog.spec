Name:           rawdog
Version:        2.9
Release:        %mkrel 2
Summary:        An RSS aggregator 
Group:          Networking/News
License:        GPL
URL:            http://offog.org/code/rawdog.html
Source0:        http://offog.org/files/%{name}-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-root
BuildArch:      noarch
BuildRequires:  python-devel
%description
rawdog is an RSS Aggregator Without Delusions Of Grandeur. Written in Python, 
it uses Mark Pilgrim's feed parser to read RSS 0.9, 1.0, 2.0, CDF and Atom 
feeds. 

It runs from cron, collects articles from a number of feeds, and generates a 
static HTML page listing the newest articles in date order. It supports 
per-feed customizable update times, and uses ETags, Last-Modified, and gzip 
compression to minimize network bandwidth usage.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
python setup.py install --prefix=$RPM_BUILD_ROOT/%_prefix

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc README config NEWS PLUGINS style.css 
%_bindir/rawdog
%py_puresitedir/rawdoglib/
%py_puresitedir/*.egg-info
%_mandir/man1/*


