Name:    f3
Version: 8.0
Release: 1
Summary: Utility to test for fake flash drives and cards
License: GPLv3
Group:   System/Kernel and hardware
URL:     https://oss.digirati.com.br/%{name}/
Source:  https://github.com/AltraMayor/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires: pkgconfig(libparted)
BuildRequires: pkgconfig(systemd)

%description
F3 is a utility to test for fake flash drives and cards. It is a Free
Software alternative to h2testw.  f3write will fill the unused part of
a filesystem with files NNNN.fff with known content, and f3read will
analyze the files to determine whether the contents are corrupted, as
happens with fake flash.

%prep
%autosetup

%build
%make_build all extra

%install
%make_install install-extra PREFIX=%{_prefix}

%files
%license LICENSE
%{_bindir}/f3read
%{_bindir}/f3write
%{_bindir}/f3brew
%{_bindir}/f3fix
%{_bindir}/f3probe
%{_datadir}/man/man1/f3read.1.*
%{_datadir}/man/man1/f3write.1.*
