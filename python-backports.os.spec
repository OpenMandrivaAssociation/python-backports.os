# Created by pyp2rpm-3.3.2
%global pypi_name backports.os

Name:           python-%{pypi_name}
Version:        0.1.1
Release:        2
Summary:        Backport of new features in Python's os module
Group:          Development/Python
License:        Python Software Foundation License
URL:            https://github.com/pjdelport/backports.os
Source0:        https://files.pythonhosted.org/packages/source/b/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(setuptools-scm)
# for tests
BuildRequires:  python3dist(future)

%description
This package provides backports of new features in Python's os_ module
under the backports_ namespace.

%prep
%autosetup -n %{pypi_name}-%{version}

# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py_build

%install
%py_install
rm -fr %{buildroot}/%{python_sitelib}/backports/{__init__.py*,__pycache__}

%check
%{__python} setup.py test

%files
%license LICENSE
%doc README.rst
%{python_sitelib}/backports
%{python_sitelib}/%{pypi_name}-%{version}-py*.*.egg-info
