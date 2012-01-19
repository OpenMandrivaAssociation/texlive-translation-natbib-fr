# revision 25105
# category Package
# catalog-ctan /info/translations/natbib/fr
# catalog-date 2012-01-14 10:04:15 +0100
# catalog-license lppl
# catalog-version undef
Name:		texlive-translation-natbib-fr
Version:	20120114
Release:	1
Summary:	French translation of the documentation of natbib
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/info/translations/natbib/fr
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/translation-natbib-fr.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/translation-natbib-fr.doc.tar.xz
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
