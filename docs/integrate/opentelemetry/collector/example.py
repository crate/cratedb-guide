# OpenTelemetry demo application.
from opentelemetry import metrics


def main():

    meter = metrics.get_meter("testdrive.meter.name")
    temperature = meter.create_gauge("temperature")
    humidity = meter.create_gauge("humidity")

    temperature.set(42.42)
    humidity.set(84.84)


if __name__ == "__main__":
    main()
