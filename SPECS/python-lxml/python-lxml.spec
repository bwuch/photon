Summary:        XML and HTML with Python
Name:           python3-lxml
Version:        4.7.1
Release:        2%{?dist}
Group:          Development/Libraries
License:        BSD
URL:            http://lxml.de
Source0:        https://github.com/lxml/lxml/releases/download/lxml-%{version}/lxml-%{version}.tar.gz
%define sha512  lxml=dd0d421e10db6c9084cf5b2c04a4fc54d74bd62b4dfa83efcf92dd46cd1c5f043c47613521b2de04c450b83eb1161d197b017c53e615e5785e97e7afe106b6cf
Patch0:         lxml-CVE-2022-2309.patch
Vendor:         VMware, Inc.
Distribution:   Photon
BuildRequires:  libxslt
BuildRequires:  libxslt-devel
BuildRequires:  cython3
BuildRequires:  python3
BuildRequires:  python3-devel
BuildRequires:  python3-libs
BuildRequires:  python3-xml
BuildRequires:  python3-setuptools
Requires:       python3
Requires:       python3-libs
Requires:       libxslt
Requires:       python3-xml

%description
The lxml XML toolkit is a Pythonic binding for the C libraries libxml2 and libxslt. It is unique in that it combines the speed and XML feature completeness of these libraries with the simplicity of a native Python API, mostly compatible but superior to the well-known ElementTree API.

%prep
%autosetup -p1 -n lxml-%{version}

%build
python3 setup.py build

%install
python3 setup.py install --prefix=%{_prefix} --root=%{buildroot}

%check
export LC_ALL=en_US.UTF-8
export LANGUAGE=en_US.UTF-8
make %{?_smp_mflags} test

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{python3_sitelib}/*

%changelog
* Mon Jul 18 2022 Ashwin Dayanand Kamat <kashwindayan@vmware.com> 4.7.1-2
- Fix for CVE-2022-2309
* Mon Jan 03 2022 Sujay G <gsujay@vmware.com> 4.7.1-1
- Bump version to 4.7.1 to fix CVE-2021-43818
* Mon Nov 15 2021 Prashant S Chauhan <psinghchauha@vmware.com> 4.6.3-2
- Add python3-setuptools as build requires
* Mon Jul 26 2021 Shreyas B <shreyasb@vmware.com> 4.6.3-1
- Update to v4.6.3 to Address CVE-2021-28957 & CVE-2020-27783
* Fri Nov 06 2020 Gerrit Photon <photon-checkins@vmware.com> 4.6.1-1
- Automatic Version Bump
* Fri Jul 24 2020 Gerrit Photon <photon-checkins@vmware.com> 4.5.2-1
- Automatic Version Bump
* Fri Jun 19 2020 Tapas Kundu <tkundu@vmware.com> 4.2.4-3
- Mass removal python2
* Wed Nov 28 2018 Tapas Kundu <tkundu@vmware.com> 4.2.4-2
- Fix make check
- moved build requires from subpackage
* Sun Sep 09 2018 Tapas Kundu <tkundu@vmware.com> 4.2.4-1
- Update to version 4.2.4
* Mon Aug 07 2017 Dheeraj Shetty <dheerajs@vmware.com> 3.7.3-3
- set LC_ALL and LANGUAGE for the tests to pass
* Thu Jun 01 2017 Dheeraj Shetty <dheerajs@vmware.com> 3.7.3-2
- Use python2_sitelib
* Mon Apr 03 2017 Sarah Choi <sarahc@vmware.com> 3.7.3-1
- Update to 3.7.3
* Wed Feb 08 2017 Xiaolin Li <xiaolinl@vmware.com> 3.5.0b1-4
- Added python3 site-packages.
* Tue Oct 04 2016 ChangLee <changlee@vmware.com> 3.5.0b1-3
- Modified %check
* Tue May 24 2016 Priyesh Padmavilasom <ppadmavilasom@vmware.com> 3.5.0b1-2
- GA - Bump release of all rpms
* Wed Oct 28 2015 Divya Thaluru <dthaluru@vmware.com> 3.5.0b1-1
- Initial build.
