%global tl_name wnri
%global tl_revision 22459

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Ridgeways fonts
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/wnri
License:	gpl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/wnri.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/wnri.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Fonts (as Metafont source) for Old English, Indic languages in Roman
transliteration and Puget Salish (Lushootseed) and other Native American
languages.

