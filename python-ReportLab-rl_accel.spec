%define		_snap	20070412
Summary:	A C coded extension accelerator for the ReportLab Toolkit
Summary(pl.UTF-8):	Napisany w C akcelerator rozszerzeń dla toolkitu ReportLab
Name:		python-ReportLab-rl_accel
Version:	0.60
Release:	1
License:	distributable
Group:		Libraries/Python
Source0:	http://www.reportlab.org/daily/rl_accel-%{version}-daily-unix.tgz
# Source0-md5:	3ab351d94797eda2ef77d6b88426597f
URL:		http://www.reportlab.org/
BuildRequires:	python-devel >= 1:2.4
%pyrequires_eq	python
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A C coded extension accelerator for the ReportLab Toolkit.

%description -l pl.UTF-8
Napisany w C akcelerator rozszerzeń dla toolkitu ReportLab.

%prep
%setup -q -n rl_accel-%{version}-%{_snap}

%build
cd rl_accel
CFLAGS="%{rpmcflags}"; export CFLAGS
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
cd rl_accel
python setup.py install \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/*.so
