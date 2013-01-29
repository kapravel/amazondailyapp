import gnomekeyring
import glib
glib.set_application_name('Amazon daily app downloader')


class Keyring():
    """ Easy interface for Gnome-keyring."""

    def __init__(self):
        if not gnomekeyring.is_available():
            raise Exception("Gnome keyring not available!")
        self.keyring_name = gnomekeyring.get_default_keyring_sync()

    def set_password(self, key_name, user, password):
        return gnomekeyring.item_create_sync(
                    self.keyring_name,
                    gnomekeyring.ITEM_GENERIC_SECRET,
                    key_name,
                    {"user": user,
                      "key_name": key_name},
                    password,
                    True)

    def __get_credentials(self, key_name):
        try:
            items = gnomekeyring.find_items_sync(
                gnomekeyring.ITEM_GENERIC_SECRET,
                {"key_name": key_name})
            return items[0].attributes["user"], items[0].secret
        except (gnomekeyring.DeniedError, gnomekeyring.NoMatchError):
            return None, None

    def get_user(self, key_name):
        return self.__get_credentials(key_name)[0]

    def get_password(self, key_name):
        return self.__get_credentials(key_name)[1]


if __name__ == '__main__':
    kr = Keyring()
    kr.set_password('test_amazon', 'test_user', 'test_password')
    assert 'test_user' == kr.get_user('test_amazon')
    assert 'test_password' == kr.get_password('test_amazon')
    print "All tests OK."
