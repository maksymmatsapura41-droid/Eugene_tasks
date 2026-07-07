from dataclasses import dataclass
from abc import ABC, abstractmethod
import asyncio
from typing import Protocol


@dataclass
class PaymentDetails:
    amount: float


@dataclass
class CardPaymentDetails(PaymentDetails):
    card_number: str
    cvv: str


@dataclass
class CryptoPaymentDetails(PaymentDetails):
    wallet_address: str
    network: str


class GatewayError(Exception):
    pass

class FraudSuspicionError(GatewayError):
    pass

class GasPriceTooHighError(GatewayError):
    pass

class AsyncPaymentGateway(ABC):
    @property
    @abstractmethod
    def currency(self):
        pass

    @abstractmethod
    async def payment_process(self, details: PaymentDetails) -> str:
        pass

class StripeAsyncGateway(AsyncPaymentGateway):
    @property
    def currency(self):
        return "$"

    async def payment_process(self, details: PaymentDetails) -> str:
        if not isinstance(details, CardPaymentDetails): raise TypeError
        await asyncio.sleep(1)
        if details.cvv == "000": raise FraudSuspicionError
        return "!"


class BinanceAsyncGateway(AsyncPaymentGateway):
    @property
    def currency(self):
        return "BTC"

    async def payment_process(self, details: PaymentDetails) -> str:
        if not isinstance(details, CryptoPaymentDetails): raise TypeError
        await asyncio.sleep(1)
        if details.amount > 10000: raise GasPriceTooHighError
        return "!"

class AsyncAnalyticsLogger(Protocol):
    async def log_success(self, tx_id, amount):
        pass

    async def log_error(self, error_msg):
        pass


class DatabaseAnalytics:
    async def log_success(self, tx_id, amount):
        await asyncio.sleep(0.05)

    async def log_error(self, error_msg):
        await asyncio.sleep(0.05)

class PaymentProcessor:
    def __init__(self, gateway: AsyncPaymentGateway, logger: AsyncAnalyticsLogger):
        self.gateway = gateway
        self.logger = logger

    async def checkout(self, details: PaymentDetails):
        try:
            x = await self.gateway.payment_process(details)
            await self.logger.log_success(x, details.amount)
        except Exception as e:
            await self.logger.log_error(e)


