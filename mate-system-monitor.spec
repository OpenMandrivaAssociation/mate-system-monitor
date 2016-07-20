%define url_ver %(echo %{version}|cut -d. -f1,2)

Summary:	Simple process monitor for MATE
Name:		mate-system-monitor
Version:	1.14.0
Release:	1
License:	GPLv2+
Group:		Graphical desktop/GNOME
Url:		http://mate-desktop.org
Source0:	http://pub.mate-desktop.org/releases/%{url_ver}/%{name}-%{version}.tar.xz
BuildRequires:	intltool
BuildRequires:	mate-common
BuildRequires:	yelp-tools
BuildRequires:	pkgconfig(dbus-glib-1)
BuildRequires:	pkgconfig(giomm-2.4)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(glibmm-2.4)
BuildRequires:	pkgconfig(gtkmm-3.0)
BuildRequires:	pkgconfig(libgtop-2.0)
BuildRequires:	pkgconfig(librsvg-2.0)
BuildRequires:	pkgconfig(libwnck-3.0)
BuildRequires:	pkgconfig(libxml-2.0)
Requires:	polkit-mate

%description
Mate-system-monitor is a simple process and system monitor.

%prep
%setup -q
%apply_patches

%build
%configure --with-gtk=3.0

%make

%install
%makeinstall_std

# remove unneeded converter
rm -fr  %{buildroot}%{_datadir}/MateConf

%find_lang %{name} --with-gnome --all-name

%files -f %{name}.lang
%doc README NEWS AUTHORS
%{_bindir}/mate-system-monitor
%{_datadir}/applications/*
%{_datadir}/glib-2.0/schemas/org.mate.system-monitor.*.xml
%{_datadir}/pixmaps/%{name}
%{_datadir}/appdata/%{name}.appdata.xml
%{_mandir}/man1/mate-system-monitor.1*

