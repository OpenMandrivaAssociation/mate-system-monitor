%define url_ver %(echo %{version}|cut -d. -f1,2)

Summary:	Simple process monitor for MATE
Name:		mate-system-monitor
Version:	1.26.1
Release:	1
License:	GPLv2+
Group:		Graphical desktop/Other
Url:		http://mate-desktop.org
Source0:	http://pub.mate-desktop.org/releases/%{url_ver}/%{name}-%{version}.tar.xz

BuildRequires:	autoconf-archive
BuildRequires:	desktop-file-utils
BuildRequires:	intltool
BuildRequires:	itstool
BuildRequires:	mate-common
BuildRequires:	pkgconfig(dbus-glib-1)
BuildRequires:	pkgconfig(gio-2.0)
BuildRequires:	pkgconfig(giomm-2.4)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(glibmm-2.4)
BuildRequires:	pkgconfig(gtkmm-3.0)
BuildRequires:	pkgconfig(libgtop-2.0)
BuildRequires:	pkgconfig(librsvg-2.0)
BuildRequires:	pkgconfig(libsystemd)
BuildRequires:	pkgconfig(libwnck-3.0)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	yelp-tools
BuildRequires:  pkgconfig(polkit-agent-1)

Requires:	polkit-agent
Requires:	mate-desktop

%description
The MATE Desktop Environment is the continuation of GNOME 2. It provides an
intuitive and attractive desktop environment using traditional metaphors for
Linux and other Unix-like operating systems.

MATE is under active development to add support for new technologies while
preserving a traditional desktop experience.

This package provides a simple process and system monitor that integrates
well with the MATE desktop environment.

%files -f %{name}.lang
%doc README NEWS AUTHORS ChangeLog TODO
%{_bindir}/mate-system-monitor
%{_datadir}/applications/%{name}.desktop
%{_datadir}/glib-2.0/schemas/org.mate.system-monitor.*.xml
%{_datadir}/pixmaps/%{name}
%{_datadir}/metainfo/%{name}.appdata.xml
%{_libexecdir}/%{name}/msm-kill
%{_libexecdir}/%{name}/msm-renice
%{_datadir}/polkit-1/actions/org.mate.mate-system-monitor.policy
%doc %{_mandir}/man1/mate-system-monitor.1*

#---------------------------------------------------------------------------

%prep
%setup -q
%autopatch -p1

%build
#NOCONFIGURE=yes ./autogen.sh
%configure \
	--disable-schemas-compile \
	--enable-systemd \
	--enable-wnck

%make_build

%install
%make_install

# locales
%find_lang %{name} --with-gnome --all-name

%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop
