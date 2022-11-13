Name:		texlive-translation-natbib-fr
Version:	25105
Release:	1
Summary:	French translation of the documentation of natbib
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/info/translations/natbib/fr
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/translation-natbib-fr.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/translation-natbib-fr.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg

%description
A French translation of the documentation of natbib.

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/latex/translation-natbib-fr/f-natbib.dtx
%doc %{_texmfdistdir}/doc/latex/translation-natbib-fr/f-natbib.pdf

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
