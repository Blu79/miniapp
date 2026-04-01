[app]
title = Rai Bai App
package.name = raibaiapp
package.domain = org.cu18cm
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0

# Requirements
requirements = python3,kivy==2.3.0,telethon

orientation = portrait
fullscreen = 0

# Quyền Android (rất quan trọng)
android.permissions = INTERNET,FOREGROUND_SERVICE,ACCESS_NETWORK_STATE,WAKE_LOCK

# Package
package.domain = org.cu18cm
package.name = raibaiapp

# Build cho cả 32bit và 64bit
android.arch = armeabi-v7a,arm64-v8a

# Tăng bộ nhớ nếu build chậm
p4a.bootstrap = sdl2
