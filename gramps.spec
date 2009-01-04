Summary:	Genealogical Research and Analysis Management Programming System
Name:		gramps
Version:	3.0.4
Release:	%mkrel 1
License:	GPLv2+
Group:		Sciences/Other
Source0:	http://prdownloads.sourceforge.net/gramps/%{name}-%{version}.tar.gz
Source11:	%{name}-48.png
Source12:	%{name}-32.png
Source13:	%{name}-16.png
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
URL:		http://gramps.sourceforge.net
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
Requires:	shared-mime-info

%description
gramps (Genealogical Research and Analysis Management Programming
System) is a GNOME based genealogy program supporting a Python
based plugin system.

%prep
%setup -q

%build
./autogen.sh
%configure2_5x --disable-mime-install --enable-packager-mode
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std
rm -fr $RPM_BUILD_ROOT/var

#menu
perl -pi -e 's,%{name}.png,%{name},g' $RPM_BUILD_ROOT%{_datadir}/applications/*
desktop-file-install --vendor="" \
  --remove-category="Application" \
  --remove-category="Genealogy" \
  --add-category="Science" \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications $RPM_BUILD_ROOT%{_datadir}/applications/*

#icons
install -m644 %{SOURCE11} -D $RPM_BUILD_ROOT%{_iconsdir}/hicolor/48x48/apps/%{name}.png
install -m644 %{SOURCE12} -D $RPM_BUILD_ROOT%{_iconsdir}/hicolor/32x32/apps/%{name}.png
install -m644 %{SOURCE13} -D $RPM_BUILD_ROOT%{_iconsdir}/hicolor/16x16/apps/%{name}.png

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post
%update_scrollkeeper
%update_mime_database
%update_menus
%update_icon_cache hicolor
%endif

%if %mdkversion < 200900
%postun
%clean_scrollkeeper
%{clean_menus}
%clean_icon_cache hicolor
%endif

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
