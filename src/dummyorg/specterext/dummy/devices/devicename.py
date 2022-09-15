from binascii import a2b_base64
from typing import List
from cryptoadvance.specter.util.base43 import b43_encode
from cryptoadvance.specter.device import Device


class {{ ext.devicename }}(Device):
    ''' This Device should be better described '''
    # the device_type is a string representation of this class which will be used in the
    # json-file of a device of that type. Simply use the class-name lowercase
    # and make sure it's unique
    device_type = "{{ ext.devicename | snakecase }}"
    # Will be shown when adding a new device and as a searchterm
    name = "{{ ext.devicename }}"
    # The Icon. Use a b/w.svg
    icon = "{{ ext.id }}/img/device_icon.svg"
    # optional, You might want to have a more specific template for creating a new device
    #template = "electrum/device/new_device_keys_electrum.jinja"

    # If your device is a classic Hardwarewallets, it might have one of these features:
    sd_card_support = True
    qr_code_support = True

    # auto, off or on
    # seedsigner uses on. By default it's auto.
    qr_code_animate = "off"

    # The most relevant method to implement
    def create_psbts(self, base64_psbt, wallet):
        # in QR codes keep only xpubs
        qr_psbt = wallet.fill_psbt(base64_psbt, non_witness=False, xpubs=True)
        # in SD card put as much as possible
        sd_psbt = wallet.fill_psbt(base64_psbt, non_witness=True, xpubs=True)
        psbts = {"qrcode": qr_psbt, "sdcard": sd_psbt}
        return psbts