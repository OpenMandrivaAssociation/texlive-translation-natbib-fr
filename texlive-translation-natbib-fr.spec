%global tl_name translation-natbib-fr
%global tl_revision 79618

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	French translation of the documentation of natbib
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/info/translations/natbib/fr
License:	lppl1
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/translation-natbib-fr.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/translation-natbib-fr.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
A French translation of the documentation of natbib.

