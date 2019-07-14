#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x58D0EE648A48B3BB (faure@kde.org)
#
Name     : kmediaplayer
Version  : 5.60.0
Release  : 12
URL      : https://download.kde.org/stable/frameworks/5.60/portingAids/kmediaplayer-5.60.0.tar.xz
Source0  : https://download.kde.org/stable/frameworks/5.60/portingAids/kmediaplayer-5.60.0.tar.xz
Source99 : https://download.kde.org/stable/frameworks/5.60/portingAids/kmediaplayer-5.60.0.tar.xz.sig
Summary  : Plugin interface for media player features
Group    : Development/Tools
License  : X11
Requires: kmediaplayer-data = %{version}-%{release}
Requires: kmediaplayer-lib = %{version}-%{release}
Requires: kmediaplayer-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde

%description
# KMediaPlayer
Interface for media player KParts
## Introduction
KMediaPlayer builds on the KParts framework to provide a common interface for
KParts that can play media files.

%package data
Summary: data components for the kmediaplayer package.
Group: Data

%description data
data components for the kmediaplayer package.


%package dev
Summary: dev components for the kmediaplayer package.
Group: Development
Requires: kmediaplayer-lib = %{version}-%{release}
Requires: kmediaplayer-data = %{version}-%{release}
Provides: kmediaplayer-devel = %{version}-%{release}
Requires: kmediaplayer = %{version}-%{release}
Requires: kmediaplayer = %{version}-%{release}

%description dev
dev components for the kmediaplayer package.


%package lib
Summary: lib components for the kmediaplayer package.
Group: Libraries
Requires: kmediaplayer-data = %{version}-%{release}
Requires: kmediaplayer-license = %{version}-%{release}

%description lib
lib components for the kmediaplayer package.


%package license
Summary: license components for the kmediaplayer package.
Group: Default

%description license
license components for the kmediaplayer package.


%prep
%setup -q -n kmediaplayer-5.60.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1563074363
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake ..
make  %{?_smp_mflags} VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1563074363
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kmediaplayer
cp LICENSE %{buildroot}/usr/share/package-licenses/kmediaplayer/LICENSE
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/dbus-1/interfaces/kf5_org.kde.KMediaPlayer.xml
/usr/share/kservicetypes5/kmediaplayer.desktop
/usr/share/kservicetypes5/kmediaplayerengine.desktop

%files dev
%defattr(-,root,root,-)
/usr/include/KF5/KMediaPlayer/KMediaPlayer/Player
/usr/include/KF5/KMediaPlayer/KMediaPlayer/View
/usr/include/KF5/KMediaPlayer/kmediaplayer/kmediaplayer_export.h
/usr/include/KF5/KMediaPlayer/kmediaplayer/player.h
/usr/include/KF5/KMediaPlayer/kmediaplayer/view.h
/usr/include/KF5/kmediaplayer_version.h
/usr/lib64/cmake/KF5MediaPlayer/KF5MediaPlayerConfig.cmake
/usr/lib64/cmake/KF5MediaPlayer/KF5MediaPlayerConfigVersion.cmake
/usr/lib64/cmake/KF5MediaPlayer/KF5MediaPlayerTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KF5MediaPlayer/KF5MediaPlayerTargets.cmake
/usr/lib64/libKF5MediaPlayer.so

%files lib
%defattr(-,root,root,-)
/usr/lib64/libKF5MediaPlayer.so.5
/usr/lib64/libKF5MediaPlayer.so.5.60.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kmediaplayer/LICENSE
