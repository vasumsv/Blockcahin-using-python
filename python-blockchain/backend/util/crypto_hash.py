import hashlib # sha 256 hash
import json 

def stringify(data):
    return json.dumps(data)

def crypto_hash(*args):
    """
    retrun sha 256 hash of the given data
    """

    stringified_args = sorted(map(lambda data: json.dumps(data),args))
    joined_data = ''.join(stringified_args)

    return hashlib.sha256(joined_data.encode('utf-8')).hexdigest()  #uta byte string represention and 64 hexa deciamal 

def main():
    print(f"crypto_hash('one',2,[3]):{crypto_hash('one',2,[3])}")
    
    print(f"crypto_hash(4,'vasu',[3]):{crypto_hash(4,'vasu',[3])}")

if __name__ =='__main__':
    main()
