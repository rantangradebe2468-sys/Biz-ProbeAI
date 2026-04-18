[app]

title = BizProbe AI
package.name = bizprobe
package.domain = org.bizprobe

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,csv,json

version = 1.0

requirements = python3,kivy

orientation = portrait

fullscreen = 0

# App icon (optional later)
# icon.filename = logo.png

# Permissions (safe default)
android.permissions = INTERNET

# Android settings
android.api = 33
android.minapi = 21

# Keep logs off for release
log_level = 2

[buildozer]

log_level = 2
warn_on_root = 1