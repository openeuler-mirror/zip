Name:            zip
Version:         3.0
Release:         24
Summary:         A compression and file packaging/archive utility
License:         BSD
URL:             http://www.info-zip.org/Zip.html
Source0:         http://downloads.sourceforge.net/infozip/zip30.tar.gz

# Patch1 to patch6 get from fedora
Patch1:          zip-3.0-exec-shield.patch
Patch2:          zip-3.0-currdir.patch
Patch3:          zip-3.0-time.patch
Patch4:          man.patch
Patch5:          zip-3.0-format-security.patch
Patch6:          zipnote.patch

Patch6000:       CVE-2018-13410.patch

BuildRequires:   bzip2-devel
Requires:        unzip

%description
The zip program is a compression and file packaging utility. Zip has one
compression method and can also store files without compression.
Zip automatically chooses the better of the two for each file. Compression
ratios of 2:1 to 3:1 are common for text files.

%package         help
Summary:         Documents and manuals related to zip
BuildArch:       noarch

%description     help
This package contains the documents and manuals related to zip.

%prep
%autosetup -n zip30 -p1

%build
%make_build -f unix/Makefile prefix=%{_prefix} "CFLAGS_NOOPT=-I. -DUNIX $RPM_OPT_FLAGS" generic_gcc

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_mandir}/man1
%make_install -f unix/Makefile prefix=%{buildroot}%{_prefix} MANDIR=%{buildroot}%{_mandir}/man1

%files
%defattr(-,root,root)
%doc README CHANGES TODO WHATSNEW WHERE README.CR
%doc proginfo/algorith.txt
%license LICENSE
%{_bindir}/zip*

%files help
%{_mandir}/man1/zip*

%changelog
* Tue Sep 3 2019 dongjian <dongjian13@huawei.com> - 3.0-24
- Rebuild and modify the description