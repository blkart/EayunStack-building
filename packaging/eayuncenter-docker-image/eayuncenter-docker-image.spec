%global image_name eayuncenter

Name:		eayuncenter-docker-image
Version:	0.1
Release:	1%{?dist}
Summary:	EayunCenter Docker Image

Group:		Application
License:	GPL
URL:		http://eayun.com
Source0:	eayuncenter-docker-image-%{version}.tgz

BuildRequires:	/bin/bash
Requires:	docker

%description
EayunCenter Docker Image

%prep
%setup -q


%build


%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/eayuncenter/
install -p -D -m 644 eayuncenter-image.tar %{buildroot}/usr/share/eayuncenter/

%post

%postun

%files
%doc
%attr(0755,root,root)/usr/share/eayuncenter
%attr(0644,root,root)/usr/share/eayuncenter/eayuncenter-image.tar


%changelog
* Thu Sep 28 2017 blkart <blkart.org@gmail.com> 0.1-1
- test version
