%define name nettee
%define version 0.1.8
%define release %mkrel 1

Summary: Nettee is a network "tee" program
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}.tar.bz2
License: GPL
Group: Networking/Other
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Url: http://saf.bio.caltech.edu/nettee.html


%description
nettee is a network "tee" program.  It can typically transfer
data between N nodes at (nearly) the full bandwidth provided by the 
switch which connects them.  It is handy for cloning nodes or moving 
large database files.

%prep
%setup -q -n %name-%version

%build
gcc %{optflags} -D_LARGEFILE64_SOURCE -o %name nettee.c

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

