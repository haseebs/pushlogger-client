pkgname=pushlogger-client
pkgver=0.1
pkgrel=1
pkgdesc="Push output of scripts to android application through a server"
arch=("any")
url="https://github.com/haseebs/pushlogger-client"
license=('MIT')
depends=('curl')
source=("git://github.com/haseebs/${pkgname}/")
sha1sums=('SKIP')

package() {
    cd "$pkgname"
    mkdir -p $pkgdir/usr/bin
    mv push $pkgdir/usr/bin/$pkgname
}
