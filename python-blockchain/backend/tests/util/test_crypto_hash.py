from backend.util.crypto_hash import crypto_hash


def test_crypto_hash():
    #it would create a same hash
    assert crypto_hash(1,[2],'three') == crypto_hash('three',1,[2])
    assert crypto_hash('vasu' == 'asdf')