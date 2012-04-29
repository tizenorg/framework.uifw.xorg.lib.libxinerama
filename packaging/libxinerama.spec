
Name:       libxinerama
Summary:    X.Org X11 libXinerama runtime library
Version:    1.1.1
Release:    2.6
Group:      System/Libraries
License:    MIT/X11
URL:        http://www.x.org
Source0:    http://xorg.freedesktop.org/archive/individual/lib/%{name}-%{version}.tar.gz
Requires(post):  /sbin/ldconfig
Requires(postun):  /sbin/ldconfig
BuildRequires:  pkgconfig(xproto)
BuildRequires:  pkgconfig(xextproto)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xineramaproto)
BuildRequires:  pkgconfig(xorg-macros)

%description
X.Org X11 libXinerama runtime library


%package devel
Summary:    X.Org X11 libXinerama development package
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}

%description devel
X.Org X11 libXinerama development package


%prep
export LDFLAGS+=" -Wl,--hash-style=both -Wl,--as-needed"
%setup -q -n %{name}-%{version}


%build

%reconfigure --disable-static

# Call make instruction with smp support
make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install


%clean
rm -rf %{buildroot}



%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig



%files
%defattr(-,root,root,-)
%doc COPYING
%{_libdir}/libXinerama.so.1
%{_libdir}/libXinerama.so.1.0.0


%files devel
%defattr(-,root,root,-)
%doc README ChangeLog
%{_includedir}/X11/extensions/*.h
%{_libdir}/libXinerama.so
%{_libdir}/pkgconfig/xinerama.pc
%{_mandir}/man3/*.3*

