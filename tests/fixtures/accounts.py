from factories.accounts import AccountFactory

def make_objects():
    """ return a list of new accounts """
    AccountFactory.create_batch(2)
    AccountFactory()
    AccountFactory(name='Anthony Hopkins', member=True)
    

