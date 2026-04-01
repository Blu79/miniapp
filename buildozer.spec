[app]
title = Rai Bai App
package.name = raibaiapp
package.domain = org.cu18cm
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0

requirements = python3,kivy==2.3.0,telethon

orientation = portrait
fullscreen = 0

# Quyền cần thiết
android.permissions = INTERNET,FOREGROUND_SERVICE,ACCESS_NETWORK_STATE

# Tên package
package.domain = org.cu18cm
package.name = raibaiapp

# Build cho cả 32bit và 64bit
android.arch = armeabi-v7a,arm64-v8a
