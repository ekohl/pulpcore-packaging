# Created by pyp2rpm-3.3.3
%global pypi_name MarkupSafe
%global srcname markupsafe

Name:           python-%{srcname}
Version:        1.1.1
Release:        2%{?dist}
Summary:        Safely add untrusted strings to HTML/XML markup

License:        BSD-3-Clause
URL:            https://palletsprojects.com/p/markupsafe/
Source0:        https://files.pythonhosted.org/packages/source/M/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description
%{summary}

%package -n     python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
%{summary}

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{srcname}
%license LICENSE.rst docs/license.rst
%doc README.rst
%{python3_sitearch}/markupsafe
%{python3_sitearch}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Fri Feb 28 2020 Zach Huntington-Meath <zhunting@redhat.com> - 1.1.1-2
- Bump release to build for el8

* Mon Nov 18 2019 Evgeni Golov - 1.1.1-1
- Initial package.
