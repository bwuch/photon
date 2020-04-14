Name:         erlang
Summary:      erlang
Version:      19.3
Release:      3%{?dist}
Group:        Development/Languages
Vendor:       VMware, Inc.
Distribution: Photon
License:      ASL2.0
URL:          http://erlang.com
Source0:      otp_src_%{version}.tar.gz
%define sha1 otp_src=a3be29bff2d258399b1e2fddfc76cf2f6f1efba8
Patch0:       CVE-2016-10253.patch
%description
erlang programming language

%prep
%setup -q -n otp_src_%{version}
%patch0 -p1

%build
export ERL_TOP=`pwd`
./otp_build autoconf
./configure --disable-hipe --prefix=%{_prefix}

make

%install

make install DESTDIR=$RPM_BUILD_ROOT

%post

%files
%defattr(-,root,root)
%{_bindir}/*
%{_libdir}/*
%exclude /usr/src
%exclude %{_libdir}/debug

%changelog
* Tue Apr 14 2020 Harinadh Dommaraju <hdommaraju@vmware.com> 19.3-3
- Fix CVE-2016-10253
* Fri Oct 13 2017 Alexey Makhalov <amakhalov@vmware.com> 19.3-2
- Remove BuildArch
* Thu Apr 06 2017 Chang Lee <changlee@vmware.com> 19.3-1
- Updated Version
* Mon Dec 12 2016 Priyesh Padmavilasom <ppadmavilasom@vmware.com> 19.1-1
- Initial.

