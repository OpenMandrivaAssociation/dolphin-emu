Summary:	Gamecube / Wii / Triforce Emulator
Name:		dolphin-emu
Version:	4.0.2
Release:	3
Epoch:		1
License:	GPLv2+
Group:		Emulators
Url:		http://www.dolphin-emu.com/
# Fetched from git and cleaned up from useless junk
Source0:	%{name}-%{version}.tar.bz2
Source9:	%{name}-256.png
Source10:	%{name}-128.png
Source11:	%{name}-64.png
Source12:	%{name}-32.png
Source13:	%{name}-16.png
Patch0:		dolphin-emu-cmakepath.patch
Patch1:		dolphin-emu-findx11.patch
BuildRequires:	cmake
BuildRequires:	git
BuildRequires:	ffmpeg-devel
BuildRequires:	gomp-devel
BuildRequires:	lzo-devel
#Doesnt build with polarssl 1.3
#BuildRequires:	polarssl-devel
BuildRequires:	sfml-network-devel
BuildRequires:	wxgtku3.0-devel
BuildRequires:	miniupnpc-devel
BuildRequires:	pkgconfig(ao)
BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(bluez)
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(glu)
BuildRequires:	pkgconfig(glew)
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(libpulse)
BuildRequires:	pkgconfig(libusb-1.0)
BuildRequires:	pkgconfig(openal)
BuildRequires:	pkgconfig(pangocairo)
BuildRequires:	pkgconfig(portaudio-2.0)
BuildRequires:	pkgconfig(sdl2)
BuildRequires:	pkgconfig(sm)
BuildRequires:	pkgconfig(soundtouch)
BuildRequires:	pkgconfig(xi)
BuildRequires:	pkgconfig(xrandr)
BuildRequires:	pkgconfig(zlib)

%description
Gamecube / Wii / Triforce Emulator.

%files -f %{name}.lang
%doc license.txt Readme.txt
%attr(0755,root,root) %{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_iconsdir}/hicolor/*/apps/%{name}.png
%{_datadir}/pixmaps/%{name}.xpm

#----------------------------------------------------------------------------

%prep
%setup -q
%apply_patches

%build
mkdir -p build
cd build
export CFLAGS='%{optflags} -O3'
export CXXFLAGS='%{optflags} -O3'
cmake -DCMAKE_INSTALL_PREFIX=%{buildroot}/usr ..
%make

%install
%makeinstall -C build

# not wanted
rm -f %{buildroot}/usr/lib/libpolarssl.a

install -D -m 644 %{SOURCE13} %{buildroot}%{_iconsdir}/hicolor/16x16/apps/%{name}.png
install -D -m 644 %{SOURCE12} %{buildroot}%{_iconsdir}/hicolor/32x32/apps/%{name}.png
install -D -m 644 %{SOURCE11} %{buildroot}%{_iconsdir}/hicolor/64x64/apps/%{name}.png
install -D -m 644 %{SOURCE10} %{buildroot}%{_iconsdir}/hicolor/128x128/apps/%{name}.png
install -D -m 644 %{SOURCE9} %{buildroot}%{_iconsdir}/hicolor/256x256/apps/%{name}.png

install -d %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop << EOF
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

