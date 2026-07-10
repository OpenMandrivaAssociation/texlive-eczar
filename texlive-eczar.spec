%global tl_name eczar
%global tl_revision 57716

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.1
Release:	%{tl_revision}.1
Summary:	A font family supporting Devanagari and Latin script
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/eczar
License:	ofl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/eczar.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/eczar.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
rojhettaa sNsthecaa egjhaar haa yunikodd aadhaarit mukt ttNk aahe. hyaa
ttNkaat 45+3 bhaassaa leNttin v devnaagrii lipiit purskRt kelyaa
jaataat. vaibhv siNh hyaaNnii hyaa ttNkaacaa abhiklp kelaa aahe v
aajnyaavlii tsec nirmitii ddevhidd brejhiinaa hyaaNnii kelii aahe.
egzaar yh rozettaa dvaaraa prkaashit yunikodd aadhaarit mukt ttNk hai /
is ttNk dvaaraa 45+3 bhaassaaeN laittin tthaa devnaagrii lipi meN
purskRt kii jaatii hai / vaibhv siNh ne is kaa abhiklp kiyaa hai aur
aajnyaavli tthaa nirmiti ddevidd breziinaa dvaaraa kii gyii hai / Eczar
is an open-source type family published by Rosetta. The fonts support
over 45+3 languages in Latin and Devanagari scripts in 5 weights. These
fonts were designed by Vaibhav Singh, code and production are by David
Brezina.

