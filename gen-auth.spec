#
%include        /usr/lib/rpm/macros.perl
Summary:	SMTP authentication tool
Summary(pl.UTF-8):	Narzędzie do uwierzytelniania SMTP
Name:		gen-auth
Version:	20060620.0
Release:	1
License:	GPL v2+
Group:		Applications
# based on http://jetmore.org/john/code/gen-auth
Source0:	%{name}.pl
URL:		http://jetmore.org/john/code/#gen-auth
BuildRequires:	perl-tools-pod
BuildRequires:	rpm-perlprov
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
gen-auth is a tool that generates and decodes SMTP authentication
strings (PLAIN, LOGIN, CRAM-MD5, SPA).

%description -l pl.UTF-8
Narzędzie służące do generowania i dekodowania łancuchów
uwierzytelniania SMTP. Obsługiwane standardy to PLAIN, LOGIN, CRAM-MD5
i SPA.

%prep
%setup -q -c -T

%build
pod2man %SOURCE0 > gen-auth.1
pod2text %SOURCE0 > gen-auth.txt

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install %SOURCE0 $RPM_BUILD_ROOT%{_bindir}/%{name}
install gen-auth.1 $RPM_BUILD_ROOT%{_mandir}/man1/gen-auth.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}
%{_mandir}/man1/gen-auth.1*
%doc gen-auth.txt
