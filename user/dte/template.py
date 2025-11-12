pkgname = "dte"
pkgver = "1.11.1"
pkgrel = 0
build_style = "makefile"
make_install_env = {"prefix": "/usr"}
hostmakedepends = ["gmake"]
pkgdesc = "Terminal text editor"
license = "GPL-2.0-or-later"
url = "https://craigbarnes.gitlab.io/dte"
source = f"https://craigbarnes.gitlab.io/dist/dte/dte-{pkgver}.tar.gz"
sha256 = "3d7d0d375fd31906ed436de20161dddc42d97f969a93d22b02aecfc3451e6c39"

def post_install(self):
    self.install_license("LICENSE")
    self.install_man("docs/dte.1")
    self.install_man("docs/dte-syntax.5")
    self.install_man("docs/dterc.5")
