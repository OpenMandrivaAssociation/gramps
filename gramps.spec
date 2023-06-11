Summary:	Genealogical Research and Analysis Management Programming System
Name:		gramps
Version:	5.1.5
Release:	1
License:	GPLv2+
Group:		Sciences/Other
Source0:	https://github.com/gramps-project/gramps/archive/refs/tags/v%{version}.tar.gz
Source11:	%{name}-48.png
Source12:	%{name}-32.png
Source13:	%{name}-16.png
URL:		http://www.gramps-project.org
BuildArch:	noarch
BuildRequires:	desktop-file-utils
BuildRequires:	intltool
Requires:       typelib(Gtk) = 3.0
Requires:	shared-mime-info
Requires:	xdg-utils
Requires:	python-gi
Requires:	python-gi-cairo
Requires:	python-bsddb3
Requires:	python-icu
Requires:	typelib(GExiv2)
Requires:	typelib(Pango)
Requires:	typelib(PangoCairo)
Requires:	typelib(GdkPixbuf)
Requires:	typelib(Gdk)
Requires:	typelib(GLib)

Suggests:	gtkspell3
Suggests:	typelib(GooCanvas) = 2.0
Suggests:	fonts-ttf-freefont
#Suggest it for geography functionality
Suggests:	typelib(OsmGpsMap)
Suggests:	graphviz

%description
gramps (Genealogical Research and Analysis Management Programming
System) is a GNOME based genealogy program supporting a Python
based plugin system.

%prep
%autosetup -p1

%build
python setup.py build

%install
python setup.py install --root %{buildroot}
# fix it:
perl -pi -e "s@%{buildroot}@@" %buildroot/%python_sitelib/gramps/gen/utils/resource-path
rm -fr %{buildroot}/var

%find_lang %{name} --with-gnome --with-man

%files -f %{name}.lang
%{_bindir}/%{name}
%{_datadir}/metainfo/gramps.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}
%{_datadir}/mime/packages/%{name}.xml
%{_datadir}/mime-info/%{name}.*
%{_mandir}/man1/%{name}.1*
%{_iconsdir}/hicolor/*/mimetypes/*
%{_iconsdir}/hicolor/*/apps/%{name}.*
%python_sitelib/%name
%python_sitelib/*.egg-info
%doc %{_docdir}/gramps
