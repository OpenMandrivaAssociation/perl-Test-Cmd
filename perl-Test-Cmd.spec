%define upstream_name    Test-Cmd
%define upstream_version 1.05

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2

Summary:	Perl module for portable testing of commands and scripts
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Test/%{upstream_name}-%{upstream_version}.tar.bz2

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


%changelog
* Sat Aug 01 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1.50.0-1mdv2010.0
+ Revision: 405547
- rebuild using %%perl_convert_version

* Wed Jul 23 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.05-10mdv2009.0
+ Revision: 241965
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sat Sep 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.05-8mdv2008.0
+ Revision: 86967
- rebuild


* Tue Aug 29 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.05-7mdv2007.0
- Rebuild

* Fri Apr 28 2006 Nicolas Lécureuil <neoclust@mandriva.org> 1.05-6mdk
- Fix SPEC according to Perl Policy
    - Source URL

* Tue Dec 20 2005 Guillaume Rousse <guillomovitch@mandriva.org> 1.05-5mdk
- spec cleanup
- better URL

* Mon Dec 20 2004 Guillaume Rousse <guillomovitch@mandrake.org> 1.05-4mdk
- fix buildrequires in a backward compatible way

* Fri Jul 23 2004 Guillaume Rousse <guillomovitch@mandrake.org> 1.05-3mdk 
- rpmbuildupdate aware

* Wed Feb 25 2004 Guillaume Rousse <guillomovitch@mandrake.org> 1.05-2mdk
- fixed dir ownership (distlint)
- let spec-helper do its job

* Mon Feb 02 2004 Guillaume Rousse <guillomovitch@mandrake.org> 1.05-1mdk
- first mdk release

