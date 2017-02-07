from wallet.factory import WalletFactory
from wallet.models import Transaction

from django.test import RequestFactory
from semillas_backend.users.models import User
from semillas_backend.users.factory import UserFactory

class TestWalletModel():

    def setUp(self):
        self.factory = RequestFactory()

class TestWalletMethonds(TestWalletModel):

    def setUp(self):
        # call BaseServiceTestCase.setUp()
        super(TestWalletMethonds, self).setUp()

        self.users = UserFactory.create_batch(size=5,)
        self.wallets = WalletFactory.create_batch(size=User.objects.count(),)

    def test_transfer(self):

        self.users[0].wallet.first().transfer(self.users[1].wallet.first(), 5)
        # Check that the transaction is created with the correct value
        self.assertEqual(
            Transaction.objects.first().value,
            5
        )
        # Check that the balance on source wallet is updated
        self.assertEqual(
            self.users[0].wallet.first().balance,
            5
        )
        # Check that the balance on dest wallet is updated
        self.assertEqual(
            self.users[1].wallet.first().balance,
            15
        )
