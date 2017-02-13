
EDX_LOCALSTORAGE="https_courses.edx.org_0.localstorage"
LOCAL_LOCALSTORAGE="http_localhost_8000.localstorage"

EDX=~/.config/google-chrome/Default/Local\ Storage/${EDX_LOCALSTORAGE}
LOCAL=~/.config/google-chrome/Default/Local\ Storage/${LOCAL_LOCALSTORAGE}
BACKUP_PATH=~/jade_utils/backups

# does the backup path exist?
# TODO really need to check this.


cp "$EDX" ${BACKUP_PATH}/${EDX_LOCALSTORAGE}.$(date +"%s")
cp "$LOCAL" ${BACKUP_PATH}/${LOCAL_LOCALSTORAGE}.$(date +"%s")
