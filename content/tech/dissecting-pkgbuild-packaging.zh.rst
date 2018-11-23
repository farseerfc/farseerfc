深入淺出講 PKGBUILD 打包
===========================================

:id: dissecting-pkgbuild-packaging
:translation_id: dissecting-pkgbuild-packaging
:lang: zh
:date: 2018-11-19 17:15
:tags: linux, archlinux, pkgbuild, pacman
:status: draft

即便是 Arch Linux 初學者，也鮮有完全靠官方源中的軟件包就能過活的用戶，或多或少都得依賴一些第三方源或者 AUR 中的額外軟件包補充可用軟件庫。
成爲 Arch Linux 可信用戶(Trusted User) 也有三個年頭了，作爲 TU 的日常工作，就是審閱 AUR 上用戶提交的軟件包，遷移優秀的包進入 community 官方源，
自然積累了些許處理 PKGBUILD 打包的經驗。