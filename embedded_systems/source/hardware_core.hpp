#pragma once
#include <chrono>
#include <string>
#include <stdexcept>

// BaseErrorHandling class

class BaseErrorHandling {
	public:
		inline static void trigger_halt(const std::string& reason) {
			// For logging or sending emerge stop signals to hardware
			throw std::runtime_error("HALT SIGNAL" + reason);
		}

};

class WatchdogTimer {
	private:
		int timeout_ms;
		std::chrono::steady_clock::time_point last_feed_time;
	
	public:
		WatchdogTimer(int timeout) : timeout_ms(timeout) {feed(); } // Constructor

		inline void feed() {
			last_feed_time = std::chrono::steady_clock::now();
		}

		inline bool is_expired() const {
			auto now = std::chrono::steady_clock::now();
			auto elapsed = std::chrono::duration_cast<std::chrono::milliseconds>(now - last_feed_time).count();
			return elapsed > timeout_ms;
		}
};

enum class HardwareState {INIT, IDLE, RUNNING, ERROR};

class BaseStateMachine {
	private:
		hardwareState current_state = HardwareState::INIT;
	public:
		inline HardwareState get_state() const {return current_state; }
		inline void transition_to(HardwareState new_state) {
			current_state = new_state;
		}
};
