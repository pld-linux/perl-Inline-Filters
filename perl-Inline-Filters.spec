#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Inline
%define		pnam	Filters
Summary:	Inline::Filters Perl module
Summary(cs.UTF-8):   Modul Inline::Filters pro Perl
Summary(da.UTF-8):   Perlmodul Inline::Filters
Summary(de.UTF-8):   Inline::Filters Perl Modul
Summary(es.UTF-8):   Módulo de Perl Inline::Filters
Summary(fr.UTF-8):   Module Perl Inline::Filters
Summary(it.UTF-8):   Modulo di Perl Inline::Filters
Summary(ja.UTF-8):   Inline::Filters Perl モジュール
Summary(ko.UTF-8):   Inline::Filters 펄 모줄
Summary(nb.UTF-8):   Perlmodul Inline::Filters
Summary(pl.UTF-8):   Moduł Perla Inline::Filters
Summary(pt.UTF-8):   Módulo de Perl Inline::Filters
Summary(pt_BR.UTF-8):   Módulo Perl Inline::Filters
Summary(ru.UTF-8):   Модуль для Perl Inline::Filters
Summary(sv.UTF-8):   Inline::Filters Perlmodul
Summary(uk.UTF-8):   Модуль для Perl Inline::Filters
Summary(zh_CN.UTF-8):   Inline::Filters Perl 模块
Name:		perl-Inline-Filters
Version:	0.12
Release:	4
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	388567f0ce9d59a4c5145ef59312815d
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
# Warning: preprocesor filters do not work with perl-Inline-0.43 !
BuildRequires:	perl-Inline = 0.42
BuildRequires:	perl-Inline-C
%endif
Requires:	perl-Inline = 0.42
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Inline::Filters - Common source code filters for Inline Modules.

%description -l pl.UTF-8
Moduł Inline::Filters - filtry dla modułów Inline.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL </dev/null \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Inline/Filters.pm
%{_mandir}/man3/*
