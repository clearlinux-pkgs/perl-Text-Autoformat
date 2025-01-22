#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
# autospec version: v21
# autospec commit: 94c6be0
#
Name     : perl-Text-Autoformat
Version  : 1.75
Release  : 39
URL      : https://cpan.metacpan.org/authors/id/N/NE/NEILB/Text-Autoformat-1.75.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/N/NE/NEILB/Text-Autoformat-1.75.tar.gz
Summary  : 'Automatic text wrapping and reformatting'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Text-Autoformat-license = %{version}-%{release}
Requires: perl-Text-Autoformat-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Text::Reform)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
This archive contains the distribution Text-Autoformat,
version 1.75:
Automatic text wrapping and reformatting

%package dev
Summary: dev components for the perl-Text-Autoformat package.
Group: Development
Provides: perl-Text-Autoformat-devel = %{version}-%{release}
Requires: perl-Text-Autoformat = %{version}-%{release}

%description dev
dev components for the perl-Text-Autoformat package.


%package license
Summary: license components for the perl-Text-Autoformat package.
Group: Default

%description license
license components for the perl-Text-Autoformat package.


%package perl
Summary: perl components for the perl-Text-Autoformat package.
Group: Default
Requires: perl-Text-Autoformat = %{version}-%{release}

%description perl
perl components for the perl-Text-Autoformat package.


%prep
%setup -q -n Text-Autoformat-1.75
cd %{_builddir}/Text-Autoformat-1.75

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} -I. Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Text-Autoformat
cp %{_builddir}/Text-Autoformat-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/perl-Text-Autoformat/7e7147eb6dbe39bfc665364e6c717827fc8e51d3 || :
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Text::Autoformat.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Text-Autoformat/7e7147eb6dbe39bfc665364e6c717827fc8e51d3

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
