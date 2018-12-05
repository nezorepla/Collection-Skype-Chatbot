#!/usr/bin/python
import os
import vodaucwa

import aiml

# Create the kernel and learn AIML files
kernel = aiml.Kernel()
kernel.learn("std-startup.xml")
kernel.respond("load aiml b")

# Press CTRL-C to break this loop
#while True:
#    print kernel.respond(raw_input("Enter your message >> "))



def messageReceived(message):
  #  message.reply("Selam %s, su an cevap veremesem de,bu mesaja en kisa zamanda cevap verecegim; \"%s\"." % (message.uri, message.message))
  message.reply("OTOMATIK CEVAP:\"%s\"</b>" % (kernel.respond(message.message)))


def main():
    bot = vodaucwa.LyncBot()
    bot.setMessageCallback(messageReceived)
    username = "xxx\\xxx"
    password = "xxx"
#    proxy = "http://proxy.company.com:80/"
#    os.environ["http_proxy"] = proxy
#    os.environ["https_proxy"] = proxy
    bot.authenticate("https://lyncdiscoverinternal.xxx.com.tr/", username, password)
    bot.loop()




    
if __name__ == '__main__':
    main()
