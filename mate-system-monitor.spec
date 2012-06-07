Summary:	Simple process monitor for MATE
Name:		mate-system-monitor
Version:	1.2.1
Release:	1
License:	GPLv2+
Group:		Graphical desktop/GNOME
URL:		http://mate-desktop.org
Source0:	http://pub.mate-desktop.org/releases/1.2/%{name}-%{version}.tar.xz

BuildRequires:	docbook-dtd412-xml
BuildRequires:	intltool
BuildRequires:	mate-common
BuildRequires:	mate-conf
BuildRequires:	xsltproc
BuildRequires:	pkgconfig(dbus-glib-1)
BuildRequires:	pkgconfig(giomm-2.4)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(glibmm-2.4)
BuildRequires:	pkgconfig(gtkmm-2.4)
BuildRequires:	pkgconfig(libgtop-2.0)
BuildRequires:	pkgconfig(librsvg-2.0)
BuildRequires:	pkgconfig(libwnck-1.0)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(mateconf-2.0)
BuildRequires:	pkgconfig(mate-doc-utils)
BuildRequires:	pkgconfig(mate-icon-theme)

Requires:	polkit-mate

%description
Mate-system-monitor is a simple process and system monitor.

%prep
%setup -q
%apply_patches

%build
NOCONFIGURE=yes ./autogen.sh
%configure2_5x \
	--disable-scrollkeeper

%make LIBS='-lgmodule-2.0'

%install
%makeinstall_std
%find_lang %{name} --with-gnome

%files -f %{name}.lang
%doc README NEWS AUTHORS
%{_sysconfdir}/mateconf/schemas/mate-system-monitor.schemas
%{_bindir}/mate-system-monitor
%{_datadir}/applications/*
%{_datadir}/pixmaps/%{name}
# mate help files 
%{_datadir}/mate/help

