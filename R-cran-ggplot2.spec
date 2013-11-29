%define		fversion	%(echo %{version} |tr r -)
%define		modulename	ggplot2
Summary:	Fast hierarchical clustering routines for R and Python
Name:		R-cran-%{modulename}
Version:	0.9.3.1
Release:	1
License:	GPL v2
Group:		Applications/Math
Source0:	ftp://stat.ethz.ch/R-CRAN/src/contrib/%{modulename}_%{fversion}.tar.gz
# Source0-md5:	f01d950c6385750e737ac7eac6260c87
URL:		http://cran.fhcrc.org/web/packages/ggplot2/index.html
BuildRequires:	R >= 2.8.1
BuildRequires:	R-cran-digest
BuildRequires:	R-cran-gtable
BuildRequires:	R-cran-reshape2
BuildRequires:	R-cran-proto
BuildRequires:	R-cran-plyr
BuildRequires:	R-cran-scales
Requires(post,postun):	R >= 2.8.1
Requires(post,postun):	perl-base
Requires(post,postun):	textutils
Requires:	R
Requires:	R-cran-digest
Requires:	R-cran-gtable
Requires:	R-cran-reshape2
Requires:	R-cran-proto
Requires:	R-cran-plyr
Requires:	R-cran-scales
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
An implementation of the grammar of graphics in R. It combines the
advantages of both base and lattice graphics: conditioning and shared
axes are handled automatically, and you can still build up a plot step
by step from multiple data sources. It also implements a sophisticated
multidimensional conditioning system and a consistent interface to map
data to aesthetic attributes. See the ggplot2 website for more
information, documentation and examples.

%prep
%setup -q -c

%build
R CMD build %{modulename}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/R/library/
R CMD INSTALL %{modulename} --library=$RPM_BUILD_ROOT%{_libdir}/R/library/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{modulename}/DESCRIPTION
%{_libdir}/R/library/%{modulename}
