Summary:	RSS Reader for Evolution Mail
Name:		evolution-rss
Version:	0.0.6
Release:	%mkrel 2
Group:		Networking/News
License:	GPLv2
URL:		http://mips.edu.ms/evo/index.php/Evolution_RSS_Reader_Plugin
Source0:	http://mips.edu.ms/%{name}-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires:	evolution-devel >= 2.4

%description
This plugin enables support for RSS feeds in evolution mail.

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS FAQ NEWS README TODO
%{_libdir}/bonobo/servers/*.server
%{_libdir}/evolution/*/plugins/*
%{_datadir}/evolution/*/errors/*
%{_datadir}/evolution/*/images/*
%{_datadir}/evolution/glade/*.glade
