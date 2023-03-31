Name:		texlive-eczar
Version:	57716
Release:	2
Summary:	A font family supporting Devanagari and Latin script
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/eczar
License:	ofl
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/eczar.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/eczar.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
rojhettaa sNsthecaa egjhaar haa yunikodd aadhaarit mukt ttNk
aahe. hyaa ttNkaat 45+3 bhaassaa leNttin v devnaagrii lipiit
purskRt kelyaa jaataat. vaibhv siNh hyaaNnii hyaa ttNkaacaa
abhiklp kelaa aahe v aajnyaavlii tsec nirmitii ddevhidd
brejhiinaa hyaaNnii kelii aahe. egzaar yh rozettaa dvaaraa
prkaashit yunikodd aadhaarit mukt ttNk hai / is ttNk dvaaraa
45+3 bhaassaaeN laittin tthaa devnaagrii lipi meN purskRt kii
jaatii hai / vaibhv siNh ne is kaa abhiklp kiyaa hai aur
aajnyaavli tthaa nirmiti ddevidd breziinaa dvaaraa kii gyii hai
/ Eczar is an open-source type family published by Rosetta. The
fonts support over 45+3 languages in Latin and Devanagari
scripts in 5 weights. These fonts were designed by Vaibhav
Singh, code and production are by David Brezina.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/fonts/opentype/public/eczar
%doc %{_texmfdistdir}/doc/fonts/eczar

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
