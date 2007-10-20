%define evomajor 2.12

Summary:	RSS Reader for Evolution Mail
Name:		evolution-rss
Version:	0.0.6
Release:	%mkrel 3
Group:		Networking/News
License:	GPLv2
URL:		http://mips.edu.ms/evo/index.php/Evolution_RSS_Reader_Plugin
Source0:	http://mips.edu.ms/%{name}-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires:	evolution-devel >= %{evomajor}
Requires:	evolution >= %evomajor

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
%{_libdir}/evolution/%{evomajor}/plugins/*
%{_datadir}/evolution/%{evomajor}/errors/*
%{_datadir}/evolution/%{evomajor}/images/*
%{_datadir}/evolution/glade/*.glade
