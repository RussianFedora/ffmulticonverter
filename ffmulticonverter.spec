Name:       ffmulticonverter
Version:    1.8.0
Release:    3%{?dist}
Summary:    GUI File Format Converter

License:    GPLv3+
URL:        https://sites.google.com/site/ffmulticonverter/home
Source0:    http://sourceforge.net/projects/ffmulticonv/files/%{name}-%{version}.tar.gz

BuildArch:  noarch

BuildRequires:  pkgconfig(python3)
BuildRequires:  python3-setuptools
BuildRequires:  desktop-file-utils

Requires:   python3-qt5
Requires:   ImageMagick
Requires:   unoconv
Requires:   ffmpeg


%description
Graphical application which enables you to convert audio, video, image and
document files between all popular formats using ffmpeg, unoconv, and
ImageMagick.

Features:
 - Conversions for several file formats.
 - Very easy to use interface.
 - Access to common conversion options.
 - Audio/video ffmpeg-presets management.
 - Options for saving and naming files.
 - Recursive conversions

%prep
%autosetup


%build
%py3_build

%install
%py3_install


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop


%files
%doc ChangeLog README.txt AUTHORS TRANSLATORS
%license COPYING
%{_bindir}/%{name}
%{python3_sitelib}/%{name}-%version-py%{python3_version}.egg-info
%{python3_sitelib}/%{name}
%{_datadir}/applications/*.desktop
%{_datadir}/%{name}
%{_datadir}/pixmaps/%{name}.png
%{_mandir}/man1/%{name}.1.*

%changelog
* Sat Aug 13 2016 Vasiliy N. Glazov <vascom2@gmail.com> 1.8.0-3
- Correct license, requires and directory own

* Fri Aug 12 2016 Vasiliy N. Glazov <vascom2@gmail.com> 1.8.0-2
- Clean spec

* Tue Jul 19 2016 Vasiliy N. Glazov <vascom2@gmail.com> 1.8.0-1
- Update to 1.8.0

* Thu Jun 16 2016 Vasiliy N. Glazov <vascom2@gmail.com> 1.7.2-2
- Correct files handling
- Use pkgconfig in BR

* Fri Dec 18 2015 Vasiliy N. Glazov <vascom2@gmail.com> 1.7.2-1
- Update to 1.7.2

* Tue Jun 30 2015 Vasiliy N. Glazov <vascom2@gmail.com> 1.7.1-1
- Update to 1.7.1
- Use macros for python lib path

* Wed Mar 25 2015 Vasiliy N. Glazov <vascom2@gmail.com> 1.7.0-1
- Update to 1.7.0

* Wed Oct 08 2014 Vasiliy N. Glazov <vascom2@gmail.com> 1.6.0-2
- Bump rebuild for Fedora 21

* Mon Jan 13 2014 Vasiliy N. Glazov <vascom2@gmail.com> 1.6.0-1
- Update to 1.6.0

* Tue Jun 18 2013 Vasiliy N. Glazov <vascom2@gmail.com> 1.5.2-1
- Update to 1.5.2

* Fri May 24 2013 Vasiliy N. Glazov <vascom2@gmail.com> 1.5.1-1
- Initial release
