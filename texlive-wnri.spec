# revision 22459
# category Package
# catalog-ctan /fonts/wnri
# catalog-date 2011-05-06 00:38:04 +0200
# catalog-license gpl
# catalog-version undef
Name:		texlive-wnri
Version:	20110506
Release:	2
Summary:	Ridgeway's fonts
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/wnri
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/wnri.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/wnri.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Fonts (as Metafont source) for Old English, Indic languages in
Roman transliteration and Puget Salish (Lushootseed) and other
Native American languages.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/source/public/wnri/acctmax.mf
%{_texmfdistdir}/fonts/source/public/wnri/acutacct.mf
%{_texmfdistdir}/fonts/source/public/wnri/addpunc.mf
%{_texmfdistdir}/fonts/source/public/wnri/baraacct.mf
%{_texmfdistdir}/fonts/source/public/wnri/bargacct.mf
%{_texmfdistdir}/fonts/source/public/wnri/bnduacct.mf
%{_texmfdistdir}/fonts/source/public/wnri/brbracct.mf
%{_texmfdistdir}/fonts/source/public/wnri/brevacct.mf
%{_texmfdistdir}/fonts/source/public/wnri/cdilacct.mf
%{_texmfdistdir}/fonts/source/public/wnri/facutact.mf
%{_texmfdistdir}/fonts/source/public/wnri/fbaraact.mf
%{_texmfdistdir}/fonts/source/public/wnri/fbargact.mf
%{_texmfdistdir}/fonts/source/public/wnri/fbrevact.mf
%{_texmfdistdir}/fonts/source/public/wnri/fgravact.mf
%{_texmfdistdir}/fonts/source/public/wnri/fhachact.mf
%{_texmfdistdir}/fonts/source/public/wnri/fhattact.mf
%{_texmfdistdir}/fonts/source/public/wnri/fubrvact.mf
%{_texmfdistdir}/fonts/source/public/wnri/fudacact.mf
%{_texmfdistdir}/fonts/source/public/wnri/fudgract.mf
%{_texmfdistdir}/fonts/source/public/wnri/gamma.mf
%{_texmfdistdir}/fonts/source/public/wnri/gram_max.mf
%{_texmfdistdir}/fonts/source/public/wnri/grampunc.mf
%{_texmfdistdir}/fonts/source/public/wnri/gravacct.mf
%{_texmfdistdir}/fonts/source/public/wnri/greeks.mf
%{_texmfdistdir}/fonts/source/public/wnri/haccbase.mf
%{_texmfdistdir}/fonts/source/public/wnri/hachacct.mf
%{_texmfdistdir}/fonts/source/public/wnri/hattacct.mf
%{_texmfdistdir}/fonts/source/public/wnri/iaesc.mf
%{_texmfdistdir}/fonts/source/public/wnri/ibrvacct.mf
%{_texmfdistdir}/fonts/source/public/wnri/igamma.mf
%{_texmfdistdir}/fonts/source/public/wnri/italcskt.mf
%{_texmfdistdir}/fonts/source/public/wnri/italla.mf
%{_texmfdistdir}/fonts/source/public/wnri/ligature.mf
%{_texmfdistdir}/fonts/source/public/wnri/ligaturi.mf
%{_texmfdistdir}/fonts/source/public/wnri/macracct.mf
%{_texmfdistdir}/fonts/source/public/wnri/mudaacct.mf
%{_texmfdistdir}/fonts/source/public/wnri/odotacct.mf
%{_texmfdistdir}/fonts/source/public/wnri/orngacct.mf
%{_texmfdistdir}/fonts/source/public/wnri/product.mf
%{_texmfdistdir}/fonts/source/public/wnri/romanla.mf
%{_texmfdistdir}/fonts/source/public/wnri/romanskt.mf
%{_texmfdistdir}/fonts/source/public/wnri/romanua.mf
%{_texmfdistdir}/fonts/source/public/wnri/sktmisc.mf
%{_texmfdistdir}/fonts/source/public/wnri/tildacct.mf
%{_texmfdistdir}/fonts/source/public/wnri/u-ring.mf
%{_texmfdistdir}/fonts/source/public/wnri/ubaracct.mf
%{_texmfdistdir}/fonts/source/public/wnri/ubrvacct.mf
%{_texmfdistdir}/fonts/source/public/wnri/udacacct.mf
%{_texmfdistdir}/fonts/source/public/wnri/udgracct.mf
%{_texmfdistdir}/fonts/source/public/wnri/udmcacct.mf
%{_texmfdistdir}/fonts/source/public/wnri/udotacct.mf
%{_texmfdistdir}/fonts/source/public/wnri/uibvacct.mf
%{_texmfdistdir}/fonts/source/public/wnri/umlaacct.mf
%{_texmfdistdir}/fonts/source/public/wnri/urmcacct.mf
%{_texmfdistdir}/fonts/source/public/wnri/urngacct.mf
%{_texmfdistdir}/fonts/source/public/wnri/uumlacct.mf
%{_texmfdistdir}/fonts/source/public/wnri/wnindic.map
%{_texmfdistdir}/fonts/source/public/wnri/wnrib10.mf
%{_texmfdistdir}/fonts/source/public/wnri/wnrib8.mf
%{_texmfdistdir}/fonts/source/public/wnri/wnribi10.mf
%{_texmfdistdir}/fonts/source/public/wnri/wnrii10.mf
%{_texmfdistdir}/fonts/source/public/wnri/wnrii8.mf
%{_texmfdistdir}/fonts/source/public/wnri/wnrir10.mf
%{_texmfdistdir}/fonts/source/public/wnri/wnrir8.mf
%{_texmfdistdir}/fonts/source/public/wnri/wnris10.mf
%{_texmfdistdir}/fonts/source/public/wnri/wnris8.mf
%{_texmfdistdir}/fonts/source/public/wnri/wnrit10.mf
%{_texmfdistdir}/fonts/source/public/wnri/wnrit8.mf
%{_texmfdistdir}/fonts/tfm/public/wnri/wnrib10.tfm
%{_texmfdistdir}/fonts/tfm/public/wnri/wnrib8.tfm
%{_texmfdistdir}/fonts/tfm/public/wnri/wnribi10.tfm
%{_texmfdistdir}/fonts/tfm/public/wnri/wnrii10.tfm
%{_texmfdistdir}/fonts/tfm/public/wnri/wnrii8.tfm
%{_texmfdistdir}/fonts/tfm/public/wnri/wnrir10.tfm
%{_texmfdistdir}/fonts/tfm/public/wnri/wnrir8.tfm
%{_texmfdistdir}/fonts/tfm/public/wnri/wnris10.tfm
%{_texmfdistdir}/fonts/tfm/public/wnri/wnris8.tfm
%{_texmfdistdir}/fonts/tfm/public/wnri/wnrit10.tfm
%{_texmfdistdir}/fonts/tfm/public/wnri/wnrit8.tfm
%doc %{_texmfdistdir}/doc/fonts/wnri/README
%doc %{_texmfdistdir}/doc/fonts/wnri/old/README
%doc %{_texmfdistdir}/doc/fonts/wnri/old/barnett.map
%doc %{_texmfdistdir}/doc/fonts/wnri/old/lushucid.map
%doc %{_texmfdistdir}/doc/fonts/wnri/old/newgb.map

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts doc %{buildroot}%{_texmfdistdir}
