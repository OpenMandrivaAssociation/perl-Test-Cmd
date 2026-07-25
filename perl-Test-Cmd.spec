%define upstream_name    Test-Cmd
%define upstream_version 1.09

Name:		perl-%{upstream_name}
Version:	%{upstream_version}
Release:	1

Summary:	Perl module for portable testing of commands and scripts

License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://github.com/neilb/Test-Cmd
Source0:	https://cpan.metacpan.org/authors/id/N/NE/NEILB/Test-Cmd-%{upstream_version}.tar.gz

BuildRequires:	make
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



