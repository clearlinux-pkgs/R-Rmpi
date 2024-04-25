#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
# autospec version: v3
# autospec commit: c1050fe
#
Name     : R-Rmpi
Version  : 0.7.2
Release  : 58
URL      : https://cran.r-project.org/src/contrib/Rmpi_0.7-2.tar.gz
Source0  : https://cran.r-project.org/src/contrib/Rmpi_0.7-2.tar.gz
Summary  : Interface (Wrapper) to MPI (Message-Passing Interface)
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-Rmpi-lib = %{version}-%{release}
Requires: openmpi
BuildRequires : buildreq-R
BuildRequires : openmpi-dev
BuildRequires : openssh
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
provides interactive R manager and worker environment.

%package lib
Summary: lib components for the R-Rmpi package.
Group: Libraries

%description lib
lib components for the R-Rmpi package.


%prep
%setup -q -n Rmpi
pushd ..
cp -a Rmpi buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1702503274

%install
export SOURCE_DATE_EPOCH=1702503274
rm -rf %{buildroot}
LANG=C.UTF-8
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -flto -fno-semantic-interposition "
FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -flto -fno-semantic-interposition "
AR=gcc-ar
RANLIB=gcc-ranlib
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL  --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper -mprefer-vector-width=512  " >> ~/.R/Makevars
R CMD INSTALL --preclean  --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean  --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/usr/lib64/R/library/Rmpi/CITATION
/usr/lib64/R/library/Rmpi/DESCRIPTION
/usr/lib64/R/library/Rmpi/INDEX
/usr/lib64/R/library/Rmpi/MacR64slaves.sh
/usr/lib64/R/library/Rmpi/Meta/Rd.rds
/usr/lib64/R/library/Rmpi/Meta/demo.rds
/usr/lib64/R/library/Rmpi/Meta/features.rds
/usr/lib64/R/library/Rmpi/Meta/hsearch.rds
/usr/lib64/R/library/Rmpi/Meta/links.rds
/usr/lib64/R/library/Rmpi/Meta/nsInfo.rds
/usr/lib64/R/library/Rmpi/Meta/package.rds
/usr/lib64/R/library/Rmpi/NAMESPACE
/usr/lib64/R/library/Rmpi/R/Rmpi
/usr/lib64/R/library/Rmpi/R/Rmpi.rdb
/usr/lib64/R/library/Rmpi/R/Rmpi.rdx
/usr/lib64/R/library/Rmpi/Rprofile
/usr/lib64/R/library/Rmpi/Rslaves.sh
/usr/lib64/R/library/Rmpi/Rslaves32.cmd
/usr/lib64/R/library/Rmpi/Rslaves64.cmd
/usr/lib64/R/library/Rmpi/cslavePI.c
/usr/lib64/R/library/Rmpi/demo/cslavePI.R
/usr/lib64/R/library/Rmpi/demo/masterslavePI.R
/usr/lib64/R/library/Rmpi/demo/simPI.R
/usr/lib64/R/library/Rmpi/demo/simplePI.R
/usr/lib64/R/library/Rmpi/demo/slave1PI.R
/usr/lib64/R/library/Rmpi/demo/slave2PI.R
/usr/lib64/R/library/Rmpi/help/AnIndex
/usr/lib64/R/library/Rmpi/help/Rmpi.rdb
/usr/lib64/R/library/Rmpi/help/Rmpi.rdx
/usr/lib64/R/library/Rmpi/help/aliases.rds
/usr/lib64/R/library/Rmpi/help/paths.rds
/usr/lib64/R/library/Rmpi/html/00Index.html
/usr/lib64/R/library/Rmpi/html/R.css
/usr/lib64/R/library/Rmpi/slavedaemon.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/Rmpi/libs/Rmpi.so
/usr/lib64/R/library/Rmpi/libs/Rmpi.so.avx2
/usr/lib64/R/library/Rmpi/libs/Rmpi.so.avx512
