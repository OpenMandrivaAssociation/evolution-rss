%define evomajor %(pkg-config evolution-shell --variable=execversion)
%define evominor %(echo %evomajor|awk -F. '{print $2}')
%define evounstable %(echo 2.$((%evominor-1)))
%define evonextmajor %(echo 2.$((%evominor+1)))
%define evoplugindir %(pkg-config evolution-plugin --variable=plugindir)

%define xulrunner 1.9
%define xullibname %mklibname xulrunner %xulrunner
%define xulver %(rpm -q --queryformat %%{VERSION} %xullibname)

Summary:	RSS Reader for Evolution Mail
Name:		evolution-rss
Version:	0.1.0
Release:	%mkrel 6
Group:		Networking/News
License:	GPLv2+
URL:		http://gnome.eu.org/index.php/Evolution_RSS_Reader_Plugin
Source0:	http://gnome.eu.org/%name-%version.tar.gz
Patch0: 60_startup-glue.patch
Patch1: 61_allow-libxul-embedding.patch
Patch2: 62_undef-gecko-home.patch
Patch3: 63_set-profile-path-after-init.patch
Patch4: 64_glue-shutdown.patch
Patch5: 65_firefox-import.patch
Patch6: 66_from_svn_add_evo_23_support.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires:	evolution-devel >= 2.4.1
Requires:	evolution >= %evounstable
Requires:	evolution < %evonextmajor
BuildRequires:	xulrunner-devel-unstable
Requires:	%xullibname = %xulver

%description
This plugin enables support for RSS feeds in evolution mail.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p0
%patch5 -p0
%patch6 -p1

%build
%configure2_5x --disable-schemas-install --with-primary-render=gecko
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
