%define evomajor 2.22
%define evomajor_next 2.23
%define evomajor_unstable 2.21

Summary:	RSS Reader for Evolution Mail
Name:		evolution-rss
Version:	0.1.0
Release:	%mkrel 1
Group:		Networking/News
License:	GPLv2+
URL:		http://gnome.eu.org/index.php/Evolution_RSS_Reader_Plugin
Source0:	http://gnome.eu.org/%name-%version.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires:	evolution-devel >= %{evomajor_unstable}
Requires:	evolution >= %evomajor_unstable
Requires:	evolution < %evomajor_next

%description
This plugin enables support for RSS feeds in evolution mail.

%prep
%setup -q

%build
%configure2_5x
%make

%post
%post_install_gconf_schemas %name

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
%{_libdir}/bonobo/servers/*.server
%{_libdir}/evolution/%{evomajor}/*/*
%{_datadir}/evolution/%{evomajor}/*/*
