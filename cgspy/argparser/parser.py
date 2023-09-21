from argparse import ArgumentParser


class Arguments:
    def __init__(self):
        self.parser = ArgumentParser(
            description="Telegram Call IP Tracer"
        )

    
    def make_args(self):
        self.parser.add_argument(
            '-i',
            '--iface'
        )

    
    def parse_args(self):
        return self.parser.parse_args()
