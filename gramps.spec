Summary:	Genealogical Research and Analysis Management Programming System
Name:		gramps
Version:	4.2.3
Release:	1
License:	GPLv2+
Group:		Sciences/Other
Source0:	http://prdownloads.sourceforge.net/gramps/%{name}-%{version}.tar.gz
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
Requires:	python3-gi
Requires:	python3-bsddb3
Requires:	python3-icu
Requires:	typelib(GExiv2)
Requires:	typelib(Pango)
Requires:	typelib(PangoCairo)
Requires:	typelib(GdkPixbuf)
Requires:	typelib(Gdk)
Requires:	typelib(GLib)

Suggests:	gtkspell3
Suggests:	typelib(Goocanvas) = 2.0
Suggests:	typelib(WebKit) = 3.0
Suggests:	fonts-ttf-freefont
#Suggest it for geography functionality
Suggests:	typelib(OsmGpsMap)

%description
gramps (Genealogical Research and Analysis Management Programming
System) is a GNOME based genealogy program supporting a Python
based plugin system.

%prep
%setup -q

%build
python3 setup.py build

%install
python3 setup.py install --root %{buildroot}
# fix it:
perl -pi -e "s@%{buildroot}@@" %buildroot/%python3_sitelib/gramps/gen/utils/resource-path
rm -fr %{buildroot}/var

#menu
perl -pi -e 's,%{name}.png,%{name},g' %{buildroot}%{_datadir}/applications/*
desktop-file-install --vendor="" \
  --remove-category="Application" \
  --remove-category="Genealogy" \
  --add-category="Science" \
  --dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/*

#icons
install -m644 %{SOURCE11} -D %{buildroot}%{_iconsdir}/hicolor/48x48/apps/%{name}.png
install -m644 %{SOURCE12} -D %{buildroot}%{_iconsdir}/hicolor/32x32/apps/%{name}.png
install -m644 %{SOURCE13} -D %{buildroot}%{_iconsdir}/hicolor/16x16/apps/%{name}.png

%find_lang %{name} --with-gnome --with-man

%files -f %{name}.lang
%doc README TODO
%{_bindir}/%{name}
%{_datadir}/appdata/gramps.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}
%{_datadir}/mime/packages/%{name}.xml
%{_datadir}/icons/gnome/*/mimetypes/*
%{_iconsdir}/%{name}.png
%{_datadir}/mime-info/%{name}.*
%{_mandir}/man1/%{name}.1*
%{_iconsdir}/hicolor/*/apps/%{name}.png
%python3_sitelib/%name
%python3_sitelib/*.egg-info

