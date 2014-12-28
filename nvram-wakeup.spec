Summary:	Read and write the WakeUp time in the BIOS
Summary(pl.UTF-8):	Odczyt i zapis czasu pobudki (WakeUp) w BIOS-ie
Name:		nvram-wakeup
Version:	1.1
Release:	1
License:	GPL v2+
Group:		Applications/System
Source0:	http://downloads.sourceforge.net/nvram-wakeup/nvram-wakup-%{version}.tar.gz
# Source0-md5:	ebd6e276167ba4351ecb1ea2bd368422
Patch0:		%{name}-no_time_helper.patch
URL:		http://sourceforge.net/projects/nvram-wakeup/
BuildRequires:	gettext-tools
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a small program that reads and writes the WakeUp time in the
BIOS. This is done via /dev/nvram on recent kernels (>2.4.6, including
2.6.x) or, alternatively, via direct ISA access. On this WakeUp time
the computer is powered on automatically. 

%description -l pl.UTF-8
Ten mały program odczytuje i zapisuje czas pobudki (WakeUp) w BIOS-ie.
Dokonuje tego poprzez /dev/nvram na nowszych jądrach Linuksa (>2.4.6,
w tym 2.6.x) lub poprzez bezpośredni dostęp do ISA. O zadanym czasie
pobudki (WakeUp) komputer jest uruchamiany automatycznie.

%prep
%setup -q -n nvram-wakup-%{version}

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

%{__rm} -r $RPM_BUILD_ROOT%{_docdir}
%find_lang %{name} --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README* HISTORY nvram-wakeup.conf
%attr(755,root,root) %{_bindir}/nvram-wakeup
%attr(755,root,root) %{_bindir}/vdrshutdown
%attr(755,root,root) %{_sbindir}/biosinfo
%attr(755,root,root) %{_sbindir}/cat_nvram
%attr(755,root,root) %{_sbindir}/guess
%attr(755,root,root) %{_sbindir}/guess-helper
%attr(755,root,root) %{_sbindir}/rtc
%attr(755,root,root) %{_sbindir}/time
%{_mandir}/man5/nvram-wakeup.conf.5*
%{_mandir}/man8/biosinfo.8*
%{_mandir}/man8/cat_nvram.8*
%{_mandir}/man8/guess.8*
%{_mandir}/man8/guess-helper.8*
%{_mandir}/man8/nvram-wakeup.8*
%{_mandir}/man8/rtc.8*
%{_mandir}/man8/set_timer.8*
%{_mandir}/man8/time.8*
