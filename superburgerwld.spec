%define name	superburgerwld
%define version 0.1.2
%define rel	1
%define release	%mkrel %rel
%define Summary Jump 'n run sidescroller with a burger

Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	http://downloads.sourceforge.net/superburgerwld/%{name}-%{version}_src.tar.bz2
Patch0:		supertux-0.1.3-fix-build.patch
License:	GPL
Group:		Games/Arcade
URL:		http://superburgerwld.sourceforge.net/
Summary:	%{Summary}
BuildRequires:	jam
BuildRequires:	SDL_mixer-devel SDL_image-devel MesaGLU-devel
BuildRequires:	oggvorbis-devel openal-devel physfs-devel zlib-devel 
BuildRequires:	desktop-file-utils
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Super Burger World is a jump and run game based on SuperTux, except
with one big difference, You play as a burger trying to rid the world
of an evil fruit company.

%prep
%setup -q -n %{name}-0.12_src
%patch0 -p1
perl -pi -e "s|-DDATA_PREFIX='.*'|-DDATA_PREFIX='\\\\\"\\\$datadir/super-burger-world\\\\\"'|" configure configure.ac

%build
%configure2_5x --bindir=%{_gamesbindir} --datadir=%{_gamesdatadir}
%make 

%install
rm -rf %{buildroot}
%{makeinstall_std} desktopdir=%{_datadir}/applications icondir=%{_datadir}/pixmaps

desktop-file-install --vendor="" \
  --remove-category="Application" \
  --add-category="Game" \
  --add-category="ArcadeGame" \
  --add-category="X-MandrivaLinux-MoreApplications-Games-Arcade" \
  --dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/*

%post
%{update_menus}

%postun
%{clean_menus}

%clean
rm -rf %{buildroot}

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog INSTALL LEVELDESIGN
%doc NEWS README TODO
%{_gamesdatadir}/super-burger-world
%{_datadir}/applications/superburgerworld.desktop
%{_datadir}/pixmaps/superbw.png
%defattr(755,root,root,755)
%{_gamesbindir}/%{name}


