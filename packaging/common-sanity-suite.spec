Name:		common-sanity-suite
Summary:	Sanity suite for Tizen Common
Version:	1.1
Release:        0
License:	GPL-2.0
Group:		Development/Testing
Source:		%{name}-%{version}.tar.gz
Source1001:	%{name}.manifest
BuildArch:	noarch
Requires:	testkit-lite
Requires:	common-suite-launcher


%description
The common-sanity-suite is the acceptance test to validate the Tizen Common image


%prep
%setup -q
cp %{SOURCE1001} .


%build


%install
## common-sanity-suite
install -d %{buildroot}/%{_datadir}/tests/%{profile}/%{name}
install -m 0755 runtest %{buildroot}/%{_datadir}/tests/%{profile}/%{name}
install -m 644 *.xml %{buildroot}/%{_datadir}/tests/%{profile}/%{name}
install -m 0644 LICENSE %{buildroot}/%{_datadir}/tests/%{profile}/%{name}
cp -r TESTDIR %{buildroot}/%{_datadir}/tests/%{profile}/%{name}


%files
%manifest %{name}.manifest
%defattr(-,root,root)
%{_datadir}/tests/%{profile}/%{name}
