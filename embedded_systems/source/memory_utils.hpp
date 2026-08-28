#pragma once
#include <cstdint>
#include <cstring>
#include <atomic>
#include <memory>
#include <stdexcept>
#include <vector>

// LOW FOOTPRINT RING BUFFER

template <typename T>
class RingBuffer {
	private:
		// Buffer saves data in heap and immediately deletes when destructor is called
		std::unique_ptr<T[]> buffer;

		// We use 16-bit for capacity and indices, instead 64-bit size_t
		// Maximum capacity is 65535 element which is enough for hardware sensors
		const uint16_t capacity;

		// Atomic 16-bit indexes for lock-free async comm
		// Producer (Hardware/Network) increments the head, Consumer (Python) increments the tail
		std::atomic<uint16_t> head;
		std::atomic<uint16_t> tail;

	public:
		explicit RingBuffer(uint16_t size) : capacity(size), head(0), tail (0) {
			if (size == 0) throw std::invalid_argument("Capacity must be > 0");
			buffer = std::make_unique<T[]>(capacity);
		}

		bool push(const T& item) {
			uint16_t current_head = head.load(std::memory_order_relaxed);
			uint16_t next_head = (current_head + 1) % capacity;

			if (next_head == tail.load(std::memory_order_acquire)) {
				return false; // Buffer is full
			}

			buffer[current_head] = item;
			head.store(next_head, std::memory_order_release);
			return true;
		}

		bool pop(T& item) {
			uint16_t current_tail = tail.load(std::memory_order_relaxed);

			if (current_tail == head.load(std::memory_order_acquire)) {
				return false; // Buffer is empty
			}
			item = buffer[current_tail];
			tail.store((current_tail + 1) % capacity, std::memory_order_release);
			return true;
		}

		uint16_t available() const {
			uint16_t h = head.load(std::memory_order_acquire);
			uint16_t t = tail.load(std::memory_order_acquire);
			if (h >= t) return h - t;
			return capacity - t + h;
		}
};

// Packed Struct
// It prevents C++ compiler to place paddings between structs
// This ensures that it occupies exactly 5 bytes (1+1+2+1) in RAM or when coming from serial port.
#pragma pack(push, 1)
struct SensorPayload {
	uint8_t sensor_id; // 1 byte Max, 255 sensor
	uint8_t status_flags; // 1 byte bitmask (e.g. 0x01 Error, 0x02 Calibration)
	uint16_t value; // 2 byte
	uint8_t crc; // 1 byte checksum
};
#pragma pack(pop)


class Payloadparser {
	private:
		enum class State : uint8_t {WAIT_HEADER, READ_DATA};
		State current_state = State::WAIT_HEADER;

		uint8_t raw_data[sizeof(SensorPayload)];
		uint8_t byte_index = 0;

		uint8_t calculate_crc(const uint8_t* data, uint8_t length) const {
			uint8_t crc = 0;
			for (uint8_t i = 0; i < length; ++i) crc ^= data[i];
			return crc;
		}
	public:
		// Parses each byte from async stream according to its state
		bool parse_byte(uint8_t b, SensorPayload& out_payload) {
			switch(current_state) {
				case State::WAIT_HEADER:
					if (b == 0xAA) { // Example start byte head
						byte_index = 0;
						current_state = State::READ_DATA;
					}
					break;


			  case State::READ_DATA:
				  raw_data[byte_index++] = b;
				  if (byte_index == sizeof(SensorPayload)){
					  current_state = State::WAIT_HEADER;

					  // CRC Validation
					  if (calculate_crc(raw_data, 4) == raw_data[4]) {
						  // Transfer bit level data via  memory copying
						  std::memcpy(&out_payload, raw_data, sizeof(SensorPayload));
						  return true;
					  }
				  }
				  break;
      }
      return false;
		}
};
