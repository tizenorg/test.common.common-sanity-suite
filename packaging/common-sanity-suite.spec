Name:		common-sanity-suite
Summary:	Sanity suite for Tizen Common
Version:	1.0.0
Release:        1
License:	GPL-2.0
Group:		Development/Testing
Source:		%{name}-%{version}.tar.gz
Source1001:	%{name}.manifest
BuildArch:	noarch
Requires:	testkit-lite
Requires:	common-suite-launcher


%description
The common-sanity-suite is the acceptance test to validate the Tizen Common image

%package -n ivi-dist-bat-tests
Summary:	Sanity suite for Tizen Common
Requires:	testkit-lite

%description -n ivi-dist-bat-tests
Basic acceptance tests for Tizen IVI profile


%prep
%setup -q
cp %{SOURCE1001} .


%build


%install
## common-sanity-suite
install -d %{buildroot}/%{_datadir}/tests/%{name}
install -m 0755 common/runtest.sh %{buildroot}/%{_datadir}/tests/%{name}
install -m 644 common/*.xml %{buildroot}/%{_datadir}/tests/%{name}
install -m 0644 LICENSE %{buildroot}/%{_datadir}/tests/%{name}
cp -r common/TESTDIR %{buildroot}/%{_datadir}/tests/%{name}

## ivi-dist-bat-tests
mkdir -p %{buildroot}/%{_datadir}/tests/ivi-dist-bat-tests
install -m 0755 ivi/prs_checker %{buildroot}/%{_datadir}/tests/ivi-dist-bat-tests
install -m 0644 ivi/tests.xml %{buildroot}/%{_datadir}/tests/ivi-dist-bat-tests
install -m 0644 ivi/README %{buildroot}/%{_datadir}/tests/ivi-dist-bat-tests
install -m 0644 LICENSE %{buildroot}/%{_datadir}/tests/ivi-dist-bat-tests


%files
%manifest %{name}.manifest
%defattr(-,root,root)
%{_datadir}/tests/%{name}

%files -n ivi-dist-bat-tests
%manifest %{name}.manifest
%defattr(-,root,root)
%{_datadir}/tests/ivi-dist-bat-tests
