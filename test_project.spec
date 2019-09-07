Name:			test_spec
Version:		1.0
Release:		1
Summary:		pratise to make rpm

Group: 			System Environment/System
License:		GPL
URL: 			https://www.cnblogs.com/luohaixian/

Source0:		test_project.tar.gz
Source1:		xxx

BuildArch:		x86_64
BuildRequires:  	python-setuptools

%description
pratise to make rpm
rpm1 c program
rpm2 python program

%package -n 		rpm1
Summary:		make rpm1

Requires:   		gcc

%description -n 	rpm1
xxxxxx

%package -n 		rpm2
Summary:		make rpm2

%description -n 	rpm2
xxxxxx

%prep
%setup -q -n test_project

%build
pushd c_program
make
popd

pushd python_program
%{__python2} setup.py build
popd

%install
mkdir -p %{buildroot}%{_bindir}
install -m 755 $RPM_BUILD_DIR/test_project/c_program/main %{buildroot}%{_bindir}/
pushd python_program
%{__python2} setup.py install --root=%{buildroot}
popd

%post -n		rpm1


%post -n		rpm2


%files -n 		rpm1
%{_bindir}/main


%files -n 		rpm2
%{python2_sitelib}/python_program*


%changelog
* Fri Sep 09 2019 <email> 1.0
- create spec
