#!/usr/bin/python
import os
import vodaucwa


def messageReceived(message):
  #  message.reply("Selam %s, su an cevap veremesem de,bu mesaja en kisa zamanda cevap verecegim; \"%s\"." % (message.uri, message.message))
  message.reply("OTOMATIK CEVAP: Selam, su an cevap veremesem de,bu mesaja en kisa zamanda cevap verecegim; <b>\"%s\"</b>" % ( message.message))

sicil=""
 
def main():
    bot = vodaucwa.LyncBot()
    bot.setMessageCallback(messageReceived)
    username = "xxxx\\xxxxx"
    password = "xxxxx"
#    proxy = "http://proxy.company.com:80/"
#    os.environ["http_proxy"] = proxy
#    os.environ["https_proxy"] = proxy
    bot.authenticate("https://lyncdiscoverinternal.xxx.com.tr/", username, password)
    bot.loop()

if __name__ == '__main__':
    main()
