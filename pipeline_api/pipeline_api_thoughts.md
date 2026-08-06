# What this module will done?

Core purpose of this module is to handle all process in a thread safe pipeline but this module won't be generic QA or DevOps pipeline

API in the sentence can be deleted because i'm thinking aborting making this module as an API at beginning instead first purpose to write a local pipeline system that first checks quality controls, then have simulations with test cases and then deploys after all tests and quality checks done, it will securely  upload firmware to desired machine

## QualityChecks

I might change my idea and stop making Quality Control module an abstracted module, instead i can directly make it a module that checks requirements and flaws in circuits and other components that @Must be checked.

Secondly i want to turn experiment engine a direct module than an abstracted module that people or i must implement when i use everytime that's stupid design.

Workflow module is going to be abstracted because people might change it in a way they desire or work in local

## Pipeline

<pre>
<span style="color: #00D2FF; font-weight: bold;">+---------------------------+</span>
<span style="color: #00D2FF; font-weight: bold;">| Step 1: Thread-Safe Pipe  |</span> 
<span style="color: #00D2FF; font-weight: bold;">| (Core Ingestion)          |</span> --------+
<span style="color: #00D2FF; font-weight: bold;">+---------------------------+</span>         |
                                      |
                                      v
<span style="color: #00D2FF; font-weight: bold;">+---------------------------+</span>     <span style="color: #39FF14; font-weight: bold;">+---------------------------+</span>
<span style="color: #00D2FF; font-weight: bold;">| Step 3: Simulation        |</span>     <span style="color: #39FF14; font-weight: bold;">| Step 2: Quality Control   |</span>
<span style="color: #00D2FF; font-weight: bold;">| (Run with Test Cases)     |</span> <---<span style= "color:#39FF14">| (Local Code & Design Chk) |</span>
<span style="color: #00D2FF; font-weight: bold;">+---------------------------+</span>     <span style="color: #39FF14; font-weight: bold;">+---------------------------+</span>
    |
    | (All checks passed)
    v
<span style="color: #FF9F00; font-weight: bold;">+---------------------------+</span>
<span style="color: #FF9F00; font-weight: bold;">| Step 4: Secure Deployment |</span>
<span style="color: #FF9F00; font-weight: bold;">| (Upload to Machine)       |</span>
<span style="color: #FF9F00; font-weight: bold;">+---------------------------+</span>
</pre>

