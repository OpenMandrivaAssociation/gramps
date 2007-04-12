%define name	gramps
%define version 2.2.6
%define release %mkrel 1

Summary:	Genealogical Research and Analysis Management Programming System
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
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
sed -i 's/2\.2/2\.3/' configure

%build
./configure --prefix=%_prefix --mandir=%_mandir --sysconfdir=%_sysconfdir \
  --enable-packager-mode
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall
rm -fr $RPM_BUILD_ROOT/var

#menu
desktop-file-install --vendor="" \
  --remove-category="Application" \
  --remove-category="Genealogy" \
  --add-category="Science" \
  --add-category="X-MandrivaLinux-MoreApplications-Sciences-Other" \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications $RPM_BUILD_ROOT%{_datadir}/applications/*

#icons
install -m644 %{SOURCE11} -D $RPM_BUILD_ROOT%{_liconsdir}/%{name}.png
install -m644 %{SOURCE12} -D $RPM_BUILD_ROOT%{_iconsdir}/%{name}.png
install -m644 %{SOURCE13} -D $RPM_BUILD_ROOT%{_miconsdir}/%{name}.png

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_scrollkeeper
%update_mime_database
%update_menus
%post_install_gconf_schemas %{name}

%preun
%preun_uninstall_gconf_schemas %{name}

%postun
%clean_scrollkeeper
%{clean_menus}

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
%{_liconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_miconsdir}/%{name}.png


