class MyContent:

    def __init__(self, my_content):
        self.my_content = my_content

    def format_content(self):
        return ''.join(['<MyML>', str(self.my_content), '</MyML>'])

    def __repr__(self):
        return f"{self.my_content}"


class Email:

    def __init__(self, protocol):
        self.protocol = protocol
        self.__sender = None
        self.__receiver = None
        self.__content = None

    def set_sender(self, sender):
        self.__sender = ''.join(["I'm ", sender])

    def set_receiver(self, receiver):
        self.__receiver = ''.join(["I'm ", receiver])

    def set_content(self, content):
        self.__content = content.format_content()

    def __repr__(self):

        template = "Sender: {sender}\nReceiver: {receiver}\nContent:\n{content}"

        return template.format(sender=self.__sender, receiver=self.__receiver, content=self.__content)



email = Email('IM')
email.set_sender('qmal')
print(email)
email.set_receiver('james')
content = MyContent('Hello, there!')
email.set_content(content)
print(email)
