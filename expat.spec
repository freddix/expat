# based on PLD Linux spec git://git.pld-linux.org/packages/expat.git
Summary:	XML 1.0 parser
Name:		expat
Version:	2.1.0
Release:	3
Epoch:		1
License:	Thai Open Source Software Center Ltd (distributable)
Group:		Applications/Publishing/XML
Source0:	http://downloads.sourceforge.net/expat/%{name}-%{version}.tar.gz
# Source0-md5:	dd7dab7a5fea97d2a6a43f511449b7cd
URL:		http://expat.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Expat is an XML parser written in C. It aims to be fully conforming.
It is currently not a validating XML parser.

%package devel
Summary:	Expat header files
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description devel
Expat header files.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__autoconf}
%configure \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /usr/sbin/ldconfig
%postun -p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc COPYING Changes README
%attr(755,root,root) %{_bindir}/xmlwf
%attr(755,root,root) %ghost %{_libdir}/libexpat.so.?
%attr(755,root,root) %{_libdir}/libexpat.so.*.*.*
%{_mandir}/man1/xmlwf.1*

%files devel
%defattr(644,root,root,755)
%doc doc/{reference.html,style.css}
%attr(755,root,root) %{_libdir}/libexpat.so
%{_includedir}/expat*.h
%{_pkgconfigdir}/*.pc

