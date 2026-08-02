# Watch Dog Timer?

## Purposes
I will write a supportive watch dog timer for embedded system threads
I want my all system asynchronous and thread-safe anything that has no business with other module must not affect it.
## How to do it?
A supportive watch dog timer should protect the systems reliabilty not the thread itself, so watch dog timer must be very sensitive to protect system, system should be immutable instead the mutable systems like linux, target audience is not just programmers or sofware enginners, we also want to medical researchers or electronic engineers to use this system so they shouldn't be abused in system with mutable options, that's why watch dog timer will watch every step of states and actions and will immediately stop running the action
