%define evomajor %(pkg-config evolution-shell --variable=execversion)
%define evominor %(echo %evomajor|awk -F. '{print $2}')
%define evounstable %(echo 2.$((%evominor-1)))
%define evonextmajor %(echo 2.$((%evominor+1)))
%define evoplugindir %(pkg-config evolution-plugin --variable=plugindir)

%define gitdate git20100429

Summary:	RSS Reader for Evolution Mail
Name:		evolution-rss
Version:	0.1.9
Release:	%mkrel -c %gitdate 1
Group:		Networking/News
License:	GPLv2+
URL:		http://gnome.eu.org/index.php/Evolution_RSS_Reader_Plugin
Source0:	http://gnome.eu.org/%name-%version-%gitdate.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires:	evolution-devel >= 2.4.1
BuildRequires:	gtkhtml-3.14-devel >= 3.18.3
BuildRequires:	libglade2.0-devel
BuildRequires:	libcanberra-devel
#gw libtool dep:
BuildRequires:	gnome-pilot-devel
Requires:	evolution >= %evounstable
Requires:	evolution < %evonextmajor
BuildRequires:	webkitgtk-devel
BuildRequires:	intltool gnome-common

%description
This plugin enables support for RSS feeds in evolution mail.

%prep
%setup -qn %name

%build
NOCONFIGURE=yes gnome-autogen.sh
%configure2_5x --disable-schemas-install --disable-gecko --with-primary-render=webkit
%make

%if %mdkversion < 200900
%post
%post_install_gconf_schemas %name
%endif

%preun
%preun_uninstall_gconf_schemas %name

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS FAQ NEWS README TODO
%{_sysconfdir}/gconf/schemas/*.schemas
%{_bindir}/*
%{evoplugindir}/*
%{_datadir}/evolution/%{evomajor}/*/*
