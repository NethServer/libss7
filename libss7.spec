Summary: Libss7, an open source implementation of Signalling System 7 (SS7)
Name: libss7
Version: 2.0.0
Release: 1%{dist}
License: GPL
Group: Utilities/System
Source: https://downloads.asterisk.org/pub/telephony/libss7/libss7-2.0.0.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-root
URL: http://www.asterisk.org
Packager: NethServer <info@nethesis.it>

%description
libss7 is a C implementation of the Signalling System 7 (SS7) specification.  

%package devel
Summary: Libss7 libraries and header files for libss7 development
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
The static libraries and header files needed for building additional plugins/modules

%prep
%setup -n %{name}-%{version}

%build
echo %{version} > .version
make

%install
make DESTDIR=$RPM_BUILD_ROOT install

%post
ldconfig

%clean
cd $RPM_BUILD_DIR
%{__rm} -rf %{name}-%{version} 
%{__rm} -rf /var/log/%{name}-sources-%{version}-%{release}.make.err
%{__rm} -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
%{_prefix}/lib/libss7.so
%{_prefix}/lib/libss7.so.2.0

%files devel
%defattr(-, root, root)
%{_includedir}/libss7.h
%{_prefix}/lib/libss7.a
