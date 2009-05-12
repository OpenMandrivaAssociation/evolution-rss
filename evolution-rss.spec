%define evomajor %(pkg-config evolution-shell --variable=execversion)
%define evominor %(echo %evomajor|awk -F. '{print $2}')
%define evounstable %(echo 2.$((%evominor-1)))
%define evonextmajor %(echo 2.$((%evominor+1)))
%define evoplugindir %(pkg-config evolution-plugin --variable=plugindir)

%define Werror_cflags %nil

Summary:	RSS Reader for Evolution Mail
Name:		evolution-rss
Version:	0.1.2
Release:	%mkrel 5
Group:		Networking/News
License:	GPLv2+
URL:		http://gnome.eu.org/index.php/Evolution_RSS_Reader_Plugin
Source0:	http://gnome.eu.org/%name-%version.tar.gz
Patch0:		evolution-rss-0.1.2-fix-gtkhtml-flags.patch
Patch1:		evolution-rss-0.1.2-linkage.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires:	evolution-devel >= 2.4.1
BuildRequires:	gtkhtml-3.14-devel
Requires:	evolution >= %evounstable
Requires:	evolution < %evonextmajor
BuildRequires:	webkitgtk-devel
BuildRequires:	intltool

%description
This plugin enables support for RSS feeds in evolution mail.

%prep
%setup -q
%patch0 -p0 -b .pkgconfig
%patch1 -p0

%build
autoreconf -fi
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
%{_libdir}/bonobo/servers/*.server
%{evoplugindir}/*
%{_datadir}/evolution/%{evomajor}/*/*
