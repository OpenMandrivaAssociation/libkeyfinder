%define major	2
%define libname	%mklibname keyfinder
%define devname	%mklibname keyfinder -d

Name:		libkeyfinder
Summary:	Musical key detection for digital audio
Version:	2.2.8
Release:	1
License:	GPLv3+
Group:		System/Libraries
Url:		https://mixxxdj.github.io/libkeyfinder/
Source0:	https://github.com/mixxxdj/libkeyfinder/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:	cmake
BuildRequires:	pkgconfig(fftw3)
BuildRequires:	pkgconfig(catch2)

%description
libkeyfinder is a small C++11 library for estimating the
musical key of digital audio.

%package -n %{libname}
Summary:	Shared libraries for libkeyfinder
Group:		System/Libraries

%description -n %{libname}
libkeyfinder is a small C++11 library for estimating the
musical key of digital audio.

%package -n %{devname}
Summary:	Development libraries and header files for libkeyfinder
Group:		Development/Other
Requires:	%{libname} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}

%description -n %{devname}
This package contains the development libraries and header files for
libkeyfinder.

%prep
%autosetup -p1

%build
%cmake
%make_build

%install
%make_install -C build

%files -n %{libname}
%license LICENSE
%doc README.md
%{_libdir}/libkeyfinder.so.%{major}{,.*}

%files -n %{devname}
%doc CHANGELOG.md
%{_includedir}/keyfinder/
%{_libdir}/cmake/KeyFinder/
%{_libdir}/pkgconfig/libkeyfinder.pc
%{_libdir}/libkeyfinder.so
