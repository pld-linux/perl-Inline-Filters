#
# Conditional build:
# _without_tests - do not perform "make test"
%include	/usr/lib/rpm/macros.perl
%define		pdir	Inline
%define		pname	Filters
Summary:	Inline::Filters Perl module
Summary(cs):	Modul Inline::Filters pro Perl
Summary(da):	Perlmodul Inline::Filters
Summary(de):	Inline::Filters Perl Modul
Summary(es):	Módulo de Perl Inline::Filters
Summary(fr):	Module Perl Inline::Filters
Summary(it):	Modulo di Perl Inline::Filters
Summary(ja):	Inline::Filters Perl ¥â¥¸¥å¡¼¥ë
Summary(ko):	Inline::Filters ÆÞ ¸ðÁÙ
Summary(no):	Perlmodul Inline::Filters
Summary(pl):	Modu³ Perla Inline::Filters
Summary(pt):	Módulo de Perl Inline::Filters
Summary(pt_BR):	Módulo Perl Inline::Filters
Summary(ru):	íÏÄÕÌØ ÄÌÑ Perl Inline::Filters
Summary(sv):	Inline::Filters Perlmodul
Summary(uk):	íÏÄÕÌØ ÄÌÑ Perl Inline::Filters
Summary(zh_CN):	Inline::Filters Perl Ä£¿é
Name:		perl-Inline-Filters
Version:	0.12
Release:	3
License:	Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pname}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-16
%if %{!?_without_tests:1}%{?_without_tests:0}
# Warning: preprocesor filters do not work with perl-Inline-0.43 !
BuildRequires:	perl-Inline = 0.42
BuildRequires:	perl-Inline-C
%endif
Requires:	perl-Inline = 0.42
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Inline::Filters - Common source code filters for Inline Modules.

%description -l pl
Modu³ Inline::Filters - filtry dla modu³ów Inline.

%prep
%setup -q -n %{pdir}-%{pname}-%{version}

%build
%{__perl} Makefile.PL </dev/null
%{__make}
%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_sitelib}/Inline/Filters.pm
%{_mandir}/man3/*
