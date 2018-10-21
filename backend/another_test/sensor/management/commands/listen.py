from django.core.management.base import BaseCommand, CommandError
from sensor.models import Sensor
import paho.mqtt.client as mqtt
from time import sleep

class Command(BaseCommand):
    help ='Closes the specified poll for voting'
    
    def on_connect(self, client, userdata, flags, rc):
        self.stdout.write("Connected with result code "+ str(rc))
        client.subscribe('Bes')

    def on_message(self, client, userdata, msg):
        self.stdout.write('Got data from sensor...{}'.format(str(msg.payload,encoding='utf-8')))

        try:
            value = (str(msg.payload,encoding='utf-8'))
            self.stdout.write(str(value))
            id = Sensor.objects.create(value=value)
            self.stdout.write('sensor value created with id: {}'.format(id))
        except:
            self.stderr.write('error parse data')
        self.stdout.write(value)
    
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        self.stdout.write('Start to listen for connections...')
        client = mqtt.Client()
        client.on_connect = self.on_connect
        client.on_message = self.on_message
        client.connect("192.168.43.54", 1883, 60)
        client.loop_forever()
        