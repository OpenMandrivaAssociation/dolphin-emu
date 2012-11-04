Name:		dolphin-emu
Version:	3.0.802
Release:	%mkrel 1
Epoch:		1
License:	GPLv2
Summary:	Gamecube / Wii / Triforce Emulator
Url:		http://www.dolphin-emu.com/
Group:		Emulators
# Fetched from git and cleaned up from useless junk
Source0:	%{name}-%{version}.tar.bz2
Source9:	%{name}-256.png
Source10:	%{name}-128.png
Source11:	%{name}-64.png
Source12:	%{name}-32.png
Source13:	%{name}-16.png
Patch0:		%{name}-cmakepath.patch
BuildRequires:	cg-devel
BuildRequires:	cmake
BuildRequires:	git
BuildRequires:	glew-devel
BuildRequires:	liblzo-devel
BuildRequires:	sfml-network-devel
BuildRequires:	zlib-devel
BuildRequires:	libao-devel
BuildRequires:	openal-devel
BuildRequires:	portaudio-devel
BuildRequires:	bluez-devel
BuildRequires:	SDL-devel
BuildRequires:	libxrandr-devel
BuildRequires:	wxgtku2.8-devel
BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(xrender) >= 0.9.6

%description
Gamecube / Wii / Triforce Emulator.

%prep
%setup -q
%patch0 -p1

%build
%__mkdir_p build
cd build
export CFLAGS='%{optflags}'
export CXXFLAGS='%{optflags}'
cmake -DCMAKE_INSTALL_PREFIX=%{buildroot}/usr -DLIB_SUFFIX=$(echo %{_lib} | cut -b4-) ..
%make

%install
%__rm -rf %{buildroot}
cd build
%makeinstall
cd ..
%__install -D -m 644 %{SOURCE13} %{buildroot}%{_iconsdir}/hicolor/16x16/apps/%{name}.png
%__install -D -m 644 %{SOURCE12} %{buildroot}%{_iconsdir}/hicolor/32x32/apps/%{name}.png
%__install -D -m 644 %{SOURCE11} %{buildroot}%{_iconsdir}/hicolor/64x64/apps/%{name}.png
%__install -D -m 644 %{SOURCE10} %{buildroot}%{_iconsdir}/hicolor/128x128/apps/%{name}.png
%__install -D -m 644 %{SOURCE9} %{buildroot}%{_iconsdir}/hicolor/256x256/apps/%{name}.png

%__install -d %{buildroot}%{_datadir}/applications
%__cat > %{buildroot}%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Name=Dolphin-Emulator
Comment=%{summary}
Exec=%{_bindir}/%{name}
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=true
Categories=Game;Emulator;
EOF

%find_lang %{name}

%clean
%__rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(0644,root,root,0755)
%doc license.txt Readme.txt
%attr(0755, root, root) %{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_iconsdir}/hicolor/*/apps/%{name}.png

