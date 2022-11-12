from dataclasses import dataclass
from typing import Any, List, TypeVar, Type, cast, Callable
from datetime import datetime

T = TypeVar("T")


def from_float(x: Any) -> float:
    assert isinstance(x, (float, int)) and not isinstance(x, bool)
    return float(x)


def to_float(x: Any) -> float:
    assert isinstance(x, float)
    return x


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def from_datetime(x: Any) -> datetime:
    return datetime.fromisoformat(x)


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


@dataclass
class Coordinates:
    lat: float
    lng: float

    @staticmethod
    def from_dict(obj: Any) -> 'Coordinates':
        assert isinstance(obj, dict)
        lat = from_float(obj.get("lat"))
        lng = from_float(obj.get("lng"))
        return Coordinates(lat, lng)

    def to_dict(self) -> dict:
        result: dict = {}
        result["lat"] = to_float(self.lat)
        result["lng"] = to_float(self.lng)
        return result


@dataclass
class Address:
    city: str
    street_name: str
    street_address: str
    zip_code: str
    state: str
    country: str
    coordinates: Coordinates

    @staticmethod
    def from_dict(obj: Any) -> 'Address':
        assert isinstance(obj, dict)
        city = from_str(obj.get("city"))
        street_name = from_str(obj.get("street_name"))
        street_address = from_str(obj.get("street_address"))
        zip_code = from_str(obj.get("zip_code"))
        state = from_str(obj.get("state"))
        country = from_str(obj.get("country"))
        coordinates = Coordinates.from_dict(obj.get("coordinates"))
        return Address(city, street_name, street_address, zip_code, state, country, coordinates)

    def to_dict(self) -> dict:
        result: dict = {}
        result["city"] = from_str(self.city)
        result["street_name"] = from_str(self.street_name)
        result["street_address"] = from_str(self.street_address)
        result["zip_code"] = from_str(self.zip_code)
        result["state"] = from_str(self.state)
        result["country"] = from_str(self.country)
        result["coordinates"] = to_class(Coordinates, self.coordinates)
        return result


@dataclass
class CreditCard:
    cc_number: str

    @staticmethod
    def from_dict(obj: Any) -> 'CreditCard':
        assert isinstance(obj, dict)
        cc_number = from_str(obj.get("cc_number"))
        return CreditCard(cc_number)

    def to_dict(self) -> dict:
        result: dict = {}
        result["cc_number"] = from_str(self.cc_number)
        return result


@dataclass
class Employment:
    title: str
    key_skill: str

    @staticmethod
    def from_dict(obj: Any) -> 'Employment':
        assert isinstance(obj, dict)
        title = from_str(obj.get("title"))
        key_skill = from_str(obj.get("key_skill"))
        return Employment(title, key_skill)

    def to_dict(self) -> dict:
        result: dict = {}
        result["title"] = from_str(self.title)
        result["key_skill"] = from_str(self.key_skill)
        return result


@dataclass
class Subscription:
    plan: str
    status: str
    payment_method: str
    term: str

    @staticmethod
    def from_dict(obj: Any) -> 'Subscription':
        assert isinstance(obj, dict)
        plan = from_str(obj.get("plan"))
        status = from_str(obj.get("status"))
        payment_method = from_str(obj.get("payment_method"))
        term = from_str(obj.get("term"))
        return Subscription(plan, status, payment_method, term)

    def to_dict(self) -> dict:
        result: dict = {}
        result["plan"] = from_str(self.plan)
        result["status"] = from_str(self.status)
        result["payment_method"] = from_str(self.payment_method)
        result["term"] = from_str(self.term)
        return result


@dataclass
class RandomAddressModelElement:
    id: int
    uid: str
    password: str
    first_name: str
    last_name: str
    username: str
    email: str
    avatar: str
    gender: str
    phone_number: str
    social_insurance_number: int
    date_of_birth: datetime
    employment: Employment
    address: Address
    credit_card: CreditCard
    subscription: Subscription

    @staticmethod
    def from_dict(obj: Any) -> 'RandomAddressModelElement':
        assert isinstance(obj, dict)
        id = from_int(obj.get("id"))
        uid = from_str(obj.get("uid"))
        password = from_str(obj.get("password"))
        first_name = from_str(obj.get("first_name"))
        last_name = from_str(obj.get("last_name"))
        username = from_str(obj.get("username"))
        email = from_str(obj.get("email"))
        avatar = from_str(obj.get("avatar"))
        gender = from_str(obj.get("gender"))
        phone_number = from_str(obj.get("phone_number"))
        social_insurance_number = int(from_str(obj.get("social_insurance_number")))
        date_of_birth = from_datetime(obj.get("date_of_birth"))
        employment = Employment.from_dict(obj.get("employment"))
        address = Address.from_dict(obj.get("address"))
        credit_card = CreditCard.from_dict(obj.get("credit_card"))
        subscription = Subscription.from_dict(obj.get("subscription"))
        return RandomAddressModelElement(id, uid, password, first_name, last_name, username, email, avatar, gender,
                                         phone_number, social_insurance_number, date_of_birth, employment, address,
                                         credit_card, subscription)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_int(self.id)
        result["uid"] = str(self.uid)
        result["password"] = from_str(self.password)
        result["first_name"] = from_str(self.first_name)
        result["last_name"] = from_str(self.last_name)
        result["username"] = from_str(self.username)
        result["email"] = from_str(self.email)
        result["avatar"] = from_str(self.avatar)
        result["gender"] = from_str(self.gender)
        result["phone_number"] = from_str(self.phone_number)
        result["social_insurance_number"] = from_str(str(self.social_insurance_number))
        result["date_of_birth"] = self.date_of_birth.isoformat()
        result["employment"] = to_class(Employment, self.employment)
        result["address"] = to_class(Address, self.address)
        result["credit_card"] = to_class(CreditCard, self.credit_card)
        result["subscription"] = to_class(Subscription, self.subscription)
        return result


def random_address_model_from_dict(s: Any) -> List[RandomAddressModelElement]:
    return from_list(RandomAddressModelElement.from_dict, s)


def random_address_model_to_dict(x: List[RandomAddressModelElement]) -> Any:
    return from_list(lambda x: to_class(RandomAddressModelElement, x), x)
