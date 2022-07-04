Summary:        Virtualization API library that supports KVM, QEMU, Xen, ESX etc
Name:           libvirt
Version:        3.2.0
Release:        9%{?dist}
License:        LGPL
URL:            http://libvirt.org/
Source0:        http://libvirt.org/sources/%{name}-%{version}.tar.xz
%define sha1    libvirt=47d4b443fdf1e268589529018c436bbc4b413a7c
Patch0:         libvirt-CVE-2017-1000256.patch
Patch1:         libvirt-CVE-2018-1064.patch
Patch2:         libvirt-CVE-2019-3840.patch
Patch3:         libvirt-CVE-2019-10161.patch
patch4:         libvirt-CVE-2019-10167.patch
patch5:         libvirt-3.2.0-CVE-2019-20485.patch
patch6:         libvirt-CVE-2021-3631.patch
Group:          Virtualization/Libraries
Vendor:         VMware, Inc.
Distribution:   Photon
BuildRequires:  cyrus-sasl
BuildRequires:  device-mapper-devel
BuildRequires:  gnutls-devel
BuildRequires:  libxml2-devel
BuildRequires:  e2fsprogs-devel
BuildRequires:  libcap-ng-devel
BuildRequires:  libnl-devel
BuildRequires:  libselinux-devel
BuildRequires:  libssh2-devel
BuildRequires:  systemd-devel
BuildRequires:  parted
BuildRequires:  python3-devel
BuildRequires:  readline-devel
BuildRequires:  xmlto
Requires:       cyrus-sasl
Requires:       device-mapper
Requires:       gnutls
Requires:       libxml2
Requires:       e2fsprogs
Requires:       libcap-ng
Requires:       libnl
Requires:       libselinux
Requires:       libssh2
Requires:       systemd
Requires:       parted
Requires:       python3
Requires:       readline

%description
Libvirt is collection of software that provides a convenient way to manage virtual machines and other virtualization functionality, such as storage and network interface management. These software pieces include an API library, a daemon (libvirtd), and a command line utility (virsh).  An primary goal of libvirt is to provide a single way to manage multiple different virtualization providers/hypervisors. For example, the command 'virsh list --all' can be used to list the existing virtual machines for any supported hypervisor (KVM, Xen, VMWare ESX, etc.) No need to learn the hypervisor specific tools!

%package docs
Summary:        libvirt docs
Group:          Development/Tools
%description docs
The contains libvirt package doc files.

%package devel
Summary:        libvirt devel
Group:          Development/Tools
Requires:       %{name} = %{version}-%{release}
%description devel
This contains development tools and libraries for libvirt.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%build
sh configure \
    --disable-silent-rules \
    --prefix=%{_prefix} \
    --bindir=%{_bindir} \
    --libdir=%{_libdir} \
    --with-udev=no \
    --with-pciaccess=no

make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install
find %{buildroot} -name '*.la' -delete

%files
%defattr(-,root,root)
%{_bindir}/*
%{_libdir}/libvirt*.so.*
%{_libdir}/libvirt/storage-backend/*
%{_libdir}/libvirt/connection-driver/*.so
%{_libdir}/libvirt/lock-driver/*.so
%{_libdir}/sysctl.d/60-libvirtd.conf
%{_libdir}/systemd/system/*
/usr/libexec/libvirt*
%{_sbindir}/*

%config(noreplace)%{_sysconfdir}/sasl2/libvirt.conf
%config(noreplace)%{_sysconfdir}/libvirt/*.conf
%{_sysconfdir}/libvirt/nwfilter/*
%{_sysconfdir}/libvirt/qemu/*
%{_sysconfdir}/logrotate.d/*
%{_sysconfdir}/sysconfig/*
%{_bindir}/*

%files devel
%{_includedir}/libvirt/*
%{_libdir}/libvirt*.so
%{_libdir}/pkgconfig/libvirt*

%dir %{_datadir}/libvirt/api/
%{_datadir}/libvirt/api/libvirt-api.xml
%{_datadir}/libvirt/api/libvirt-admin-api.xml
%{_datadir}/libvirt/api/libvirt-qemu-api.xml
%{_datadir}/libvirt/api/libvirt-lxc-api.xml

%files docs
/usr/share/augeas/lenses/*
/usr/share/doc/%{name}-%{version}/*
/usr/share/gtk-doc/*
/usr/share/libvirt/*
/usr/share/locale/*
%{_mandir}/*

%changelog
*   Mon Jul 04 2022 Mukul Sikka <msikka@vmware.com> 3.2.0-9
-   Fix for CVE-2021-3631
*   Tue Apr 07 2020 Harinadh Dommaraju <hdommaraju@vmware.com> 3.2.0-8
-   Fix for CVE-2019-20485
*   Wed Feb 12 2020 Harinadh Dommaraju <hdommaraju@vmware.com> 3.2.0-7
-   Fix for CVE-2019-10161,CVE-2019-10167
*   Fri May 24 2019 Siju Maliakkal <smaliakkal@vmware.com> 3.2.0-6
-   Fix CVE-2019-3840
*   Fri Apr 20 2018 Xiaolin Li <xiaolinl@vmware.com> 3.2.0-5
-   Fix CVE-2018-1064
*   Thu Dec 07 2017 Xiaolin Li <xiaolinl@vmware.com> 3.2.0-4
-   Move so files in folder connection-driver and lock-driver to main package.
*   Mon Dec 04 2017 Xiaolin Li <xiaolinl@vmware.com> 3.2.0-3
-   Fix CVE-2017-1000256
*   Wed Aug 23 2017 Rui Gu <ruig@vmware.com> 3.2.0-2
-   Fix missing deps in devel package
*   Thu Apr 06 2017 Kumar Kaushik <kaushikk@vmware.com> 3.2.0-1
-   Upgrading version to 3.2.0
*   Fri Feb 03 2017 Vinay Kulkarni <kulkarniv@vmware.com> 3.0.0-1
-   Initial version of libvirt package for Photon.
