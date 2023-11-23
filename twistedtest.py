from zope.interface import implements,interface
from twisted.cred import checkers,credentials,portal
from twisted.internet import protocol,reactor


from twisted.protocols import basic

class IProtocolAvater(Interface):
    def logout():
        """
        """

class EchoAvatar(object):
    implements(IProtocolAvater)

    def logout(self):
        pass



class Echo(basic.LineReceiver):
    portal = None
    avatar = None
    logout = None


    def connectionLost(self,reason):
        if self.logout:
            self.logout()
            self.avatar=None
            self.logout=None

    def lineReceived(self,line):
        if not self.avatar:
            username,password = line.strip().split(" ")
            self.tryLogin(username,password)
        else:
            self.sendline(line)

    def tryLogin(self,username, password):
        self.portal.login(credentials.UsernamePassword(username,password),None,IprotocolAvatar).addCallbacks(self._cbLogin,self._ebLogin)

    
        
