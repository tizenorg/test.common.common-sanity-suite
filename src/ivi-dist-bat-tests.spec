Summary: ivi-dist-bat-tests
Name: ivi-dist-bat-tests
Version: 0.1.0
Release: 1
License: GPLv2
Group: Development/Testing
Source0: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
#Requires: 

%description
This package is for ivi acceptance test

%prep
%setup -q

%build
./autogen.sh
%configure
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
/opt/ivi-dist-bat-tests/*

%changelog
* Thu Nov 2 2012 Yu, Liyun <liyunx.yu@intel.com> 0.1.0-1
 - Just have core processes check

