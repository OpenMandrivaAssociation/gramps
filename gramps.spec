Summary:	Genealogical Research and Analysis Management Programming System
Name:		gramps
Version:	3.4.2
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
BuildRequires:	python-gobject
Requires:	pygtk2.0
Requires:	gnome-python-gconf
Requires:	gnome-python-canvas
Requires:	gnome-python-gnomevfs
Requires:	python-exiv2
Requires:	python-graphviz
Requires:	shared-mime-info
Requires:	xdg-utils
Suggests:	gnome-python-gtkspell
Suggests:	python-webkitgtk
Suggests:	fonts-ttf-freefont
#Suggest it for geography functionality
Suggests:	python-osmgpsmap

%description
gramps (Genealogical Research and Analysis Management Programming
System) is a GNOME based genealogy program supporting a Python
based plugin system.

%prep
%setup -q

%build
%configure2_5x --disable-mime-install --enable-packager-mode
%make

%install
%makeinstall_std
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

%clean
rm -rf %buildroot

%files -f %{name}.lang
%defattr(-, root, root)

%doc README TODO
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*
%{_datadir}/mime/packages/%{name}.xml
%{_datadir}/icons/gnome/*/mimetypes/*
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/application-registry/%{name}.applications
%{_datadir}/mime-info/%{name}.*
%{_mandir}/man1/%{name}.1*
%{_iconsdir}/hicolor/*/apps/%{name}.png
