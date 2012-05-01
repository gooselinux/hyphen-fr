Name: hyphen-fr
Summary: French hyphenation rules
Version: 2.0
Release: 2.1%{?dist}
Source: http://download.tuxfamily.org/dicollecte2/hyph_fr_FR_2-0.zip
Group: Applications/Text
URL: http://dicollecte.tuxfamily.org/home.php?prj=fr
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
License: LGPLv2+
BuildArch: noarch

Requires: hyphen

%description
French hyphenation rules.

%prep
%setup -q -c

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/hyphen
cp -p *.dic $RPM_BUILD_ROOT/%{_datadir}/hyphen

pushd $RPM_BUILD_ROOT/%{_datadir}/hyphen/
fr_FR_aliases="fr_BE fr_CA fr_CH fr_LU fr_MC"
for lang in $fr_FR_aliases; do
        ln -s hyph_fr_FR.dic hyph_$lang.dic
done
popd

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc README_hyph_fr_FR.txt
%{_datadir}/hyphen/*

%changelog
* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 2.0-2.1
- Rebuilt for RHEL 6

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat May 23 2009 Caolan McNamara <caolanm@redhat.com> - 2.0-1
- initial version

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20080318-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Dec 31 2008 Caolan McNamara <caolanm@redhat.com> - 0.20080318-1
- initial version
