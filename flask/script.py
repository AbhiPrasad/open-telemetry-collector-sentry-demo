import os

from opentelemetry import trace
from opentelemetry.ext.otcollector.trace_exporter import CollectorSpanExporter
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchExportSpanProcessor

exporter = CollectorSpanExporter(
    service_name="basic-service", endpoint="localhost:55678"
)

trace.set_tracer_provider(TracerProvider())
tracer = trace.get_tracer(__name__)
span_processor = BatchExportSpanProcessor(exporter)

trace.get_tracer_provider().add_span_processor(span_processor)
with tracer.start_as_current_span("foo"):
    with tracer.start_as_current_span("bar"):
        with tracer.start_as_current_span("baz"):
            print("Hello world from OpenTelemetry Python!")
