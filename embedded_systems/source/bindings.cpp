#include <pybind11/pybind11.h>
#include "memory_utils.hpp"

namespace py = pybind11;

PYBIND11_MODULE(labox_embedded_core, m) {
    // Sıkıştırılmış Struct'ı Python Class'ı olarak dışa aktar
    py::class_<SensorPayload>(m, "SensorPayload")
        .def_readonly("sensor_id", &SensorPayload::sensor_id)
        .def_readonly("status_flags", &SensorPayload::status_flags)
        .def_readonly("value", &SensorPayload::value);

    // uint8_t tutan RingBuffer'ı Python'a bağla
    py::class_<RingBuffer<uint8_t>>(m, "ByteRingBuffer")
        .def(py::init<uint16_t>())
        .def("available", &RingBuffer<uint8_t>::available)
        // Python bytearray'den besleme metodu eklenebilir
        ;
}
