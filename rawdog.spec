Name:           rawdog
Version:        2.23
Release:        1
Summary:        An RSS aggregator 
Group:          Networking/News
License:        GPL
URL:            http://offog.org/code/rawdog.html
Source0:        http://offog.org/files/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  python2

%description
rawdog is an RSS Aggregator Without Delusions Of Grandeur. Written in Python, 
it uses Mark Pilgrim's feed parser to read RSS 0.9, 1.0, 2.0, CDF and Atom 
feeds. 

It runs from cron, collects articles from a number of feeds, and generates a 
static HTML page listing the newest articles in date order. It supports 
per-feed customizable update times, and uses ETags, Last-Modified, and gzip 
compression to minimize network bandwidth usage.

This package is deprecated because it has been abandoned upstream and still
requires python 2.x.
Users are strongly advised to look for an alternative.

%prep
%autosetup -p1
python2 setup.py build

%install
python2 setup.py install --root=%{buildroot}

%files
%doc README config NEWS PLUGINS style.css 
%{_bindir}/rawdog
%{py2_puresitedir}/rawdoglib
%{py2_puresitedir}/*.egg-info
%{_mandir}/man1/*
