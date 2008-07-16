%define evomajor %(pkg-config evolution-shell --variable=execversion)
%define evominor %(echo %evomajor|awk -F. '{print $2}')
%define evounstable %(echo 2.$((%evominor-1)))
%define evonextmajor %(echo 2.$((%evominor+1)))
%define firefox_version %(rpm -q mozilla-firefox --queryformat %{VERSION})
%define evoplugindir %(pkg-config evolution-plugin --variable=plugindir)

Summary:	RSS Reader for Evolution Mail
Name:		evolution-rss
Version:	0.1.0
Release:	%mkrel 3
Group:		Networking/News
License:	GPLv2+
URL:		http://gnome.eu.org/index.php/Evolution_RSS_Reader_Plugin
Source0:	http://gnome.eu.org/%name-%version.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires:	evolution-devel >= %evounstable
Requires:	evolution >= %evounstable
Requires:	evolution < %evonextmajor
BuildRequires:	mozilla-firefox-devel
Requires:	%mklibname mozilla-firefox %firefox_version

%description
This plugin enables support for RSS feeds in evolution mail.

%prep
%setup -q

%build
%configure2_5x --disable-schemas-install
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
%{evoplugindir}/*
%{_datadir}/evolution/%{evomajor}/*/*
