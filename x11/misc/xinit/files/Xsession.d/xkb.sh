USER_XKB=$HOME/.xkb
USER_KEYMAP=$USER_XKB/keymap/default

[ -r $USER_KEYMAP ] && xkbcomp -I$USER_XKB $USER_KEYMAP $DISPLAY