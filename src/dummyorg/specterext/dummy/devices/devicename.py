import logging
from binascii import a2b_base64

from cryptoadvance.specter.device import Device
from cryptoadvance.specter.util.base43 import b43_encode
from cryptoadvance.specter.wallet import Wallet

logger = logging.getLogger(__name__)

class {{ext.devicename | camelcase }}(Device):
    # The device_type is deprecated. We have a class which already specifies the device_type
    device_type = "undefined"
    name = "Electrum"
    # Not yet existing. Put some icon here:
    icon = "{{ ext.id}}/img/devices/{{ext.devicename}}_icon.svg"
    
    template = "{{ ext.id}}/device/{{ext.devicename}}_new_device_keys.jinja"

    # pick and choose here
    sd_card_support = True
    qr_code_support = True
    qr_code_animate = "off"

    def create_psbts(self, base64_psbt, wallet):
        # remove non_witness utxo for QR code
        updated_psbt = wallet.fill_psbt(base64_psbt, non_witness=False, xpubs=False)
        psbts = {"qrcode": b43_encode(a2b_base64(updated_psbt)), "sdcard": base64_psbt}
        return psbts
