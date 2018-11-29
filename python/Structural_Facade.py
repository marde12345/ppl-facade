class AccountNumberCheck:
	def __init__(self):
		self.__accountNumber = 5116100

	def getAccountNumber(self):
		return self.__accountNumber

	def accountActive(self, acctNumToCheck):
		if acctNumToCheck == self.getAccountNumber():
			return True
		else :
			return False

class WelcomeToBank:
	def __init__(self):
		print("Selamat datang di PPL Bank")

class SecurityCodeCheck:
	def __init__(self):
		self.__securityCode = 1234

	def getSecurityCode(self):
		return self.__securityCode

	def isCodeCorrect(self, secCodeToCheck):
		if secCodeToCheck == self.getSecurityCode():
			return True
		else :
			return False

class FundsCheck:
	def __init__(self):
		self.__cashInAccount = 10000

	def getCashInAccount(self):
		return self.__cashInAccount

	def decreaseCashInAccount(self, cashWithdrawn):
		self.__cashInAccount -= cashWithdrawn

	def increaseCashInAccount(self, cashDeposited):
		self.__cashInAccount += cashDeposited
	
	def haveEnoughMoney(self, cashToWithdrawal):
			if cashToWithdrawal > self.getCashInAccount():
				print("Maaf anda tidak memiliki cukup saldo")
				print("Saldo: ",self.getCashInAccount())
				return False
			else :
				self.decreaseCashInAccount(cashToWithdrawal)
				print("Penarikan sukses")
				return True

	def makeDeposit(self, cashToDeposit):
		self.increaseCashInAccount(cashToDeposit)
		print("Setoran berhasil")
		print("Saldo: ",self.getCashInAccount())

class BankAccountFacade:
	def __init__(self, newNum, newCode):
		self.__accountNumber = newNum
		self.__securityCode = newCode

		self.bankWelcome = WelcomeToBank()
		self.acctChecker = AccountNumberCheck()
		self.codeChecker = SecurityCodeCheck()
		self.fundChecker = FundsCheck()

	def getAccountNumber(self):
		return self.__accountNumber

	def getSecurityCode(self):
		return self.__securityCode

	def withdrawCash(self, cashToGet):
		if self.acctChecker.accountActive(self.getAccountNumber()) and self.codeChecker.isCodeCorrect(self.getSecurityCode()) and self.fundChecker.haveEnoughMoney(cashToGet) :
			print("Transaksi berhasil")
		else :
			print("Transaksi gagal")

	def depositCash(self, cashToDeposit):
		if self.acctChecker.accountActive(self.getAccountNumber()) and self.codeChecker.isCodeCorrect(self.getSecurityCode()):
			self.fundChecker.makeDeposit(cashToDeposit)
			print("Transaksi berhasil")
		else :
			print("Transaksi gagal")
		

fasmasign = BankAccountFacade(5116100,1234)


fasmasign.depositCash(5000)
fasmasign.withdrawCash(15000)