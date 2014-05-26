Name: common-sanity-suite
Summary: common-sanity-suite
Version: 0.1.0
Release: 1
License: GPLv2
Group: Development/Testing
Source0: %{name}-%{version}.tar.gz

%description
This package is for ivi acceptance test

%prep
%setup -q

%build

%install
install -d %{buildroot}/%{_datadir}/tests/%{name}
install -m 0755 ivi/prs_checker %{buildroot}/%{_datadir}/tests/%{name} 
install ivi/tests.xml %{buildroot}/%{_datadir}/tests/%{name}
install ivi/README %{buildroot}/%{_datadir}/tests/%{name}
install LICENSE %{buildroot}/%{_datadir}/tests/%{name}


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%license LICENSE
%{_datadir}/tests/%{name}


%changelog
* Thu Nov 2 2012 Yu, Liyun <liyunx.yu@intel.com> 0.1.0-1
 - Just have core processes check

