%include	/usr/lib/rpm/macros.perl
%define	pdir	Inline
%define	pname	Filters
Summary:	Inline::Filters perl module
Summary(pl):	Modu³ perla Inline::Filters
Name:		perl-Inline-Filters
Version:	0.12
Release:	1
License:	Artistic
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pname}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	perl-Inline >= 0.42
BuildRequires:	rpm-perlprov >= 3.0.3-16
Requires:	perl-Inline >= 0.42
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Inline::Filters - Common source code filters for Inline Modules.

%description -l pl
Modu³ Inline::Filters - filtry dla modu³ów Inline.

%prep
%setup -q -n %{pdir}-%{pname}-%{version}

%build
perl Makefile.PL </dev/null
%{__make}

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
