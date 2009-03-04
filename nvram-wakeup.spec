#
Summary:	Read and write the WakeUp time in the BIOS
Name:		nvram-wakeup
Version:	0.99b
Release:	1
License:	GPL v2+
Group:		Applications/System
Source0:	http://dl.sourceforge.net/nvram-wakeup/nvram-wakup-%{version}.tar.gz
# Source0-md5:	a668132b1daa9c4c48f4ed45b95f3df0
Patch0:		%{name}-no_time_helper.patch
URL:		http://sourceforge.net/projects/nvram-wakeup
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a small program that reads and writes the WakeUp time in the BIOS. This
is done via /dev/nvram on recent kernels (>2.4.6, including 2.6.x) or,
alternatively, via direct ISA access. On this WakeUp time the computer is
powered on automatically. 

%prep
%setup -qn nvram-wakup-%{version}

%build
%{__make} \
	prefix="%{_prefix}" \
	CC="%{__cc}" \
	CFLAGS="-Wall %{rpmcflags} -D_GNU_SOURCE" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	prefix="$RPM_BUILD_ROOT%{_prefix}" \
	MANDIR="$RPM_BUILD_ROOT%{_mandir}" 

rm -rf $RPM_BUILD_ROOT/%{_docdir}
%find_lang %{name} --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README* HISTORY nvram-wakeup.conf
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_sbindir}/*
%{_mandir}/man8/*
%{_mandir}/man5/*
