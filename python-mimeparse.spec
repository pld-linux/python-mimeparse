#
# Conditional build:
%bcond_without	python2		# Python 2.x module
%bcond_without	python3		# Python 3.x module
%bcond_without	tests		# tests run

%define		module mimeparse
Summary:	Python 2.x module for parsing mime-type names
Summary(pl.UTF-8):	Moduł Pythona 2.x do analizy nazw typów MIME
Name:		python-%{module}
Version:	1.6.0
Release:	8
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/pypi/python-mimeparse/
Source0:	https://files.pythonhosted.org/packages/source/p/python-mimeparse/%{name}-%{version}.tar.gz
# Source0-md5:	a32ae1df93be1ddb581d1c0fa124bab4
URL:		https://github.com/dbtsai/python-mimeparse
%if %{with python2}
BuildRequires:	python-devel >= 1:2.7
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-devel >= 1:3.2
BuildRequires:	python3-setuptools
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides basic functions for parsing mime-type names and
matching them against a list of media-ranges.

%description -l pl.UTF-8
Ten moduł udostępnia podstawowe funkcje do analizy nazw typów MIME
oraz dopasowywania ich do listy zakresów mediów.

%package -n python3-%{module}
Summary:	Python 3.x module for parsing mime-type names
Summary(pl.UTF-8):	Moduł Pythona 3.x do analizy nazw typów MIME
Group:		Libraries/Python

%description -n python3-%{module}
This module provides basic functions for parsing mime-type names and
matching them against a list of media-ranges.

%description -n python3-%{module} -l pl.UTF-8
Ten moduł udostępnia podstawowe funkcje do analizy nazw typów MIME
oraz dopasowywania ich do listy zakresów mediów.

%prep
%setup -q

%build
%if %{with python2}
%py_build

%if %{with tests}
cd build-2
ln -sf ../testdata.json .
%{__python} ../mimeparse_test.py
cd ..
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
cd build-3
ln -sf ../testdata.json .
%{__python3} ../mimeparse_test.py
cd ..
%endif
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc LICENSE README.rst
%{py_sitescriptdir}/mimeparse.py[co]
%{py_sitescriptdir}/python_mimeparse-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc LICENSE README.rst
%{py3_sitescriptdir}/mimeparse.py
%{py3_sitescriptdir}/__pycache__/mimeparse.*.py[co]
%{py3_sitescriptdir}/python_mimeparse-%{version}-py*.egg-info
%endif
