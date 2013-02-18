Summary:	Genealogical Research and Analysis Management Programming System
Name:		gramps
Version:	3.4.2
Release:	2
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


%changelog
* Mon Oct 31 2011 Andrey Bondrov <abondrov@mandriva.org> 3.3.1-1
+ Revision: 708046
- New version 3.3.1, update BuildRequires, Requires, Suggests

* Sun May 08 2011 Sandro Cazzaniga <kharec@mandriva.org> 3.2.6-1
+ Revision: 672506
- new version 3.2.6 (which is a bugfix release, fixes major and minors bugs)

* Sat Nov 27 2010 Sandro Cazzaniga <kharec@mandriva.org> 3.2.5-1mdv2011.0
+ Revision: 601783
- update to new version 3.2.5

* Fri Oct 15 2010 Sandro Cazzaniga <kharec@mandriva.org> 3.2.4-1mdv2011.0
+ Revision: 585740
- update to 3.2.4

* Sun Jul 11 2010 Sandro Cazzaniga <kharec@mandriva.org> 3.2.3-1mdv2011.0
+ Revision: 551173
- update to 3.2.3

* Sun May 30 2010 Thierry Vignaud <tv@mandriva.org> 3.2.2-3mdv2010.1
+ Revision: 546596
- bump release

* Sun Apr 25 2010 Sandro Cazzaniga <kharec@mandriva.org> 3.2.2-1mdv2010.1
+ Revision: 538533
- update to 3.2.2

* Thu Apr 01 2010 Sandro Cazzaniga <kharec@mandriva.org> 3.2.0-1mdv2010.1
+ Revision: 530573
- update to 3.2.0

* Sat Dec 26 2009 Funda Wang <fwang@mandriva.org> 3.1.3-1mdv2010.1
+ Revision: 482398
- new version 3.1.3

* Sat Nov 07 2009 Frederik Himpe <fhimpe@mandriva.org> 3.1.2-1mdv2010.1
+ Revision: 462335
- update to new version 3.1.2

* Fri Sep 11 2009 Thierry Vignaud <tv@mandriva.org> 3.1.1-2mdv2010.0
+ Revision: 437810
- rebuild

* Wed Mar 11 2009 Frederik Himpe <fhimpe@mandriva.org> 3.1.1-1mdv2009.1
+ Revision: 353923
- update to new version 3.1.1

* Sun Mar 08 2009 Frederik Himpe <fhimpe@mandriva.org> 3.1.0-1mdv2009.1
+ Revision: 353012
- Update to new version 3.1.0
- Don't run autogen.sh: it's not needed and does not even work with 3.1.0

* Sun Jan 04 2009 Jérôme Soyer <saispo@mandriva.org> 3.0.4-1mdv2009.1
+ Revision: 324428
- New upstream release

* Fri Nov 28 2008 Götz Waschk <waschk@mandriva.org> 3.0.3-1mdv2009.1
+ Revision: 307466
- new version
- add missing dep on gnome-python-gtkspell

* Thu Aug 07 2008 Thierry Vignaud <tv@mandriva.org> 3.0.1-2mdv2009.0
+ Revision: 266948
- rebuild early 2009.0 package (before pixel changes)

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Sun Jun 01 2008 Funda Wang <fwang@mandriva.org> 3.0.1-1mdv2009.0
+ Revision: 213893
- add missing files
- New version 3.0.1

* Tue Apr 15 2008 Thierry Vignaud <tv@mandriva.org> 3.0.0-1mdv2009.0
+ Revision: 193495
- further adjust file list
- adjust file list
- disable --enable-packager-mode (which just remove schemas)
- new release
- new release
- kill dead sources
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Tue Oct 23 2007 Jérôme Soyer <saispo@mandriva.org> 2.2.9-1mdv2008.1
+ Revision: 101473
- New release 2.2.9

* Thu Sep 06 2007 Adam Williamson <awilliamson@mandriva.org> 2.2.8-2mdv2008.0
+ Revision: 80865
- fd.o icons
- fix errors in the .desktop file
- use configure macro
- drop the bogus sed command which was changing the app version...
- use Fedora license policy

* Sun Jun 24 2007 Funda Wang <fwang@mandriva.org> 2.2.8-1mdv2008.0
+ Revision: 43564
- New version


* Sun Feb 18 2007 Jérôme Soyer <saispo@mandriva.org> 2.2.6-1mdv2007.0
+ Revision: 122509
- New release 2.2.6

* Mon Jan 29 2007 Götz Waschk <waschk@mandriva.org> 2.2.5-1mdv2007.1
+ Revision: 115010
- fix build with new gnome-doc-utils
- new version

* Fri Jan 05 2007 Nicolas Lécureuil <neoclust@mandriva.org> 2.2.4-1mdv2007.1
+ Revision: 104391
- New Version 2.2.4

* Mon Nov 27 2006 Götz Waschk <waschk@mandriva.org> 2.2.3-1mdv2007.1
+ Revision: 87350
- new version
- update file list

* Fri Nov 03 2006 Götz Waschk <waschk@mandriva.org> 2.2.2-1mdv2007.1
+ Revision: 76106
- new version

* Tue Oct 31 2006 Götz Waschk <waschk@mandriva.org> 2.2.1-2mdv2007.1
+ Revision: 74767
- fix buildrequires
- Import gramps

* Mon Oct 30 2006 Götz Waschk <waschk@mandriva.org> 2.2.1-1mdv2007.1
- New version 2.2.1

* Sat Sep 16 2006 Emmanuel Andry <eandry@mandriva.org> 2.0.11-3mdv2007.0
- Oops ! Moved desktop-file-utils from requires to buildrequires

* Sat Sep 16 2006 Emmanuel Andry <eandry@mandriva.org> 2.0.11-2mdv2007.0
- xdg menu
- gconf, mime and scrollkeeper macros
- fix Xvfb path

* Wed May 03 2006 Götz Waschk <waschk@mandriva.org> 2.0.11-1mdk
- New release 2.0.11

* Tue Mar 07 2006 Götz Waschk <waschk@mandriva.org> 2.0.10-1mdk
- New release 2.0.10

* Wed Dec 14 2005 Götz Waschk <waschk@mandriva.org> 2.0.9-1mdk
- New release 2.0.9
- use mkrel

* Fri Sep 09 2005 Götz Waschk <waschk@mandriva.org> 2.0.8-1mdk
- New release 2.0.8

* Wed Aug 17 2005 Götz Waschk <waschk@mandriva.org> 2.0.6-1mdk
- New release 2.0.6

* Fri Jul 08 2005 G�tz Waschk <waschk@mandriva.org> 2.0.5-1mdk
- New release 2.0.5

* Fri Jul 01 2005 G�tz Waschk <waschk@mandriva.org> 2.0.4-1mdk
- New release 2.0.4

* Mon Jun 06 2005 G�tz Waschk <waschk@mandriva.org> 2.0.3-1mdk
- New release 2.0.3

* Thu May 26 2005 G�tz Waschk <waschk@mandriva.org> 2.0.1-1mdk
- replace patch by packager mode
- New release 2.0.1

* Fri May 13 2005 G�tz Waschk <waschk@mandriva.org> 2.0.0-1mdk
- make the package noarch
- handle gconf stuff
- handle mime stuff
- add new files
- fix source URL
- new version

* Wed Mar 23 2005 Lenny Cartier <lenny@mandrakesoft.com> 1.0.11-1mdk
- from Emmanuel Andry <eandry@free.fr> : 
	- New release 1.0.11

* Wed Mar 09 2005 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 1.0.10-1mdk
- cosmetics
- fix summary-ended-with-dot
- from Emmanuel Andry <eandry@free.fr> :
	o New release 1.0.10

* Mon Nov 01 2004 G�tz Waschk <waschk@linux-mandrake.com> 1.0.8-1mdk
- fix file list
- New release 1.0.8

* Wed Aug 18 2004 Pascal Terjan <pterjan@mandrake.org> 1.0.7-1mdk
- New release 1.0.7

* Tue Aug 03 2004 Goetz Waschk <waschk@linux-mandrake.com> 1.0.5-1mdk
- New release 1.0.5

* Fri Jun 18 2004 Goetz Waschk <waschk@linux-mandrake.com> 1.0.4-1mdk
- New release 1.0.4

* Sat Apr 24 2004 Goetz Waschk <waschk@linux-mandrake.com> 1.0.3-1mdk
- New release 1.0.3

* Tue Apr 06 2004 Götz Waschk <waschk@linux-mandrake.com> 1.0.2-1mdk
- new version

