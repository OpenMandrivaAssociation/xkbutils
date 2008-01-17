Name:		xkbutils
Version:	1.0.1
Release:	%mkrel 7
Summary:	X.Org X11 XKB utilities
Group:		Development/X11
Source:		http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
License:	MIT
BuildRoot:	%{_tmppath}/%{name}-root

BuildRequires:	x11-util-macros		>= 1.1.5
BuildRequires:	libxaw-devel		>= 1.0.4
BuildRequires:	libxkbfile-devel	>= 1.0.4

%description
This package provides several XKB utilities for X.org.

%prep
%setup -q -n %{name}-%{version}

%build
%configure	--x-includes=%{_includedir} \
		--x-libraries=%{_libdir}

%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/xkbbell
%{_bindir}/xkbvleds
%{_bindir}/xkbwatch
