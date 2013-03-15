%define		_class		Text
%define		_subclass	Figlet
%define		upstream_name	%{_class}_%{_subclass}

Name:		php-pear-%{upstream_name}
Version:	1.0.2
Release:	4
Summary:	Render text using FIGlet fonts
License:	PHP License
Group:		Development/PHP
URL:		http://pear.php.net/package/Text_Figlet/
Source0:	http://download.pear.php.net/package/%{upstream_name}-%{version}.tar.bz2
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildArch:	noarch
BuildRequires:	php-pear


%description
Engine for use FIGlet fonts to rendering text.

%prep
%setup -q -c
mv package.xml %{upstream_name}-%{version}/%{upstream_name}.xml

%install

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean



%files
%defattr(-,root,root)
%doc %{upstream_name}-%{version}/docs/*
%{_datadir}/pear/%{_class}
%{_datadir}/pear/data/%{upstream_name}
%{_datadir}/pear/packages/%{upstream_name}.xml




%changelog
* Fri Dec 16 2011 Oden Eriksson <oeriksson@mandriva.com> 1.0.2-3mdv2012.0
+ Revision: 742287
- fix major breakage by careless packager

* Fri May 27 2011 Oden Eriksson <oeriksson@mandriva.com> 1.0.2-2
+ Revision: 679591
- mass rebuild

* Sat Aug 14 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.0.2-1mdv2011.0
+ Revision: 569601
- update to new version 1.0.2

* Sat Jul 31 2010 Thomas Spuhler <tspuhler@mandriva.org> 1.0.1-5mdv2011.0
+ Revision: 564125
- Increased release for rebuild

* Sun Nov 15 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.0.1-4mdv2010.1
+ Revision: 466322
- spec cleanup
- use pear installer
- don't ship tests, even in documentation
- own all directories
- use rpm filetriggers starting from mandriva 2010.1

* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 1.0.1-3mdv2010.0
+ Revision: 441657
- rebuild

* Thu Jan 01 2009 Oden Eriksson <oeriksson@mandriva.com> 1.0.1-2mdv2009.1
+ Revision: 322672
- rebuild

* Wed Dec 17 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.0.1-1mdv2009.1
+ Revision: 315174
- update to new version 1.0.1

* Thu Jul 17 2008 Oden Eriksson <oeriksson@mandriva.com> 1.0.0-2mdv2009.0
+ Revision: 237118
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Apr 20 2007 Oden Eriksson <oeriksson@mandriva.com> 1.0.0-1mdv2008.0
+ Revision: 16000
- fix build
- 1.0.0


* Sat Nov 11 2006 Oden Eriksson <oeriksson@mandriva.com> 0.8.1-1mdv2007.0
+ Revision: 82751
- Import php-pear-Text_Figlet

* Fri Feb 10 2006 Oden Eriksson <oeriksson@mandriva.com> 0.8.1-1mdk
- 0.8.1
- new group (Development/PHP)

* Fri Aug 26 2005 Oden Eriksson <oeriksson@mandriva.com> 0.8.0-6mdk
- rebuilt to fix auto deps

* Wed Aug 10 2005 Oden Eriksson <oeriksson@mandriva.com> 0.8.0-5mdk
- rebuilt to use new pear auto deps/reqs from pld

* Sun Jul 31 2005 Oden Eriksson <oeriksson@mandriva.com> 0.8.0-4mdk
- fix deps

* Thu Jul 21 2005 Oden Eriksson <oeriksson@mandriva.com> 0.8.0-3mdk
- reworked the %%post and %%preun stuff, like in conectiva
- fix deps

* Wed Jul 20 2005 Oden Eriksson <oeriksson@mandriva.com> 0.8.0-2mdk
- fix deps

* Tue Jul 19 2005 Oden Eriksson <oeriksson@mandriva.com> 0.8.0-1mdk
- initial Mandriva package (PLD import)

