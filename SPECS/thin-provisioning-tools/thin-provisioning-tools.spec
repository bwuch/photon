Summary:        Thin provisioning tools
Name:           thin-provisioning-tools
Version:        0.6.3
Release:        4%{?dist}
License:        GPLv3+
Group:          System Environment/Base
URL:            https://github.com/jthornber/thin-provisioning-tools
Vendor:         VMware, Inc.
Distribution:   Photon

Source0:        %{name}-%{version}.tar.gz
%define sha1    %{name}=6e2db216ffaa62a8945d42d91131b94b59fe73d7

BuildRequires:  expat-devel
BuildRequires:  libaio-devel
BuildRequires:  boost-devel

Requires:       expat
Requires:       libaio
Requires:       boost

%description
thin-provisioning-tools contains check,dump,restore,repair,rmap
and metadata_size tools to manage device-mapper thin provisioning
target metadata devices; cache check,dump,metadata_size,restore
and repair tools to manage device-mapper cache metadata devices
are included and era check, dump, restore and invalidate to manage
snapshot eras

%prep
%autosetup -p1

%build
autoconf
export CFLAGS="%{optflags}"
export LDFLAGS=""
%configure STRIP=/bin/true

make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} MANDIR=%{_mandir} install %{?_smp_mflags}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc COPYING README.md
%{_mandir}/man8/*
%{_sbindir}/pdata_tools
%{_sbindir}/cache_check
%{_sbindir}/cache_dump
%{_sbindir}/cache_metadata_size
%{_sbindir}/cache_restore
%{_sbindir}/cache_repair
%{_sbindir}/era_check
%{_sbindir}/era_dump
%{_sbindir}/era_restore
%{_sbindir}/era_invalidate
%{_sbindir}/thin_check
%{_sbindir}/thin_dump
%{_sbindir}/thin_metadata_size
%{_sbindir}/thin_restore
%{_sbindir}/thin_repair
%{_sbindir}/thin_rmap
%{_sbindir}/thin_delta
%{_sbindir}/thin_ls
%{_sbindir}/thin_trim

%changelog
* Fri Oct 29 2021 Shreenidhi Shedi <sshedi@vmware.com> 0.6.3-4
- Bump version as a part of boost upgrade
* Fri Oct 13 2017 Alexey Makhalov <amakhalov@vmware.com> 0.6.3-3
- Use standard configure macros
* Tue Apr 25 2017 Priyesh Padmavilasom <ppadmavilasom@vmware.com> 0.6.3-2
- Ensure non empty debuginfo
* Tue Mar 28 2017 Xiaolin Li <xiaolinl@vmware.com> 0.6.3-1
- Updated to version 0.6.3.
* Mon Mar 13 2017 Alexey Makhalov <amakhalov@vmware.com> 0.6.1-3
- Fix gcc-6.3 compilation errors
* Tue May 24 2016 Priyesh Padmavilasom <ppadmavilasom@vmware.com> 0.6.1-2
- GA - Bump release of all rpms
* Thu Feb 25 2016 Kumar Kaushik <kaushikk@vmware.com> 0.6.1-1
- Updating version
* Tue Mar 3 2015 Divya Thaluru <dthaluru@vmware.com> 0.4.1-1
- Initial version
