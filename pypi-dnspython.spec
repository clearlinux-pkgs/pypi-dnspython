#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xF24B3AFC8CA2F5C7 (halley@dnspython.org)
#
Name     : pypi-dnspython
Version  : 2.1.0
Release  : 71
URL      : https://files.pythonhosted.org/packages/13/27/5277de856f605f3429d752a39af3588e29d10181a3aa2e2ee471d817485a/dnspython-2.1.0.zip
Source0  : https://files.pythonhosted.org/packages/13/27/5277de856f605f3429d752a39af3588e29d10181a3aa2e2ee471d817485a/dnspython-2.1.0.zip
Source1  : https://files.pythonhosted.org/packages/13/27/5277de856f605f3429d752a39af3588e29d10181a3aa2e2ee471d817485a/dnspython-2.1.0.zip.asc
Summary  : DNS toolkit
Group    : Development/Tools
License  : ISC
Requires: pypi-dnspython-license = %{version}-%{release}
Requires: pypi-dnspython-python = %{version}-%{release}
Requires: pypi-dnspython-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(poetry)
BuildRequires : pypi-pytest
Patch1: 0001-Disable-broken-test.patch

%description
record types. It can be used for queries, zone transfers, and dynamic
        updates.  It supports TSIG authenticated messages and EDNS0.
        
        dnspython provides both high and low level access to DNS. The high
        level classes perform queries for data of a given name, type, and
        class, and return an answer set.  The low level classes allow
        direct manipulation of DNS zones, messages, names, and records.

%package license
Summary: license components for the pypi-dnspython package.
Group: Default

%description license
license components for the pypi-dnspython package.


%package python
Summary: python components for the pypi-dnspython package.
Group: Default
Requires: pypi-dnspython-python3 = %{version}-%{release}

%description python
python components for the pypi-dnspython package.


%package python3
Summary: python3 components for the pypi-dnspython package.
Group: Default
Requires: python3-core
Provides: pypi(dnspython)

%description python3
python3 components for the pypi-dnspython package.


%prep
%setup -q -n dnspython-2.1.0
cd %{_builddir}/dnspython-2.1.0
%patch1 -p1
pushd ..
cp -a dnspython-2.1.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1653058836
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
cd tests; make test
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-dnspython
cp %{_builddir}/dnspython-2.1.0/LICENSE %{buildroot}/usr/share/package-licenses/pypi-dnspython/66db5e89fe8fe8e61165a511e71966e84b6b0102
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot}/usr/share/clear/optimized-elf/ %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-dnspython/66db5e89fe8fe8e61165a511e71966e84b6b0102

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
