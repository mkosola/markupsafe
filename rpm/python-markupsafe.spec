Name: python-markupsafe
Version: 0.18
Release: 1
Summary: Implements a XML/HTML/XHTML Markup safe string for Python
Group: Development/Languages
License: BSD
URL: http://pypi.python.org/pypi/MarkupSafe
Source0: %{name}-%{version}.tar.gz

BuildRequires: python-devel python-setuptools

%description
A library for safe markup escaping.

%prep
%setup -q -n %{name}-%{version}

%build
cd markupsafe
CFLAGS="$RPM_OPT_FLAGS" %{__python} setup.py build

%install
cd markupsafe
rm -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root %{buildroot}

%check
cd markupsafe
%{__python} setup.py test

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc markupsafe/AUTHORS markupsafe/LICENSE markupsafe/README.rst
%{python_sitearch}/*
