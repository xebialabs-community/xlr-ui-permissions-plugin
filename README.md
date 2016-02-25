# XL Release UI Permissions Extension #

Provides a read only view for all permissions in the system. Shows up as a menu item in the top menu in XL Release UI. 

# Installation #

You can copy the pre build jar file from under the releases section under git repo

OR 

Build the project:
```
gradle build
```

Copy the extension to the plugins folder of your XLD installation:
```
cp ./build/libs/xlr-ui-permissions.jar $XLRelease_HOME/plugins
```


#Usage#

XL Release doesn't fully support UI Extensions functionality but the backend architecture is available. 

1. Open XL Release in a new browser window and then login.
2. Now open another tab in the same browser and type this [localhost:5516/static/4.8.0/web/permissions-plugin/permissions.html](localhost:5516/static/4.8.0/web/permissions-plugin/permissions.html)

(Note : the version 4.8.0 is the version of XL Release. if you use a different version then change the version in the URL.)



# Snapshot #

![Configuration] (/screenshot.png)
