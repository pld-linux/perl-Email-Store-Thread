#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Email
%define	pnam	Store-Thread
Summary:	Email::Store::Thread - store threading information for a mail
Summary(pl.UTF-8):	Email::Store::Thread - przechowywanie informacji o wątkowaniu dla poczty
Name:		perl-Email-Store-Thread
Version:	1.1
Release:	1
License:	unknown
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	ab76577ddb077bb59f00d8cf684f9be4
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Email-Folder
BuildRequires:	perl-Email-Store
BuildRequires:	perl(Mail::Thread) >= 2.5
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This adds to a mail the concept of a thread container. A thread
container is a node in a tree which represents the thread of an email
conversation. It plugs into the indexing process and works out where
in the tree the mail belongs; you can then ask a mail for its
container, a container for its message, and for its parent, child and
sibling containers, which are used to navigate the thread tree.
There's also a root container which represents the top message in the
tree.

This is distributed separately from the main Email::Store distribution
as as it tends to slow down indexing somewhat.

%description -l pl.UTF-8
Ten moduł dodaje do poczty ideę kontenera wątków. Kontener wątków to
węzeł w drzewie reprezentujący wątek korespondencji pocztowej. Włącza
się do procesu indeksowania i działa tam, gdzie w drzewie należy dany
list; można odpytać list o jego kontener, kontener jego wiadomości
oraz o kontenery rodzica, potomka i rodzeństwa, używane do nawigacji w
drzewie wątków. Jest także kontener "root" reprezentujący górną
wiadomość w drzewie.

Moduł jest rozprowadzany jako wydzielony z dystrybucji Email::Store,
jako że wydaje się zwalniać trochę indeksowanie.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/Email/Store/*.pm
%{_mandir}/man3/*
