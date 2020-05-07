adb devices
adb shell input keyevent 26
Start-Sleep -s 0.5
adb shell input swipe 500 1000 500 20 500
Start-Sleep -s 0.5
adb shell input text  "132659"
Start-Sleep -s 0.5
adb shell am start -n jp.goodsmile.touhoulostword_android/com.google.firebase.MessagingUnityPlayerActivity
Start-Sleep -s 3
python screen.py
