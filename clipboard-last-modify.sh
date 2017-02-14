EDX_LOCALSTORAGE="https_courses.edx.org_0.localstorage"
LOCAL_LOCALSTORAGE="http_localhost_8000.localstorage"

SRC=~/.config/google-chrome/Default/Local\ Storage/$EDX_LOCALSTORAGE
TGT=~/.config/google-chrome/Default/Local\ Storage/$LOCAL_LOCALSTORAGE

# stat "$SRC" | grep modify
# stat "$TGT" | grep modify

echo $SRC
stat "$SRC" | grep Modify

echo ""
echo $TGT
stat "$TGT" | grep Modify
