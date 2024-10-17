%define name nettee
%define version 0.1.8
%define release 8

Summary: Network "tee" program
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}.tar.bz2
License: GPL
Group: Networking/Other
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Url: https://saf.bio.caltech.edu/nettee.html


%description
nettee is a network "tee" program.  It can typically transfer
data between N nodes at (nearly) the full bandwidth provided by the 
switch which connects them.  It is handy for cloning nodes or moving 
large database files.

%prep
%setup -q -n %name-%version

%build
gcc -O2 -g -pipe -Wformat -Werror=format-security -fexceptions -fstack-protector --param=ssp-buffer-size=4 -fomit-frame-pointer -fasynchronous-unwind-tables -D_LARGEFILE64_SOURCE -o nettee nettee.c

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_mandir}/man1
install -m755 $RPM_BUILD_DIR/%name-%version/%name %{buildroot}%{_bindir}/%name
install -m644 $RPM_BUILD_DIR/%name-%version/%name.1 %{buildroot}%{_mandir}/man1/%name.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc LICENSE *.TXT *.html *.sh
%{_bindir}/%{name}
%{_mandir}/man1/%name.*



%changelog
* Mon Dec 06 2010 Oden Eriksson <oeriksson@mandriva.com> 0.1.8-7mdv2011.0
+ Revision: 613036
- the mass rebuild of 2010.1 packages

* Wed Jan 27 2010 Antoine Ginies <aginies@mandriva.com> 0.1.8-6mdv2010.1
+ Revision: 497237
- fix build (remove some GCC flags)

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - rebuild

* Mon Feb 18 2008 Thierry Vignaud <tv@mandriva.org> 0.1.8-2mdv2008.1
+ Revision: 170996
- rebuild
- fix "foobar is blabla" summary (=> "blabla") so that it looks nice in rpmdrake
- fix no-buildroot-tag
- kill re-definition of %%buildroot on Pixel's request

  + Antoine Ginies <aginies@mandriva.com>
    - remove buildroot

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Thu Oct 25 2007 Erwan Velu <erwan@mandriva.org> 0.1.8-1mdv2008.1
+ Revision: 102065
- 1.0.8
- 0.1.8

  + Thierry Vignaud <tv@mandriva.org>
    - fix man pages

* Tue Jun 12 2007 Antoine Ginies <aginies@mandriva.com> 0.1.7-2mdv2008.0
+ Revision: 38107
- fix group (#29869)

* Mon May 21 2007 Antoine Ginies <aginies@mandriva.com> 0.1.7-1mdv2008.0
+ Revision: 29311
- use %%mkrel macro


* Thu Nov 17 2005 Antoine Ginies <aginies@mandriva.com> 0.1.7-1mdk
- first mdk release

