[app]
# (str) Title of your application
title = PymonSays  # Change to SymonSays if preferred

# (str) Package name
package.name = pymonsays  # Or symonsays if you prefer

# (str) Package domain
package.domain = com.codecodes

# (str) Source code where the main.py file is located
source.dir = .

# (str) The entry point of the application (the script that starts the app)
source.include_exts = py,png,jpg,kv,wav,ico

# (str) Application version
version = 1.0

# (str) Application icon
icon.filename = icon.ico

# (str) Supported orientation (one of: portrait, landscape, sensor, or any)
orientation = portrait

# (bool) Indicate if the application is fullscreen
fullscreen = 1

# (list) Permissions required by your app
android.permissions = 

# (str) The file to execute, relative to the source directory
entrypoint = main.py

# (list) Include specific libraries or modules required by your app
requirements = kivy,pygame,comtypes>=1.4.8,<2.0,pydub>=0.25.1,<1.0,pypiwin32>=223,<224,pyttsx3>=2.98,<3.0,pywin32>=308,<309

# (str) Package the app in debug mode (for testing) or release mode (for production)
debug = 1

# (str) Presplash image used during app startup
presplash.filename = presplash.png

# (list) Files to include in the .apk package
android.include_exts = wav,ico,png

# (list) Exclude files or directories from the APK
android.exclude_exts = txt,md,gitignore

[buildozer]
# (str) Log level: (info, debug, error, warning)
log_level = 2

# (bool) Automatically answer 'yes' to all Buildozer prompts
auto_accept_license = True
