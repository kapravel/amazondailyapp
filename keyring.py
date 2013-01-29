import gnomekeyring

class Keyring():

    def __init__(self):
        if not hasattr(self, "keyring"):
            self.keyring = gnomekeyring.get_default_keyring_sync()

    def set_password(self, name, user, password, userid = ""):
        return gnomekeyring.item_create_sync(
                    self.keyring,
                    gnomekeyring.ITEM_GENERIC_SECRET,
                    name,
            {"user": user, "app":"amazon"},
                    password,
                    True)

    def get_user(self, item_id):
        try:
            items = gnomekeyring.find_items_sync(gnomekeyring.ITEM_GENERIC_SECRET, {"app":"amazon"})
            return items[0].attributes["user"]
        except (gnomekeyring.DeniedError, gnomekeyring.NoMatchError):
            return ""
    def get_password(self, item_id):
        try:
            items = gnomekeyring.find_items_sync(gnomekeyring.ITEM_GENERIC_SECRET, {"app":"amazon"})
            return items[0].secret
        except (gnomekeyring.DeniedError, gnomekeyring.NoMatchError):
            return ""

def keyring_setup(username, password):
	# use this to setup your keyring
	kr = Keyring()
	#XXX position 14 is arbitary and might delete a previous entry!
	kr.set_password("amazon", username, password, 14)
	kr.set_username("amazon", username, 14)
	print kr.get_password(14)
	print kr.get_user(14)
