import requests
from stellar_base.builder import Builder
from stellar_base.address import Address
from stellar_base.utils import StellarMnemonic
from stellar_base.keypair import Keypair



#secret is the phrase so user does not has to enter both
#public and private key
sm = StellarMnemonic("english")
secret = sm.generate()
kp = Keypair.deterministic(secret, lang="english", index=1)
publickey = kp.address().decode()
seed = kp.seed().decode()


url = 'https://friendbot.stellar.org'
r = requests.get(url, params={'addr':publickey})      
print(publickey, seed)



