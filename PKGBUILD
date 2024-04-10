# Maintainer: Timot <filmabemtv2@gmail.com>
pkgname=joma
pkgver=0.0.1
pkgrel=1
pkgdesc="My first attempt to make a wrapper (kinda) for pacman and for a configurable aur helper"
arch=('x86_64')
url=""
license=('MIT')
groups=()
depends=()
makedepends=('git')
checkdepends=()
optdepends=()
provides=('joma')
conflicts=('joma')
replaces=('joma')
backup=()
options=()
changelog=
source=(
    "joma.py"
    'config.yaml'
    )
sha256sums=('')

package() {
    install -Dm 755 "${srcdir}/joma.py" "${pkgdir}/usr/bin/joma"
    install -Dm 644 "${srcdir}/config.yaml" "${pkgdir}/etc/skel/.config/joma-config.yaml"

}

post_install() {
    for home in /home/*; do
        if [ -d "$home" ]; then
            cp /etc/skel/.config/joma-config.yaml "$home/.config/joma-config.yaml"
            chown $(basename $home):$(basename $home) "$home/.config/joma-config.yaml"
        fi
    done
}

post_upgrade() {
    # This function does nothing.
    :
}
