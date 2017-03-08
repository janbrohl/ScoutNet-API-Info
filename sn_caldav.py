import icalendar
import caldav
import json
import datetime
import pytz

__version__ = "0.1"


DESCRIPTION_MAP = {"info": "Info", "kategorien": "Kategorie", "veranstalter": "Veranstalter",
                   "zielgruppe": "Zielgruppe", "link_text": "Link_Text"}


BERLIN = pytz.timezone("Europe/Berlin")


def decode_description(s):
    return {k.lower(): v for k, v in json.loads(s.replace('\\"', '"')).items()}


def encode_description(obj):
    return json.dumps({v: obj[k] for k, v in DESCRIPTION_MAP.items()}).replace('"', '\\"')


def get_cal(user, pw, group_id):
    url = "https://{user}:{pw}@webcal.scoutnet.de/webcal/{group_id}/".format(
        user=user, pw=pw, group_id=group_id)
    client = caldav.DAVClient(url)
    principal = client.principal()
    calendars = principal.calendars()
    return calendars[0]


class LocalEvent:
    EVENT_MAP = {"summary": "summary", "dtstart": "start", "dtend": "end",
                 "url": "url", "uid": "uid", "created": "created", "last-modified": "modified"}

    def __init__(self, start, end, summary, url="", info="", kategorien=None, veranstalter="", zielgruppe="", link_text="", uid=None, created=None, modified=None, caldav_event=None):
        self.start = start
        self.end = end
        self.summary = summary
        self.url = url
        self.info = info
        self.kategorien = [] if kategorien is None else kategorien
        self.veranstalter = veranstalter
        self.zielgruppe = zielgruppe
        self.link_text = link_text
        self.uid = uid
        self.created = created
        self.modified = modified
        self.caldav_event = caldav_event

    def to_ical(self):
        now = datetime.datetime.now(pytz.UTC)
        cal = icalendar.Calendar()
        cal.add('prodid', '-//Brohlsoft//ScoutNet.de Python-CalDAV//')
        cal.add('version', __version__)
        event = icalendar.Event()
        event.add("url", self.url)
        event.add('summary', self.summary)
        event.add('dtstart', self.start)
        event.add('dtend', self.end)
        event.add('created', self.created or now)
        event.add('dtstamp', self.modified or now)
        event.add('last-modified', self.modified or now)
        event.add('description', encode_description(dict(info=self.info, kategorien=self.kategorien,
                                                         veranstalter=self.veranstalter,
                                                         zielgruppe=self.zielgruppe,
                                                         link_text=self.link_text)))
        event.add('uid', self.uid or caldav.uuid.uuid4())
        cal.add_component(event)
        return cal.to_ical()

    @classmethod
    def from_ical(cls, s):
        cal = icalendar.Calendar.from_ical(s)
        event = cal.subcomponents[0]
        d = decode_description(event["description"])
        for k, v in cls.EVENT_MAP.items():
            d[v] = event[k]
        return cls(**d)

    @classmethod
    def load_caldav(cls, caldav_event):
        obj = cls.from_ical(caldav_event.data)
        obj.caldav_event = caldav_event
        return obj

    def save_caldav(self):
        s = self.to_ical()
        self.caldav_event.data = s
        self.caldav_event.save()

    def delete_caldav(self):
        self.caldav_event.delete()

    def add_to_cal(self, cal):
        self.caldav_event = cal.add_event(self.to_ical())
        return self.caldav_event

    def __repr__(self):
        return ("LocalEvent(start={start!r}, end={end!r}, summary={summary!r}, url={url!r}, info={info!r}, "
                "kategorien={kategorien!r}, veranstalter={veranstalter!r}, zielgruppe={zielgruppe!r}, "
                "link_text={link_text!r}, uid={uid!r}, created={created!r}, modified={modified!r}, "
                "caldav_event={caldav_event!r})").format(start=self.start, end=self.end, summary=self.summary,
                                                         url=self.url, info=self.info, kategorien=self.kategorien,
                                                         veranstalter=self.veranstalter, zielgruppe=self.zielgruppe,
                                                         link_text=self.link_text, uid=self.uid,
                                                         created=self.created, modified=self.modified,
                                                         caldav_event=self.caldav_event)


if __name__ == "__main__":
    import getpass
    user = input("User: ")
    pw = getpass.getpass()
    group_id = input("Group-ID: ")

    print()
    print("Searching calendar...")
    c = get_cal(user=user, pw=pw, group_id=group_id)
    print("found", c)
    print()
    print("New Event:")
    e = LocalEvent(BERLIN.localize(datetime.datetime(2100, 1, 1)),
                   BERLIN.localize(datetime.datetime(2100, 1, 2)),
                   "Testevent")
    print(e)
    print()
    print("Adding Event...")
    print("saved as", e.add_to_cal(c))
    print()
    input("Press enter to delete the event")
    e.delete_caldav()
    print("deleted")
