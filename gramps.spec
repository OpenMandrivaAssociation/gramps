Summary:	Genealogical Research and Analysis Management Programming System
Name:		gramps
Version:	3.2.6
Release:	%mkrel 1
License:	GPLv2+
Group:		Sciences/Other
Source0:	http://prdownloads.sourceforge.net/gramps/%{name}-%{version}.tar.gz
Source11:	%{name}-48.png
Source12:	%{name}-32.png
Source13:	%{name}-16.png
URL:		http://www.gramps-project.org
BuildArch: noarch
BuildRequires:	scrollkeeper >= 0.1.4 docbook-utils
BuildRequires:  gnome-python-gconf
BuildRequires:  gnome-python-canvas
BuildRequires:  gnome-python-gnomevfs
BuildRequires:  pygtk2.0-libglade
BuildRequires:  libpython-devel
BuildRequires:  libgnome-vfs2-devel
BuildRequires:  desktop-file-utils
BuildRequires:  gnome-doc-utils libxslt-proc
BuildRequires:  intltool gnome-common
Requires:       gnome-python-gconf
Requires:	gnome-python-canvas
Requires:	gnome-python-gnomevfs
Requires:	gnome-python-gtkspell
Requires:	pygtk2.0-libglade
Requires:	python-enchant
Requires:	shared-mime-info

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
rm -fr %buildroot/var

#menu
perl -pi -e 's,%{name}.png,%{name},g' %buildroot%{_datadir}/applications/*
desktop-file-install --vendor="" \
  --remove-category="Application" \
  --remove-category="Genealogy" \
  --add-category="Science" \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications $RPM_BUILD_ROOT%{_datadir}/applications/*

#icons
install -m644 %{SOURCE11} -D %buildroot%{_iconsdir}/hicolor/48x48/apps/%{name}.png
install -m644 %{SOURCE12} -D %buildroot%{_iconsdir}/hicolor/32x32/apps/%{name}.png
install -m644 %{SOURCE13} -D %buildroot%{_iconsdir}/hicolor/16x16/apps/%{name}.png

%find_lang %{name} --with-gnome

%clean
rm -rf %buildroot

%files -f %{name}.lang
%defattr(-, root, root)

%doc README TODO
%{_bindir}/%{name}
%{_datadir}/applications/*.desktop
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*
%_datadir/mime/packages/%{name}.xml
%_datadir/icons/gnome/48x48/mimetypes/*
%_datadir/pixmaps/gramps.png
%_datadir/icons/gnome/scalable/mimetypes/*
%_datadir/application-registry/%{name}.applications
%_datadir/mime-info/*
%{_mandir}/man1/*
%lang(fr) %_mandir/fr/man1/gramps.1.*
%lang(nl) %_mandir/nl/man1/gramps.1.*
%lang(pl) %_mandir/pl/man1/gramps.1.*
%lang(sv) %_mandir/sv/man1/gramps.1.*
%{_iconsdir}/hicolor/*/apps/%{name}.png
