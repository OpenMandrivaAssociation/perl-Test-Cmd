%define module  Test-Cmd
%define name    perl-%{module}
%define version 1.05
%define release %mkrel 8

Name:           %{name}
Version:        %{version}
Release:        %{release}
Summary:        Perl module for portable testing of commands and scripts
License:        GPL or Artistic
Group:          Development/Perl
Url:            http://search.cpan.org/dist/%{module}
Source:         http://www.cpan.org/modules/by-module/Test/%{module}-%{version}.tar.bz2
%if %{mdkversion} < 1010
BuildRequires:  perl-devel
%endif
BuildArch:      noarch

%description 
The Test::Cmd module provides a low-level framework for portable automated
testing of executable commands and scripts (in any language, not just Perl),
especially commands and scripts that interact with the file system.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/Test
%{_mandir}/*/*

