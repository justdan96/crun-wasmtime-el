%global git0 https://github.com/containers/%{name}

# Used for comparing with latest upstream tag
# to decide whether to autobuild and set download_url (non-rawhide only)
%define built_tag 1.14.4

Summary: OCI runtime written in C
Name: crun
Version: 1.14.4
Release: 1%{?dist}
URL: %{git0}
Source0: %{name}-%{version}.tar.xz
License: GPLv2+

# We always run autogen.sh
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: gcc
%if 0%{?centos}
BuildRequires: python3
%else
BuildRequires: python3-libmount
BuildRequires: python
%endif
BuildRequires: git-core
BuildRequires: libcap-devel
BuildRequires: systemd-devel
BuildRequires: yajl-devel
BuildRequires: libseccomp-devel
BuildRequires: libselinux-devel
BuildRequires: libtool
BuildRequires: make
BuildRequires: glibc-static
%if ! 0%{?centos}
%ifnarch %ix86
BuildRequires: criu-devel >= 3.15
%endif
%endif
Provides: oci-runtime

%description
crun is a runtime for running OCI containers.
This version is enabled for wasmtime.

%prep
%autosetup -p1 -n %{name}-%{version}

%build
./autogen.sh
%configure --disable-silent-rules --with-wasmtime

%make_build

%install
%make_install
rm -rf $RPM_BUILD_ROOT/usr/lib*

%files
%license COPYING
%{_bindir}/%{name}
%{_mandir}/man1/*

%changelog
* Mon Mar 25 2024 Dan Bryant <daniel.bryant@linux.com> - 1.14.4-1
- Version bump

* Wed Jun 09 2021 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0.20.1-1
- Fixes: https://github.com/containers/crun/issues/687

* Wed Jun 02 2021 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0.20-1
- bump to 0.20

* Mon May 17 2021 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0.19.1-3
- rebuild to fix prior build downgrades

* Fri May 07 2021 RH Container Bot <rhcontainerbot@fedoraproject.org> - 0.19.1-1
- autobuilt 0.19.1

* Thu Apr 22 2021 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0.19.1-2
- rebuild for new bodhi

* Thu Apr 22 2021 Giuseppe Scrivano <gscrivan@redhat.com> - 0.19.1-1
- built version 0.19.1

* Tue Apr 13 2021 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0.19-2
- unversioned Provides: oci-runtime
- runc package will also provide an unversioned Provides: oci-runtime.
- user should pull in runc separately or else it will install crun by default
 (alphabetical order)
- similar situation as caddy, httpd, lighttpd and nginx having Provides:
webserver

* Tue Apr 06 2021 Giuseppe Scrivano <gscrivan@redhat.com> - 0.19-1
- built version 0.19

* Wed Mar 31 2021 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0.18-5
- linux: always remount bind mounts ghpr#640

* Thu Mar 25 2021 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0.18-4
- Requires: libcap >= 2.48

* Thu Feb 25 2021 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0.18-3
- bump for centos

* Wed Feb 24 2021 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0.18-2
- bump to make centos happy

* Fri Feb 19 2021 Giuseppe Scrivano <gscrivan@redhat.com> - 0.18-1
- built version 0.18

* Thu Feb 04 2021 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0.17-3
- use deprecated changelog format

* Thu Feb 04 2021 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0.17-2
- bump for centos on obs

* Thu Jan 21 2021 Giuseppe Scrivano <gscrivan@redhat.com> - 0.17-1
- built version 0.17

* Thu Dec 17 2020 Giuseppe Scrivano <gscrivan@redhat.com> - 0.16-3
- build with CRIU

* Wed Nov 25 2020 Jindrich Novy <jnovy@redhat.com> - 0.16-2
- fix license

* Tue Nov 24 2020 Giuseppe Scrivano <gscrivan@redhat.com> - 0.16-1
- built version 0.16

* Wed Nov 04 2020 Giuseppe Scrivano <gscrivan@redhat.com> - 0.15.1-1
- built version 0.15.1

* Wed Sep 30 2020 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0.15-5
- rebuild to bump release tag ahead of older fedoras

* Wed Sep 30 2020 Giuseppe Scrivano <gscrivan@redhat.com> - 0.15-4
- backport "exec: check read bytes from sync"

* Thu Sep 24 2020 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0.15-3
- release tag ahead of f32

* Wed Sep 23 2020 RH Container Bot <rhcontainerbot@fedoraproject.org> - 0.15-1
- autobuilt 0.15

* Wed Sep 23 2020 Giuseppe Scrivano <gscrivan@redhat.com> - 0.15-2
- rebuild

* Wed Sep 23 2020 RH Container Bot <rhcontainerbot@fedoraproject.org> - 0.15-1
- autobuilt 0.15

* Mon Sep 14 2020 Giuseppe Scrivano <gscrivan@redhat.com> - 0.14.1-5
- backport 4453af4c060e380051552ee589af5cad37f2ae82

* Fri Sep 11 2020 RH Container Bot <rhcontainerbot@fedoraproject.org> - 0.14.1-1
- autobuilt 0.14.1

* Mon Aug 31 2020 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0.14.1-4
- rebuild

* Thu Aug 27 2020 Giuseppe Scrivano <gscrivan@redhat.com> - 0.14.1-3
- backport ed9c3e6f466dfb6d2e79802060fabd5f4b66f78e

* Mon Aug 17 2020 RH Container Bot <rhcontainerbot@fedoraproject.org> - 0.14.1-1
- autobuilt 0.14.1

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 08 2020 Giuseppe Scrivano <gscrivan@redhat.com> - 0.14.1-1
- built version 0.14.1

* Thu Jul 02 2020 Giuseppe Scrivano <gscrivan@redhat.com> - 0.14-1
- built version 0.14

* Wed Apr 15 2020 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0.13-2
- release bump for correct upgrade path

* Thu Mar 05 2020 Giuseppe Scrivano <gscrivan@redhat.com> - 0.13-1
- built version 0.13

* Mon Feb 17 2020 Giuseppe Scrivano <gscrivan@redhat.com> - 0.12.2.1-1
- built version 0.12.2.1

* Mon Feb 17 2020 Giuseppe Scrivano <gscrivan@redhat.com> - 0.12.2-1
- built version 0.12.2

* Thu Feb 6 2020 Giuseppe Scrivano <gscrivan@redhat.com> - 0.12.1-1
- built version 0.12.1

* Mon Feb 3 2020 Giuseppe Scrivano <gscrivan@redhat.com> - 0.12-1
- built version 0.12

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Dec 23 2019 Giuseppe Scrivano <gscrivan@redhat.com> - 0.11-1
- built version 0.11

* Mon Nov 18 2019 Giuseppe Scrivano <gscrivan@redhat.com> - 0.10.6-1
- built version 0.10.6

* Sun Nov 10 2019 Giuseppe Scrivano <gscrivan@redhat.com> - 0.10.5-2
- built version 0.10.5
- fix CVE-2019-18837

* Sun Nov 10 2019 Giuseppe Scrivano <gscrivan@redhat.com> - 0.10.5-1
- built version 0.10.5

* Thu Oct 31 2019 Giuseppe Scrivano <gscrivan@redhat.com> - 0.10.4-1
- built version 0.10.4

* Tue Oct 29 2019 Giuseppe Scrivano <gscrivan@redhat.com> - 0.10.3-1
- built version 0.10.3

* Mon Oct 7 2019 Giuseppe Scrivano <gscrivan@redhat.com> - 0.10.2-1
- built version 0.10.2

* Fri Oct 4 2019 Giuseppe Scrivano <gscrivan@redhat.com> - 0.10.1-1
- built version 0.10.1

* Tue Oct 1 2019 Giuseppe Scrivano <gscrivan@redhat.com> - 0.10-1
- built version 0.10

* Fri Sep 13 2019 Giuseppe Scrivano <gscrivan@redhat.com> - 0.9.1-1
- built version 0.9.1

* Wed Sep 11 2019 Giuseppe Scrivano <gscrivan@redhat.com> - 0.9-1
- built version 0.9

* Tue Sep 10 2019 Jindrich Novy <jnovy@redhat.com> - 0.8-3
- Add versioned oci-runtime provide.

* Mon Sep 9 2019 Dan Walsh <dwalsh@redhat.com> - 0.8-2
- Add provides oci-runtime

* Mon Aug 19 2019 Giuseppe Scrivano <gscrivan@redhat.com> - 0.8-1
- built version 0.8

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jul 18 2019 Giuseppe Scrivano <gscrivan@redhat.com> - 0.7-1
- built version 0.7

* Tue Jun 18 2019 Giuseppe Scrivano <gscrivan@redhat.com> - 0.6-1
- built version 0.6
