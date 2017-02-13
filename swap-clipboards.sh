SRC=~/.config/google-chrome/Default/Local\ Storage/https_courses.edx.org_0.localstorage
TGT=~/.config/google-chrome/Default/Local\ Storage/http_localhost_8000.localstorage

echo "$SRC"
echo "$TGT"

cp "$SRC" /tmp/src_swap_store
cp "$TGT" /tmp/tgt_swap_store
cp /tmp/tgt_swap_store "$SRC"
cp /tmp/src_swap_store "$TGT"

