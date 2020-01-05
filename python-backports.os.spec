# Created by pyp2rpm-3.3.2
%global pypi_name backports.os

Name:           python-%{pypi_name}
Version:        0.1.1
Release:        %mkrel 6
Summary:        Backport of new features in Python's os module
Group:          Development/Python
License:        Python Software Foundation License
URL:            https://github.com/pjdelport/backports.os
Source0:        https://files.pythonhosted.org/packages/source/b/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(setuptools-scm)
# for tests
BuildRequires:  python3dist(future)

%description
This package provides backports of new features in Python's os_ module
under the backports_ namespace.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
Group:          Development/Python
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
This package provides backports of new features in Python's os_ module
under the backports_ namespace.

%prep
%autosetup -n %{pypi_name}-%{version}

# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install
rm -fr %{buildroot}/%{python3_sitelib}/backports/{__init__.py*,__pycache__}

%check
%{__python3} setup.py test

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/backports
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info
