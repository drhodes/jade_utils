
# this replaces localhosts clipboard with edx's

SRC=~/.config/google-chrome/Default/Local\ Storage/https_courses.edx.org_0.localstorage
TGT=~/.config/google-chrome/Default/Local\ Storage/http_localhost_8000.localstorage

echo "$SRC"
echo "$TGT"

cp "$SRC" "$TGT"
