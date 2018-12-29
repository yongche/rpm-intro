Name:     hello
Version:  2.1
Release:  1%{?dist}
Summary:  The "Hello World" program from GNU
Summary(zh_CN):  GNU "Hello World"
License:  GPLv3+
URL:      http://ftp.gnu.org/gnu/hello
Source0:  http://ftp.gnu.org/gnu/hello/%{name}-%{version}.tar.gz

%description
The "Hello World" program, done with all bells and whistles of a proper FOSS
project, including configuration, build, internationalization, help files, etc.

%description -l zh_CN
"Hello World"

%prep
%setup -q


%build
%configure
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}


%files
%doc

%changelog
* Sat Dec 29 2018 zhangchunsheng<zhangchunsheng@yongche.com> - 2.10-1
- hello