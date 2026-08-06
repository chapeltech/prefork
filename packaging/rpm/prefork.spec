Name:           prefork
Version:        0.4
Release:        1%{?dist}
Summary:        Preforking helper for inetd-style services
License:        MIT
URL:            https://github.com/ChapelTech/prefork
Source0:        prefork-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  groff-base

%description
prefork is a small helper for running inetd-style services with a pool of
preforked worker processes.

%prep
%autosetup

%build
%make_build CFLAGS="%{optflags}" NROFF=/usr/bin/nroff

%install
install -Dpm0755 prefork %{buildroot}%{_libexecdir}/prefork
install -Dpm0644 prefork.8 %{buildroot}%{_mandir}/man8/prefork.8

%files
%license debian/copyright
%{_libexecdir}/prefork
%{_mandir}/man8/prefork.8*

%changelog
* Thu Aug 06 2026 ChapelTech <packages@chapel.tech> - 0.4-1
- Add Alpine package builds and use the shared package release workflow.

* Wed Aug 05 2026 ChapelTech <packages@chapel.tech> - 0.3-2
- Publish signed EL9 RPMs as a new package revision.

* Wed Aug 05 2026 ChapelTech <packages@chapel.tech> - 0.3-1
- Add Rocky/RHEL packaging.
