#
# Conditional build:
%bcond_without	python3	# Python3

%define		module mimeparse
Summary:	Python module for parsing mime-type names
Name:		python-%{module}
Version:	0.1.3
Release:	2
License:	MIT
Group:		Libraries/Python
URL:		https://mimeparse.googlecode.com/
Source0:	https://mimeparse.googlecode.com/files/%{module}-%{version}.tar.gz
# Source0-md5:	03ce207391454db37279e78ce2112365
BuildRequires:	python-devel
%{?with_python3:BuildRequires:	python3-devel}
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides basic functions for parsing mime-type names and
matching them against a list of media-ranges.

%package -n python3-%{module}
Summary:	Python module for parsing mime-type names
Group:		Libraries/Python

%description -n python3-%{module}
This module provides basic functions for parsing mime-type names and
matching them against a list of media-ranges.

%prep
%setup -q -n %{module}-%{version}

%build
%{__python} setup.py build --build-base py2

%if %{with python3}
%{__python3} setup.py build --build-base py3
%endif

%if %{with tests}
%{__python} mimeparse_test.py

%if %{with python3}
cd py3
%{__python3} mimeparse_test.py
%endif
%endif

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py build \
	--build-base py2 \
	install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%py_postclean

%if %{with python3}
%{__python3} setup.py build \
	--build-base py3 \
	install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{py_sitescriptdir}/mimeparse.py[co]
%{py_sitescriptdir}/mimeparse-%{version}-py*.egg-info

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc README
%{py3_sitescriptdir}/__pycache__/mimeparse.*.py[co]
%{py3_sitescriptdir}/mimeparse-%{version}-py*.egg-info
%{py3_sitescriptdir}/mimeparse.py
%endif
