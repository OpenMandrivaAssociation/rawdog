Name:           rawdog
Version:        2.13
Release:        1
Summary:        An RSS aggregator 
Group:          Networking/News
License:        GPL
URL:            http://offog.org/code/rawdog.html
Source0:        http://offog.org/files/%{name}-%{version}.tar.gz
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




%changelog
* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 2.12-2mdv2010.0
+ Revision: 442670
- rebuild

* Wed Mar 04 2009 Michael Scherer <misc@mandriva.org> 2.12-1mdv2009.1
+ Revision: 348619
- update to new version 2.12

* Tue Jan 06 2009 Funda Wang <fwang@mandriva.org> 2.11-5mdv2009.1
+ Revision: 326001
- rebuild

* Fri Aug 01 2008 Thierry Vignaud <tv@mandriva.org> 2.11-4mdv2009.0
+ Revision: 260072
- rebuild

* Fri Jul 25 2008 Thierry Vignaud <tv@mandriva.org> 2.11-3mdv2009.0
+ Revision: 247893
- rebuild

* Sat Mar 01 2008 Michael Scherer <misc@mandriva.org> 2.11-1mdv2008.1
+ Revision: 177250
- update to new version 2.11

  + Thierry Vignaud <tv@mandriva.org>
    - fix spacing at top of description

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 2.9-2mdv2008.1
+ Revision: 140744
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Sat Dec 09 2006 Michael Scherer <misc@mandriva.org> 2.9-2mdv2007.0
+ Revision: 94226
- Rebuild for new python
- Import rawdog


