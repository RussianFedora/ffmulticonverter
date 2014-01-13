%define py_sitedir /usr/lib/python?.?/site-packages

Name:       ffmulticonverter
Version:    1.6.0
Release:    1%{?dist}
Summary:    GUI File Format Converter

License:    GPLv3
URL:        https://sites.google.com/site/ffmulticonverter/home
Source0:    http://sourceforge.net/projects/ffmulticonv/files/%{name}-%{version}.tar.gz

BuildArch:  noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

Requires:   python3-PyQt4
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
%setup -q -n %{name}-%version


%build
%{__python3} setup.py build

%install
%{__python3} ./setup.py install -O1 --root=%{buildroot}
chmod 755 %{buildroot}%{py_sitedir}/%{name}/%{name}.py
chmod 755 %{buildroot}%{py_sitedir}/%{name}/about_dlg.py
chmod 755 %{buildroot}%{py_sitedir}/%{name}/presets_dlgs.py
chmod 755 %{buildroot}%{py_sitedir}/%{name}/progress.py
chmod 755 %{buildroot}%{py_sitedir}/%{name}/preferences_dlg.py


%files
%doc ChangeLog COPYING README.txt AUTHORS TRANSLATORS
%{_bindir}/%{name}
%{py_sitedir}/%{name}-%version-py3.3.egg-info
%{py_sitedir}/%{name}
%{_datadir}/applications/*.desktop
%{_datadir}/%{name}/presets.xml
%{_datadir}/pixmaps/%{name}.png
%{_mandir}/man1/ffmulticonverter.1.gz

%changelog
* Mon Jan 13 2014 Vasiliy N. Glazov <vascom2@gmail.com> 1.6.0-1
- Update to 1.6.0

* Tue Jun 18 2013 Vasiliy N. Glazov <vascom2@gmail.com> 1.5.2-1
- Update to 1.5.2

* Fri May 24 2013 Vasiliy N. Glazov <vascom2@gmail.com> 1.5.1-1
- Initial release
