%define upstream_name    Test-Cmd
%define upstream_version 1.06

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Perl module for portable testing of commands and scripts

License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Test/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:  perl-devel
BuildArch:	noarch

%description 
The Test::Cmd module provides a low-level framework for portable automated
testing of executable commands and scripts (in any language, not just Perl),
especially commands and scripts that interact with the file system.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/Test
%{_mandir}/*/*



