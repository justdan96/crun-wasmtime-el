%global with_debug 1
%global with_check 0

%if 0%{?with_debug}
%global _find_debuginfo_dwz_opts %{nil}
%global _dwz_low_mem_die_limit 0
%else
%global debug_package %{nil}
%endif

%global built_tag v2.1.10
%global built_tag_strip %(b=%{built_tag}; echo ${b:1})
%global gen_version %(b=%{built_tag_strip}; echo ${b/-/"~"})

Name: conmon
Epoch: 2
Version: %{gen_version}
Release: 1%{?dist}
Summary: OCI container runtime monitor
License: ASL 2.0
URL: https://github.com/containers/conmon
Source0: %{url}/archive/%{built_tag}.tar.gz
BuildRequires: gcc
BuildRequires: git
BuildRequires: glib2-devel
BuildRequires: libseccomp-devel
BuildRequires: systemd-devel
BuildRequires: systemd-libs
BuildRequires: make
Requires: glib2
Requires: systemd-libs
Requires: libseccomp

%description
%{summary}.

%prep
%autosetup -Sgit -n %{name}-%{built_tag_strip}
sed -i 's/install.bin: bin\/conmon/install.bin:/' Makefile
sed -i 's/install.crio: bin\/conmon/install.crio:/' Makefile

%build
%{__make} DEBUGFLAG="-g" bin/conmon

%install
%{__make} PREFIX=%{buildroot}%{_prefix} install.bin install.crio

#define license tag if not already defined
%{!?_licensedir:%global license %doc}

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_libexecdir}/crio/%{name}
%dir %{_libexecdir}/crio

%changelog
* Mon Mar 25 2024 Dan Bryant <daniel.bryant@linux.com> - 2.1.10-1
- Version bump

* Fri Jun 17 2022 Peter Hunt <pehunt@redhat.com> - 2:2.1.2-1
- bump to v2.1.2

* Thu Mar 17 2022 Peter Hunt <pehunt@redhat.com> - 2:2.1.0-2
- bump to v2.1.0

* Thu Jun 03 2021 RH Container Bot <rhcontainerbot@fedoraproject.org> - 2:2.0.29-1
- autobuilt v2.0.29
