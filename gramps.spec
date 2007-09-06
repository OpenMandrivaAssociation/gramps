Summary:	Genealogical Research and Analysis Management Programming System
Name:		gramps
Version:	2.2.8
Release:	%mkrel 2
License:	GPLv2+
Group:		Sciences/Other
Source0:	http://prdownloads.sourceforge.net/gramps/%{name}-%{version}.tar.bz2
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
Requires:	pygtk2.0-libglade
Requires:	shared-mime-info 

%description
gramps (Genealogical Research and Analysis Management Programming
System) is a GNOME based genealogy program supporting a Python
based plugin system.

%prep
%setup -q
./autogen.sh

%build
%configure2_5x \
  --enable-packager-mode
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall
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

%post
%update_scrollkeeper
%update_mime_database
%update_menus
%post_install_gconf_schemas %{name}
%update_icon_cache hicolor

%preun
%preun_uninstall_gconf_schemas %{name}

%postun
%clean_scrollkeeper
%{clean_menus}
%clean_icon_cache hicolor

%files -f %{name}.lang
%defattr(-, root, root)

%doc README TODO
%_sysconfdir/gconf/schemas/%{name}.schemas
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
%{_datadir}/omf/%{name}
%{_mandir}/man1/*
%{_iconsdir}/hicolor/*/apps/%{name}.png

