from twisted.internet.task import react
from twisted.internet.defer import inlineCallbacks as coroutine
from autobahn.twisted.wamp import Session
from autobahn.twisted.connection import Connection


class MySession(Session):

    @coroutine
    def onJoin(self, details):
        print("on_join: {}".format(details))

        def add2(a, b):
            return a + b

        yield self.register(add2, u'com.example.add2')

        try:
            res = yield self.call(u'com.example.add2', 2, 3)
            print("result: {}".format(res))
        except Exception as e:
            print("error: {}".format(e))
        finally:
            self.leave()


if __name__ == '__main__':

    connection = Connection()
    connection.session = MySession
    react(connection.start)
