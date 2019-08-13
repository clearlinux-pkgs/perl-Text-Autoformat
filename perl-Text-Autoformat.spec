#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Text-Autoformat
Version  : 1.75
Release  : 22
URL      : https://cpan.metacpan.org/authors/id/N/NE/NEILB/Text-Autoformat-1.75.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/N/NE/NEILB/Text-Autoformat-1.75.tar.gz
Summary  : A Perl module for automatic text wrapping and reformatting
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Text-Autoformat-license = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Text::Reform)

%description
This archive contains the distribution Text-Autoformat,
version 1.75:
Automatic text wrapping and reformatting

%package dev
Summary: dev components for the perl-Text-Autoformat package.
Group: Development
Provides: perl-Text-Autoformat-devel = %{version}-%{release}
Requires: perl-Text-Autoformat = %{version}-%{release}
Requires: perl-Text-Autoformat = %{version}-%{release}

%description dev
dev components for the perl-Text-Autoformat package.


%package license
Summary: license components for the perl-Text-Autoformat package.
Group: Default

%description license
license components for the perl-Text-Autoformat package.


%prep
%setup -q -n Text-Autoformat-1.75

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
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
cp LICENSE %{buildroot}/usr/share/package-licenses/perl-Text-Autoformat/LICENSE
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
/usr/lib/perl5/vendor_perl/5.28.2/Text/Autoformat.pm
/usr/lib/perl5/vendor_perl/5.28.2/Text/Autoformat/Hang.pm
/usr/lib/perl5/vendor_perl/5.28.2/Text/Autoformat/NullHang.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Text::Autoformat.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Text-Autoformat/LICENSE
